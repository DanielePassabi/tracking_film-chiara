const state = {
  data: null,
  posters: new Map(),
  sort: "episodes",
  query: "",
};

const fmt = new Intl.NumberFormat("it-IT");
const fmtOne = new Intl.NumberFormat("it-IT", {
  maximumFractionDigits: 1,
});

const $ = (selector) => document.querySelector(selector);

function formatDate(value) {
  if (!value) return "n.d.";
  return new Date(value).toLocaleDateString("it-IT", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}

function statCard(label, value, detail) {
  return `
    <article class="stat-card">
      <span>${label}</span>
      <strong>${value}</strong>
      <span>${detail}</span>
    </article>
  `;
}

function renderSummary(data) {
  const stats = data.stats;
  $("#summaryGrid").innerHTML = [
    statCard("Serie", fmt.format(stats.seriesCount), `${fmt.format(stats.followedShows)} seguite`),
    statCard("Episodi", fmt.format(stats.episodesSeen), `${fmt.format(stats.distinctEpisodes)} distinti`),
    statCard("Ore", fmtOne.format(stats.runtimeHours), "runtime stimato"),
    statCard("Periodo", "2018-2026", `${formatDate(stats.firstSeen)} - ${formatDate(stats.lastSeen)}`),
    statCard("Episodi rivisti", fmt.format(stats.rewatchedEpisodes), "marcati su Gossip Girl"),
  ].join("");

  $("#importRecords").textContent = fmt.format(data.archiveImport.records);
  $("#archiveTopSeries").textContent = data.archiveImport.topSeries || "serie recuperate";
  $("#rewatchCount").textContent = fmt.format(stats.rewatchedEpisodes);
}

function renderYearChart(data) {
  const values = data.years.map((year) => year.chartRecords);
  const max = Math.max(...values);
  $("#yearChart").innerHTML = data.years
    .map((year) => {
      const value = year.chartRecords;
      const width = Math.max(3, (value / max) * 100);
      const archiveRecords = year.records - year.chartRecords;
      const title = archiveRecords
        ? `${fmt.format(year.records)} record totali, ${fmt.format(archiveRecords)} in archivio`
        : `${fmt.format(year.records)} record`;
      return `
        <div class="bar-row">
          <span class="bar-label">${year.year}</span>
          <span class="bar-track"><span class="bar-fill" style="width:${width}%"></span></span>
          <span class="bar-value" title="${title}">${fmt.format(value)}</span>
        </div>
      `;
    })
    .join("");
}

function rankList(items, metric) {
  const max = Math.max(...items.map((item) => metric.value(item)));
  return `
    <div class="rank-list">
      ${items
        .map((item) => {
          const value = metric.value(item);
          const width = Math.max(5, (value / max) * 100);
          return `
            <article class="rank-item">
              <div class="rank-topline">
                <span>${metric.name(item)}</span>
                <span>${metric.format(value)}</span>
              </div>
              <div class="bar-track"><div class="bar-fill" style="width:${width}%"></div></div>
              <span class="rank-meta">${metric.meta(item)}</span>
            </article>
          `;
        })
        .join("")}
    </div>
  `;
}

function renderRanks(data) {
  $("#episodeRank").innerHTML = rankList(data.top.episodes.slice(0, 7), {
    name: (item) => item.name,
    value: (item) => item.episodesSeen,
    format: (value) => fmt.format(value),
    meta: (item) =>
      item.runtimeHours > 0
        ? `${fmtOne.format(item.runtimeHours)} ore stimate`
        : `${fmt.format(item.trackingRecords)} record nel tracking`,
  });

  $("#hourRank").innerHTML = rankList(data.top.hours.slice(0, 7), {
    name: (item) => item.name,
    value: (item) => item.runtimeHours,
    format: (value) => `${fmtOne.format(value)} h`,
    meta: (item) => `${fmt.format(item.trackingRecords)} record nel tracking`,
  });

  $("#monthRank").innerHTML = rankList(data.top.months.slice(0, 7), {
    name: (item) => item.label,
    value: (item) => item.records,
    format: (value) => fmt.format(value),
    meta: (item) => item.topSeries ? `${item.topSeries} in evidenza` : "mese intenso",
  });
}

function sortedSeries() {
  const query = state.query.trim().toLowerCase();
  const filtered = state.data.series.filter((item) => item.name.toLowerCase().includes(query));
  const sorters = {
    episodes: (a, b) => b.episodesSeen - a.episodesSeen,
    hours: (a, b) => b.runtimeHours - a.runtimeHours,
    recent: (a, b) => new Date(b.lastSeen || 0) - new Date(a.lastSeen || 0),
    rewatch: (a, b) => b.rewatchedEpisodes - a.rewatchedEpisodes,
  };
  return filtered.sort(sorters[state.sort]).slice(0, 60);
}

function seriesCard(item) {
  const lastSeen = item.lastSeen ? `Ultima traccia: ${formatDate(item.lastSeen)}` : "Ultima traccia non disponibile";
  const flags = [item.followed ? "seguita" : null, item.bulkRecords ? `${fmt.format(item.bulkRecords)} batch` : null]
    .filter(Boolean)
    .join(" · ");
  const poster = state.posters.get(item.name);
  const initials = item.name
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((word) => word[0])
    .join("")
    .toUpperCase();
  const posterMarkup = poster?.localPath
    ? `<img src="${poster.localPath}" alt="Poster di ${item.name}" loading="lazy" />`
    : `<span>${initials}</span>`;

  return `
    <article class="series-card">
      <div class="poster-frame ${poster?.localPath ? "" : "poster-fallback"}">
        ${posterMarkup}
      </div>
      <div class="series-body">
        <div>
          <h3>${item.name}</h3>
          <p class="series-meta">${lastSeen}${flags ? ` · ${flags}` : ""}</p>
        </div>
        <div class="series-stats">
          <span class="mini-stat">
            <strong>${fmt.format(item.episodesSeen || item.trackingEpisodes)}</strong>
            <span>episodi</span>
          </span>
          <span class="mini-stat">
            <strong>${fmtOne.format(item.runtimeHours)}</strong>
            <span>ore</span>
          </span>
          <span class="mini-stat">
            <strong>${fmt.format(item.rewatchedEpisodes)}</strong>
            <span>rivisti</span>
          </span>
        </div>
      </div>
    </article>
  `;
}

function renderSeries() {
  const items = sortedSeries();
  $("#seriesGrid").innerHTML = items.length
    ? items.map(seriesCard).join("")
    : '<p class="empty-state">Nessuna serie trovata.</p>';
}

function bindControls() {
  $("#searchInput").addEventListener("input", (event) => {
    state.query = event.target.value;
    renderSeries();
  });

  document.querySelectorAll(".segmented button").forEach((button) => {
    button.addEventListener("click", () => {
      state.sort = button.dataset.sort;
      document.querySelectorAll(".segmented button").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
      renderSeries();
    });
  });
}

async function init() {
  const response = await fetch("./data/polpetta-data.json");
  state.data = await response.json();
  try {
    const posterResponse = await fetch("./data/posters.json");
    const posterData = await posterResponse.json();
    state.posters = new Map(posterData.records.map((item) => [item.name, item]));
  } catch {
    state.posters = new Map();
  }
  renderSummary(state.data);
  renderYearChart(state.data);
  renderRanks(state.data);
  renderSeries();
  bindControls();
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

init().catch((error) => {
  document.body.innerHTML = `<main class="section-shell"><div class="empty-state">Errore nel caricamento dei dati: ${error.message}</div></main>`;
});
