# Discovery Summary

Fonte analizzata:

```text
C:\Users\danyp\Documents\Programmazione\Github\Repo\film-polpetta\data\raw
```

Audit generato il 2026-07-07.

## Sintesi numerica

- CSV trovati: 51.
- Righe totali: 8.708.
- File principale per il sito: `tracking-prod-records-v2.csv`, con 6.197 record.
- Serie distinte nel tracking principale: 137.
- Episodi distinti nel tracking principale: 5.938.
- Episodi visti secondo `user_tv_show_data.csv`: 6.047.
- Ore calcolabili dal runtime del tracking: circa 806,6.
- Serie seguite in `followed_tv_show.csv`: 129, di cui 125 attive.
- Serie in `user_tv_show_data.csv`: 137, di cui 119 con almeno un episodio visto.
- Episodi marcati come rivisti: 121 record in `rewatched_episode.csv`, tutti associati a `Gossip Girl`.
- Date nel tracking principale: dal 2018-04-20 al 2026-06-10.

## Avvertenze importanti

- Il mese 2018-04 contiene 3.148 record, di cui 2.936 nel solo 2018-04-20 e 206 nel 2018-04-23. E' ragionevole trattarlo come archivio recuperato del passato: va raccontato a parte ed escluso dai grafici principali.
- Anche il 2026-06-10 contiene molti record nello stesso secondo con `bulk_type = season`, quindi va mostrato come batch di stagione e non come cronologia minuto per minuto.
- `user_statistics.csv` non e' affidabile per gli episodi visti: riporta `nb_episodes_watched = 0`, mentre altri file contengono migliaia di episodi.
- `movie_name` e' vuoto nel tracking principale. La prima versione del sito dovrebbe quindi concentrarsi sulle serie TV.
- `vote_key` contiene codici tecnici, non un voto leggibile senza mappatura aggiuntiva.

## File da usare

| File | Uso consigliato |
| --- | --- |
| `tracking-prod-records-v2.csv` | Fonte principale per timeline, episodi, runtime, stagioni, batch e serie. |
| `user_tv_show_data.csv` | Conteggio episodi visti per serie e stato seguito/preferito. |
| `followed_tv_show.csv` | Lista serie seguite, stato attivo, data di follow. |
| `rewatched_episode.csv` | Episodi marcati come rivisti. Non equivale a cicli completi di rewatch. |
| `seen_episode_source.csv` | Origine dell'azione di visione, utile per capire se e' stata marcata da pagina episodio o stagione. |
| `show_seen_episode_latest.csv` | Ultimo episodio visto per alcune serie. |
| `stats-prod-cache.csv` | Statistiche recenti gia aggregate da TV Time, da usare con cautela. |
| `ratings-live-votes.csv`, `ratings-v2-prod-votes.csv`, `emotions-live-votes.csv` | Reazioni/voti grezzi, utili solo se decodifichiamo i codici. |

## File da escludere dal sito

Questi file servono al GDPR export ma non al regalo/sito:

- token e sessioni: `access_token.csv`, `refresh_token.csv`, `user_session.csv`, `auth-prod-login.csv`;
- device e advertising: `device_data.csv`, `user_device.csv`, `ad_identifier.csv`, `_appsflyer_ids.csv`, `installed_app.csv`;
- rete e privacy: `ip_address.csv`, `user_personal_data.csv`, `user_facebook_data.csv`, `user_facebook_like.csv`;
- social operativo: `friend.csv`, `user_connection.csv`, `user_social_data.csv`, `webhook_data.csv`.

## Top serie per episodi visti

Da `user_tv_show_data.csv`:

| Serie | Episodi |
| --- | ---: |
| Keeping Up with the Kardashians | 281 |
| Friends | 236 |
| Modern Family | 230 |
| How I Met Your Mother | 208 |
| The Vampire Diaries | 171 |
| Love Bugs | 170 |
| The Office (US) | 168 |
| Once Upon a Time (2011) | 166 |
| Totally Spies! | 156 |
| New Girl | 146 |

## Top serie per ore stimate

Da `tracking-prod-records-v2.csv`, con `runtime` interpretato in secondi:

| Serie | Episodi nel tracking | Ore stimate |
| --- | ---: | ---: |
| Modern Family | 250 | 87,5 |
| The Office (US) | 172 | 68,8 |
| The O.C. | 92 | 67,5 |
| The Kardashians | 60 | 45,5 |
| Cougar Town | 102 | 42,5 |
| Grace and Frankie | 71 | 35,0 |
| Outer Banks | 40 | 33,3 |
| Ginny & Georgia | 30 | 28,3 |
| Elite | 32 | 26,7 |
| Bridgerton | 24 | 24,9 |

## Attivita per anno

Da `tracking-prod-records-v2.csv`:

| Anno | Record |
| --- | ---: |
| 2018 | 271 + 3.148 di archivio |
| 2019 | 362 |
| 2020 | 336 |
| 2021 | 416 |
| 2022 | 595 |
| 2023 | 471 |
| 2024 | 241 |
| 2025 | 123 |
| 2026 | 234 |

## Mesi piu intensi

| Mese | Record |
| --- | ---: |
| 2023-05 | 338 |
| 2021-07 | 221 |
| 2020-08 | 193 |
| 2019-11 | 192 |
| 2022-12 | 177 |
| 2026-03 | 174 |
| 2022-01 | 171 |
| 2019-12 | 170 |
| 2024-01 | 156 |

## Direzione consigliata per il sito

Costruirei una mini app statica centrata su quattro viste:

1. Dashboard affettiva: totale serie, episodi, ore, periodo coperto, episodi rivisti e serie simbolo.
2. Timeline: anni e mesi, con badge per distinguere import/batch da visioni puntuali.
3. Libreria serie: ricerca, filtri, episodi visti, ore stimate, ultimo aggiornamento.
4. Schede speciali: top serie, episodi rivisti di Gossip Girl, periodi intensi, "comfort shows".

Da decidere insieme:

- Recuperiamo poster e metadati esterni oppure restiamo solo sui dati esportati?
- Il tono deve essere piu dashboard o piu album regalo?
- Nascondiamo completamente dati social/personali anche dal codice sorgente generato?
- Come vogliamo etichettare aprile 2018 dentro la timeline: "import storico", "recupero dati" o altro?
