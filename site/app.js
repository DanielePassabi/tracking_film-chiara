const state = {
  data: null,
  posters: new Map(),
  moviePosters: new Map(),
  view: "series",
  sort: "episodes",
  query: "",
};

const fmt = new Intl.NumberFormat("it-IT");
const fmtOne = new Intl.NumberFormat("it-IT", {
  maximumFractionDigits: 1,
});

const $ = (selector) => document.querySelector(selector);

const sortNotes = {
  series: {
    episodes: "Ordine: piu episodi visti, poi piu record nel tracking, poi piu ore stimate.",
    hours: "Ordine: piu ore stimate, poi piu episodi visti, poi titolo.",
    recent: "Ordine: ultima traccia piu recente, poi titolo.",
    rewatch: "Ordine: piu episodi rivisti, poi piu episodi visti, poi titolo.",
  },
  movies: {
    watched: "Ordine: piu visioni registrate, poi ultima visione piu recente, poi titolo.",
    hours: "Ordine: piu ore note, poi ultima visione piu recente, poi titolo.",
    recent: "Ordine: ultima visione o traccia piu recente, poi titolo.",
    watchlist: "Ordine: prima i film da vedere, poi ultima traccia piu recente, poi titolo.",
  },
};

const viewCopy = {
  series: {
    title: "Polpetta TV Diary",
    eyebrow: "TV Time export",
    lede: "Una memoria interattiva delle serie viste, fra maratone, comfort show e ritorni speciali.",
    timelineHeading: "Anni, picchi e import storici",
    timelineTitle: "Attivita per anno",
    timelinePill: "archivio separato",
    noteTitle: "Nota sui batch",
    noteText:
      "Aprile 2018 sembra un recupero massivo di cose viste prima: resta raccontato qui, ma non falsifica i grafici principali.",
    noteMetricLabel: "record nell'archivio del passato",
    noteMetricSmall: (data) => `${data.archiveImport.topSeries || "serie recuperate"} in cima a quel blocco`,
    ranksHeading: "Le serie che hanno lasciato piu traccia",
    rankTitles: ["Top episodi", "Top ore", "Mesi piu intensi"],
    libraryTitle: "Tutte le serie",
    searchPlaceholder: "Cerca una serie",
    empty: "Nessuna serie trovata.",
    spotlightTitle: "Gossip Girl e gli episodi rivisti",
    spotlightText:
      "A quanto pare, nell'universo di Polpetta l'Upper East Side non si visita una volta sola: ci si torna, episodio dopo episodio.",
    spotlightLabel: "episodi marcati come rivisti",
    footerDetail: "Dati TV Time puliti. Poster locali da TVMaze, con fallback per match mancanti.",
  },
  movies: {
    title: "Polpetta Movie Diary",
    eyebrow: "Film export",
    lede: "Una pagina parallela per film visti, watchlist e tracce lasciate nel vecchio export di TV Time.",
    timelineHeading: "Anni e serate cinema",
    timelineTitle: "Film visti per anno",
    timelinePill: "solo watch",
    noteTitle: "Watchlist",
    noteText:
      "Nel file film compaiono azioni diverse: guardato, seguito e da vedere. Qui la timeline conta solo i film segnati come visti.",
    noteMetricLabel: "record nella watchlist",
    noteMetricSmall: (data) => `${fmt.format(data.movies.stats.followedMovies)} film anche seguiti`,
    ranksHeading: "I film che raccontano meglio la libreria",
    rankTitles: ["Top ore note", "Mesi piu film", "Decenni uscita"],
    libraryTitle: "Tutti i film",
    searchPlaceholder: "Cerca un film",
    empty: "Nessun film trovato.",
    spotlightTitle: "La coda dei prossimi film",
    spotlightText:
      "La parte bella del tracker film e' che non racconta solo cosa e' gia successo: conserva anche i titoli messi da parte per dopo.",
    spotlightLabel: "film segnati da vedere",
    footerDetail: "Dati TV Time puliti. I poster film usano un fallback grafico quando non sono presenti asset locali.",
  },
};

function toDate(value) {
  if (!value) return null;
  const date = new Date(value.replace(" ", "T"));
  return Number.isNaN(date.getTime()) ? null : date;
}

function formatDate(value) {
  const date = toDate(value);
  if (!date) return "n.d.";
  return date.toLocaleDateString("it-IT", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function periodLabel(firstSeen, lastSeen) {
  const first = toDate(firstSeen);
  const last = toDate(lastSeen);
  if (!first || !last) return "n.d.";
  return first.getFullYear() === last.getFullYear()
    ? String(first.getFullYear())
    : `${first.getFullYear()}-${last.getFullYear()}`;
}

function currentData() {
  if (state.view === "movies") {
    return {
      stats: state.data.movies.stats,
      top: state.data.movies.top,
      years: state.data.movies.years,
      items: state.data.movies.items,
    };
  }
  return {
    stats: state.data.stats,
    top: state.data.top,
    years: state.data.years,
    items: state.data.series,
  };
}

function dateValue(...values) {
  for (const value of values) {
    const date = toDate(value);
    if (date) return date.getTime();
  }
  return 0;
}

function byName(a, b) {
  return a.name.localeCompare(b.name, "it", { sensitivity: "base" });
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

function renderChrome() {
  const copy = viewCopy[state.view];
  $("#page-title").textContent = copy.title;
  $("#heroEyebrow").textContent = copy.eyebrow;
  $("#heroLede").textContent = copy.lede;
  $("#timelineHeading").textContent = copy.timelineHeading;
  $("#timelineTitle").textContent = copy.timelineTitle;
  $("#timelinePill").textContent = copy.timelinePill;
  $("#noteTitle").textContent = copy.noteTitle;
  $("#noteText").textContent = copy.noteText;
  $("#noteMetricLabel").textContent = copy.noteMetricLabel;
  $("#ranksHeading").textContent = copy.ranksHeading;
  $("#rankTitleA").textContent = copy.rankTitles[0];
  $("#rankTitleB").textContent = copy.rankTitles[1];
  $("#rankTitleC").textContent = copy.rankTitles[2];
  $("#libraryTitle").textContent = copy.libraryTitle;
  $("#searchInput").placeholder = copy.searchPlaceholder;
  $("#spotlightTitle").textContent = copy.spotlightTitle;
  $("#spotlightText").textContent = copy.spotlightText;
  $("#spotlightLabel").textContent = copy.spotlightLabel;
  $("#footerBrand").textContent = copy.title;
  $("#footerDetail").textContent = copy.footerDetail;
  document.title = copy.title;
}

function renderSummary() {
  const data = currentData();
  const stats = data.stats;
  if (state.view === "movies") {
    $("#summaryGrid").innerHTML = [
      statCard("Film", fmt.format(stats.movieCount), `${fmt.format(stats.watchedMovies)} visti`),
      statCard("Watchlist", fmt.format(stats.watchlistMovies), `${fmt.format(stats.followedMovies)} seguiti`),
      statCard("Ore note", fmtOne.format(stats.runtimeHours), "runtime disponibile"),
      statCard("Periodo", periodLabel(stats.firstSeen, stats.lastSeen), `${formatDate(stats.firstSeen)} - ${formatDate(stats.lastSeen)}`),
      statCard("Voti", fmt.format(stats.ratedMovies), `${fmt.format(stats.emotionMovies)} con reaction`),
    ].join("");

    $("#importRecords").textContent = fmt.format(stats.watchlistRecords);
    $("#noteMetricSmall").textContent = viewCopy.movies.noteMetricSmall(state.data);
    $("#rewatchCount").textContent = fmt.format(stats.watchlistMovies);
    return;
  }

  $("#summaryGrid").innerHTML = [
    statCard("Serie", fmt.format(stats.seriesCount), `${fmt.format(stats.followedShows)} seguite`),
    statCard("Episodi", fmt.format(stats.episodesSeen), `${fmt.format(stats.distinctEpisodes)} distinti`),
    statCard("Ore", fmtOne.format(stats.runtimeHours), "runtime stimato"),
    statCard("Periodo", periodLabel(stats.firstSeen, stats.lastSeen), `${formatDate(stats.firstSeen)} - ${formatDate(stats.lastSeen)}`),
    statCard("Episodi rivisti", fmt.format(stats.rewatchedEpisodes), "marcati su Gossip Girl"),
  ].join("");

  $("#importRecords").textContent = fmt.format(state.data.archiveImport.records);
  $("#noteMetricSmall").textContent = viewCopy.series.noteMetricSmall(state.data);
  $("#rewatchCount").textContent = fmt.format(stats.rewatchedEpisodes);
}

function renderYearChart() {
  const values = currentData().years.map((year) => year.chartRecords);
  const max = Math.max(1, ...values);
  $("#yearChart").innerHTML = currentData()
    .years.map((year) => {
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
  if (!items.length) {
    return '<p class="empty-state compact-empty">Nessun dato disponibile.</p>';
  }
  const max = Math.max(1, ...items.map((item) => metric.value(item)));
  return `
    <div class="rank-list">
      ${items
        .map((item) => {
          const value = metric.value(item);
          const width = Math.max(5, (value / max) * 100);
          return `
            <article class="rank-item">
              <div class="rank-topline">
                <span>${escapeHtml(metric.name(item))}</span>
                <span>${metric.format(value)}</span>
              </div>
              <div class="bar-track"><div class="bar-fill" style="width:${width}%"></div></div>
              <span class="rank-meta">${escapeHtml(metric.meta(item))}</span>
            </article>
          `;
        })
        .join("")}
    </div>
  `;
}

function renderRanks() {
  const data = currentData();
  if (state.view === "movies") {
    $("#episodeRank").innerHTML = rankList(data.top.hours.slice(0, 7), {
      name: (item) => item.name,
      value: (item) => item.runtimeHours,
      format: (value) => `${fmtOne.format(value)} h`,
      meta: (item) => item.lastWatched ? `Visto il ${formatDate(item.lastWatched)}` : "runtime disponibile",
    });

    $("#hourRank").innerHTML = rankList(data.top.months.slice(0, 7), {
      name: (item) => item.label,
      value: (item) => item.records,
      format: (value) => fmt.format(value),
      meta: (item) => item.topMovie ? `${item.topMovie} in evidenza` : "mese cinematografico",
    });

    $("#monthRank").innerHTML = rankList(data.top.releaseDecades.slice(0, 7), {
      name: (item) => item.label,
      value: (item) => item.records,
      format: (value) => fmt.format(value),
      meta: () => "film visti usciti in questo decennio",
    });
    return;
  }

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

function sortedItems() {
  const query = state.query.trim().toLowerCase();
  const filtered = currentData().items.filter((item) => item.name.toLowerCase().includes(query));
  const sorters = {
    episodes: (a, b) =>
      b.episodesSeen - a.episodesSeen ||
      b.trackingRecords - a.trackingRecords ||
      b.runtimeHours - a.runtimeHours ||
      byName(a, b),
    hours: (a, b) =>
      b.runtimeHours - a.runtimeHours ||
      b.episodesSeen - a.episodesSeen ||
      dateValue(b.lastSeen, b.lastWatched, b.lastTracked) - dateValue(a.lastSeen, a.lastWatched, a.lastTracked) ||
      byName(a, b),
    recent: (a, b) =>
      dateValue(b.lastSeen, b.lastWatched, b.lastTracked) - dateValue(a.lastSeen, a.lastWatched, a.lastTracked) ||
      byName(a, b),
    rewatch: (a, b) =>
      b.rewatchedEpisodes - a.rewatchedEpisodes ||
      b.episodesSeen - a.episodesSeen ||
      byName(a, b),
    watched: (a, b) =>
      b.watchRecords - a.watchRecords ||
      dateValue(b.lastWatched, b.lastTracked) - dateValue(a.lastWatched, a.lastTracked) ||
      byName(a, b),
    watchlist: (a, b) =>
      Number(b.watchlist) - Number(a.watchlist) ||
      b.watchlistRecords - a.watchlistRecords ||
      dateValue(b.lastTracked, b.lastWatched) - dateValue(a.lastTracked, a.lastWatched) ||
      byName(a, b),
  };
  return filtered.sort(sorters[state.sort]).slice(0, 60);
}

function initialsFor(name) {
  return name
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((word) => word[0])
    .join("")
    .toUpperCase();
}

function seriesCard(item) {
  const safeName = escapeHtml(item.name);
  const lastSeen = item.lastSeen ? `Ultima traccia: ${formatDate(item.lastSeen)}` : "Ultima traccia non disponibile";
  const flags = [item.followed ? "seguita" : null, item.bulkRecords ? `${fmt.format(item.bulkRecords)} batch` : null]
    .filter(Boolean)
    .join(" · ");
  const poster = state.posters.get(item.name);
  const posterMarkup = poster?.localPath
    ? `<img src="${poster.localPath}" alt="Poster di ${safeName}" loading="lazy" />`
    : `<span>${escapeHtml(initialsFor(item.name))}</span>`;

  return `
    <article class="series-card">
      <div class="poster-frame ${poster?.localPath ? "" : "poster-fallback"}">
        ${posterMarkup}
      </div>
      <div class="series-body">
        <div>
          <h3>${safeName}</h3>
          <p class="series-meta">${escapeHtml(lastSeen)}${flags ? ` · ${escapeHtml(flags)}` : ""}</p>
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

function movieCard(item) {
  const safeName = escapeHtml(item.name);
  const poster = state.moviePosters.get(item.name);
  const posterMarkup = poster?.localPath
    ? `<img src="${poster.localPath}" alt="Poster di ${safeName}" loading="lazy" />`
    : `<span>${escapeHtml(initialsFor(item.name))}</span>`;
  const dateLabel = item.lastWatched
    ? `Visto: ${formatDate(item.lastWatched)}`
    : item.lastTracked
      ? `Tracciato: ${formatDate(item.lastTracked)}`
      : "Data non disponibile";
  const flags = [
    item.watched ? "visto" : null,
    item.watchlist ? "da vedere" : null,
    item.followed ? "seguito" : null,
    item.releaseYear ? String(item.releaseYear) : null,
  ]
    .filter(Boolean)
    .join(" · ");

  return `
    <article class="series-card movie-card">
      <div class="poster-frame ${poster?.localPath ? "" : "poster-fallback movie-fallback"}">
        ${posterMarkup}
      </div>
      <div class="series-body">
        <div>
          <h3>${safeName}</h3>
          <p class="series-meta">${escapeHtml(dateLabel)}${flags ? ` · ${escapeHtml(flags)}` : ""}</p>
        </div>
        <div class="series-stats">
          <span class="mini-stat">
            <strong>${fmt.format(item.watchRecords)}</strong>
            <span>visioni</span>
          </span>
          <span class="mini-stat">
            <strong>${fmtOne.format(item.runtimeHours)}</strong>
            <span>ore</span>
          </span>
          <span class="mini-stat">
            <strong>${item.releaseYear || "n.d."}</strong>
            <span>uscita</span>
          </span>
        </div>
      </div>
    </article>
  `;
}

function renderLibrary() {
  const items = sortedItems();
  const copy = viewCopy[state.view];
  $("#seriesGrid").innerHTML = items.length
    ? items.map((item) => (state.view === "movies" ? movieCard(item) : seriesCard(item))).join("")
    : `<p class="empty-state">${copy.empty}</p>`;
}

function setSortButtons() {
  const sorts =
    state.view === "movies"
      ? [
          ["watched", "Visioni"],
          ["hours", "Ore"],
          ["recent", "Recenti"],
          ["watchlist", "Da vedere"],
        ]
      : [
          ["episodes", "Episodi"],
          ["hours", "Ore"],
          ["recent", "Recenti"],
          ["rewatch", "Rivisti"],
        ];

  state.sort = sorts.some(([key]) => key === state.sort) ? state.sort : sorts[0][0];
  $("#sortNote").textContent = sortNotes[state.view][state.sort];
  $("#sortControls").innerHTML = sorts
    .map(
      ([key, label]) => `
        <button class="${key === state.sort ? "active" : ""}" data-sort="${key}">${label}</button>
      `,
    )
    .join("");

  document.querySelectorAll("#sortControls button").forEach((button) => {
    button.addEventListener("click", () => {
      state.sort = button.dataset.sort;
      setSortButtons();
      renderLibrary();
    });
  });
}

function renderAll() {
  renderChrome();
  renderSummary();
  renderYearChart();
  renderRanks();
  setSortButtons();
  renderLibrary();
  document.querySelectorAll("[data-view]").forEach((button) => {
    button.classList.toggle("active", button.dataset.view === state.view);
    button.setAttribute("aria-pressed", String(button.dataset.view === state.view));
  });
}

function bindControls() {
  $("#searchInput").addEventListener("input", (event) => {
    state.query = event.target.value;
    renderLibrary();
  });

  document.querySelectorAll("[data-view]").forEach((button) => {
    button.addEventListener("click", () => {
      state.view = button.dataset.view;
      state.query = "";
      $("#searchInput").value = "";
      renderAll();
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
  try {
    const moviePosterResponse = await fetch("./data/movie-posters.json");
    const moviePosterData = await moviePosterResponse.json();
    state.moviePosters = new Map(moviePosterData.records.map((item) => [item.name, item]));
  } catch {
    state.moviePosters = new Map();
  }
  bindControls();
  renderAll();
  if (window.lucide) {
    window.lucide.createIcons();
  }
}

init().catch((error) => {
  document.body.innerHTML = `<main class="section-shell"><div class="empty-state">Errore nel caricamento dei dati: ${escapeHtml(error.message)}</div></main>`;
});
