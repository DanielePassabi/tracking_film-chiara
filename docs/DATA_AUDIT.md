# Data Audit

Generato: `2026-07-07T12:57:57`

## Sintesi

- CSV trovati: **51**
- Righe totali: **8708**
- Cartella export: `C:\Users\danyp\Documents\Programmazione\Github\Repo\film-polpetta\data\raw`

## Tipi di file ipotizzati

| Tipo ipotizzato | File |
| --------------- | ---- |
| comments        | 1    |
| episodes        | 21   |
| people/social   | 23   |
| series          | 5    |
| unknown         | 1    |

## File

| File                                 | Tipo          | Righe | Colonne | Encoding  | Separatore |
| ------------------------------------ | ------------- | ----- | ------- | --------- | ---------- |
| _appsflyer_ids.csv                   | people/social | 2     | 4       | utf-8-sig | ','        |
| access_token.csv                     | people/social | 1     | 7       | utf-8-sig | ','        |
| ad_identifier.csv                    | people/social | 2     | 5       | utf-8-sig | ','        |
| auth-prod-login.csv                  | episodes      | 4     | 16      | utf-8-sig | ','        |
| device_data.csv                      | unknown       | 4     | 6       | utf-8-sig | ','        |
| emotions-live-votes.csv              | episodes      | 17    | 8       | utf-8-sig | ','        |
| episode_comments_last_read_date.csv  | episodes      | 2     | 8       | utf-8-sig | ','        |
| followed_tv_show.csv                 | series        | 129   | 11      | utf-8-sig | ','        |
| followed_tv_show_source.csv          | series        | 72    | 6       | utf-8-sig | ','        |
| friend.csv                           | people/social | 25    | 5       | utf-8-sig | ','        |
| gdpr_requests.csv                    | comments      | 1     | 9       | utf-8-sig | ','        |
| install_tracking.csv                 | people/social | 3     | 7       | utf-8-sig | ','        |
| installed_app.csv                    | people/social | 6     | 6       | utf-8-sig | ','        |
| ip_address.csv                       | people/social | 59    | 13      | utf-8-sig | ','        |
| lists-prod-lists.csv                 | episodes      | 2     | 15      | utf-8-sig | ','        |
| ratings-3-prod-episode_votes.csv     | episodes      | 4     | 7       | utf-8-sig | ','        |
| ratings-live-votes.csv               | episodes      | 312   | 8       | utf-8-sig | ','        |
| ratings-v2-prod-votes.csv            | episodes      | 16    | 8       | utf-8-sig | ','        |
| recommendations-prod-user-scores.csv | episodes      | 1     | 8       | utf-8-sig | ','        |
| recommendations-prod-user-shows.csv  | episodes      | 1     | 6       | utf-8-sig | ','        |
| referral.csv                         | people/social | 1     | 9       | utf-8-sig | ','        |
| refresh_token.csv                    | people/social | 2     | 6       | utf-8-sig | ','        |
| rewatched_episode.csv                | episodes      | 121   | 8       | utf-8-sig | ','        |
| seen_episode_source.csv              | episodes      | 132   | 8       | utf-8-sig | ','        |
| show_addiction_score.csv             | series        | 46    | 7       | utf-8-sig | ','        |
| show_seen_episode_latest.csv         | episodes      | 46    | 6       | utf-8-sig | ','        |
| stats-prod-cache.csv                 | episodes      | 2     | 12      | utf-8-sig | ','        |
| tracking-deployment-prod-tracks.csv  | episodes      | 1     | 7       | utf-8-sig | ','        |
| tracking-prod-count-by-timeframe.csv | episodes      | 2     | 9       | utf-8-sig | ','        |
| tracking-prod-records-v2.csv         | episodes      | 6197  | 29      | utf-8-sig | ','        |
| tracking-prod-records.csv            | episodes      | 985   | 30      | utf-8-sig | ','        |
| tv_show_user_emotion_count.csv       | series        | 5     | 7       | utf-8-sig | ','        |
| user.csv                             | series        | 1     | 48      | utf-8-sig | ','        |
| user_badge.csv                       | people/social | 3     | 4       | utf-8-sig | ','        |
| user_connection.csv                  | people/social | 75    | 5       | utf-8-sig | ','        |
| user_device.csv                      | people/social | 3     | 5       | utf-8-sig | ','        |
| user_facebook_data.csv               | people/social | 1     | 10      | utf-8-sig | ','        |
| user_facebook_like.csv               | people/social | 181   | 6       | utf-8-sig | ','        |
| user_last_updated.csv                | people/social | 1     | 4       | utf-8-sig | ','        |
| user_mail_sent_status.csv            | people/social | 1     | 11      | utf-8-sig | ','        |
| user_membership.csv                  | people/social | 1     | 9       | utf-8-sig | ','        |
| user_personal_data.csv               | people/social | 4     | 6       | utf-8-sig | ','        |
| user_platform.csv                    | people/social | 1     | 8       | utf-8-sig | ','        |
| user_session.csv                     | people/social | 4     | 10      | utf-8-sig | ','        |
| user_setting.csv                     | people/social | 32    | 6       | utf-8-sig | ','        |
| user_social_data.csv                 | people/social | 1     | 8       | utf-8-sig | ','        |
| user_statistics.csv                  | episodes      | 1     | 13      | utf-8-sig | ','        |
| user_tv_show_data.csv                | episodes      | 137   | 6       | utf-8-sig | ','        |
| watched_on_episode.csv               | episodes      | 1     | 8       | utf-8-sig | ','        |
| webhook_data.csv                     | people/social | 1     | 8       | utf-8-sig | ','        |
| where-to-watch-prod-table.csv        | episodes      | 56    | 13      | utf-8-sig | ','        |

## Colonne condivise

| Colonna               | File | Presente in                                                                                                                                                                 |
| --------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id               | 49   | _appsflyer_ids.csv, access_token.csv, ad_identifier.csv, auth-prod-login.csv, emotions-live-votes.csv, episode_comments_last_read_date.csv...                               |
| created_at            | 40   | _appsflyer_ids.csv, access_token.csv, ad_identifier.csv, device_data.csv, episode_comments_last_read_date.csv, followed_tv_show.csv...                                      |
| updated_at            | 38   | _appsflyer_ids.csv, access_token.csv, ad_identifier.csv, device_data.csv, episode_comments_last_read_date.csv, followed_tv_show.csv...                                      |
| episode_number        | 18   | auth-prod-login.csv, emotions-live-votes.csv, episode_comments_last_read_date.csv, lists-prod-lists.csv, ratings-3-prod-episode_votes.csv, ratings-live-votes.csv...        |
| movie_name            | 14   | auth-prod-login.csv, emotions-live-votes.csv, lists-prod-lists.csv, ratings-3-prod-episode_votes.csv, ratings-live-votes.csv, ratings-v2-prod-votes.csv...                  |
| series_name           | 14   | auth-prod-login.csv, emotions-live-votes.csv, lists-prod-lists.csv, ratings-3-prod-episode_votes.csv, ratings-live-votes.csv, ratings-v2-prod-votes.csv...                  |
| season_number         | 14   | auth-prod-login.csv, emotions-live-votes.csv, lists-prod-lists.csv, ratings-3-prod-episode_votes.csv, ratings-live-votes.csv, ratings-v2-prod-votes.csv...                  |
| id                    | 11   | access_token.csv, device_data.csv, gdpr_requests.csv, install_tracking.csv, user.csv, user_personal_data.csv...                                                             |
| episode_id            | 11   | emotions-live-votes.csv, episode_comments_last_read_date.csv, ratings-3-prod-episode_votes.csv, ratings-live-votes.csv, ratings-v2-prod-votes.csv, rewatched_episode.csv... |
| tv_show_name          | 10   | episode_comments_last_read_date.csv, followed_tv_show.csv, followed_tv_show_source.csv, rewatched_episode.csv, seen_episode_source.csv, show_addiction_score.csv...         |
| name                  | 8    | device_data.csv, install_tracking.csv, lists-prod-lists.csv, user.csv, user_facebook_data.csv, user_facebook_like.csv...                                                    |
| source                | 7    | followed_tv_show_source.csv, gdpr_requests.csv, install_tracking.csv, seen_episode_source.csv, user_connection.csv, user_session.csv...                                     |
| tv_show_id            | 6    | followed_tv_show.csv, followed_tv_show_source.csv, show_addiction_score.csv, show_seen_episode_latest.csv, tv_show_user_emotion_count.csv, user_tv_show_data.csv            |
| uuid                  | 5    | emotions-live-votes.csv, ratings-live-votes.csv, ratings-v2-prod-votes.csv, tracking-prod-records-v2.csv, tracking-prod-records.csv                                         |
| type                  | 5    | lists-prod-lists.csv, stats-prod-cache.csv, tracking-prod-count-by-timeframe.csv, tracking-prod-records.csv, where-to-watch-prod-table.csv                                  |
| device_id             | 4    | device_data.csv, installed_app.csv, refresh_token.csv, user_device.csv                                                                                                      |
| value                 | 4    | device_data.csv, install_tracking.csv, user_personal_data.csv, user_setting.csv                                                                                             |
| vote_key              | 4    | emotions-live-votes.csv, ratings-3-prod-episode_votes.csv, ratings-live-votes.csv, ratings-v2-prod-votes.csv                                                                |
| episode_season_number | 4    | episode_comments_last_read_date.csv, rewatched_episode.csv, seen_episode_source.csv, watched_on_episode.csv                                                                 |
| timezone              | 3    | ip_address.csv, user.csv, user_facebook_data.csv                                                                                                                            |
| runtime               | 3    | tracking-prod-count-by-timeframe.csv, tracking-prod-records-v2.csv, tracking-prod-records.csv                                                                               |
| app_id                | 2    | access_token.csv, installed_app.csv                                                                                                                                         |
| cpt                   | 2    | access_token.csv, rewatched_episode.csv                                                                                                                                     |
| range_key             | 2    | auth-prod-login.csv, where-to-watch-prod-table.csv                                                                                                                          |
| hash_key              | 2    | auth-prod-login.csv, where-to-watch-prod-table.csv                                                                                                                          |
| username              | 2    | auth-prod-login.csv, user_facebook_data.csv                                                                                                                                 |
| external_id           | 2    | auth-prod-login.csv, webhook_data.csv                                                                                                                                       |
| entity_type           | 2    | stats-prod-cache.csv, tracking-prod-records.csv                                                                                                                             |
| count                 | 2    | tracking-prod-count-by-timeframe.csv, tv_show_user_emotion_count.csv                                                                                                        |
| total_series_runtime  | 2    | tracking-prod-records-v2.csv, tracking-prod-records.csv                                                                                                                     |

## Dettaglio colonne

### _appsflyer_ids.csv

- Tipo ipotizzato: `people/social`
- Righe: `2`
- Colonne: `4`

| Colonna             | Piena  | Unici | Range                                      | Esempi                                   |
| ------------------- | ------ | ----- | ------------------------------------------ | ---------------------------------------- |
| appsflyer_device_id | 100.0% | 2     |                                            | [redacted]                               |
| created_at          | 100.0% | 2     | 2021-06-17T17:58:09 -> 2021-07-22T10:29:50 | 2021-06-17 17:58:09, 2021-07-22 10:29:50 |
| updated_at          | 100.0% | 2     | 2021-06-17T17:58:09 -> 2021-07-22T10:29:50 | 2021-06-17 17:58:09, 2021-07-22 10:29:50 |
| user_id             | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                 |

### access_token.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `7`

| Colonna      | Piena  | Unici | Range                                      | Esempi              |
| ------------ | ------ | ----- | ------------------------------------------ | ------------------- |
| app_id       | 100.0% | 1     | 1.0 -> 1.0                                 | 1                   |
| access_token | 100.0% | 1     |                                            | [redacted]          |
| created_at   | 100.0% | 1     | 2018-04-20T10:20:22 -> 2018-04-20T10:20:22 | 2018-04-20 10:20:22 |
| updated_at   | 100.0% | 1     | 2018-04-20T10:20:22 -> 2018-04-20T10:20:22 | 2018-04-20 10:20:22 |
| cpt          | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| id           | 100.0% | 1     | 20050835.0 -> 20050835.0                   | 20050835            |
| user_id      | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |

### ad_identifier.csv

- Tipo ipotizzato: `people/social`
- Righe: `2`
- Colonne: `5`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                                     |
| ---------- | ------ | ----- | ------------------------------------------ | -------------------------------------------------------------------------- |
| ad_id      | 100.0% | 2     |                                            | 00000000-0000-0000-0000-000000000000, EEAAF8A5-2835-460A-AD5C-486EF92BF481 |
| id_type    | 100.0% | 1     |                                            | IDFA                                                                       |
| created_at | 100.0% | 2     | 2018-04-20T20:20:46 -> 2020-03-18T09:08:33 | 2020-03-18 09:08:33, 2018-04-20 20:20:46                                   |
| updated_at | 100.0% | 2     | 2018-04-20T20:20:46 -> 2020-03-18T09:08:33 | 2020-03-18 09:08:33, 2018-04-20 20:20:46                                   |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                   |

### auth-prod-login.csv

- Tipo ipotizzato: `episodes`
- Righe: `4`
- Colonne: `16`

| Colonna          | Piena  | Unici | Range                                                                | Esempi                                                            |
| ---------------- | ------ | ----- | -------------------------------------------------------------------- | ----------------------------------------------------------------- |
| user_id          | 100.0% | 1     | 20319846.0 -> 20319846.0                                             | 20319846                                                          |
| valid_until      | 25.0%  | 1     | 2026-07-07T13:28:26.322404+00:00 -> 2026-07-07T13:28:26.322404+00:00 | 2026-07-07T13:28:26.322404545Z                                    |
| reset_token      | 25.0%  | 1     |                                                                      | [redacted]                                                        |
| email            | 75.0%  | 1     |                                                                      | [redacted]                                                        |
| range_key        | 100.0% | 3     |                                                                      | [redacted-long-token], facebook:1826457200982268, tvtime:20319846 |
| hash_key         | 100.0% | 3     |                                                                      | password_reset_token, [redacted-email], <no-email-set>            |
| provider         | 75.0%  | 2     |                                                                      | facebook, tvtime                                                  |
| username         | 25.0%  | 1     | 20319846.0 -> 20319846.0                                             | 20319846                                                          |
| encrypted_secret | 0.0%   | 0     |                                                                      |                                                                   |
| encrypted_token  | 0.0%   | 0     |                                                                      |                                                                   |
| external_id      | 50.0%  | 1     | 1826457200982268.0 -> 1826457200982268.0                             | 1826457200982268                                                  |
| password_hash    | 25.0%  | 1     |                                                                      | [redacted]                                                        |
| movie_name       | 0.0%   | 0     |                                                                      |                                                                   |
| series_name      | 0.0%   | 0     |                                                                      |                                                                   |
| season_number    | 0.0%   | 0     |                                                                      |                                                                   |
| episode_number   | 0.0%   | 0     |                                                                      |                                                                   |

### device_data.csv

- Tipo ipotizzato: `unknown`
- Righe: `4`
- Colonne: `6`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                   |
| ---------- | ------ | ----- | ------------------------------------------ | ---------------------------------------- |
| id         | 100.0% | 4     | 50496489.0 -> 184420347.0                  | 50496490, 50496489, 184420347, 184420346 |
| device_id  | 100.0% | 2     |                                            | [redacted]                               |
| name       | 100.0% | 2     |                                            | model, os                                |
| value      | 100.0% | 3     |                                            | iPhone9,4, ios, iPhone12,3               |
| created_at | 100.0% | 2     | 2018-04-20T10:20:22 -> 2021-07-22T10:28:08 | 2018-04-20 10:20:22, 2021-07-22 10:28:08 |
| updated_at | 100.0% | 2     | 2018-04-20T10:20:22 -> 2021-07-22T10:28:08 | 2018-04-20 10:20:22, 2021-07-22 10:28:08 |

### emotions-live-votes.csv

- Tipo ipotizzato: `episodes`
- Righe: `17`
- Colonne: `8`

| Colonna        | Piena  | Unici | Range                    | Esempi                                                                                                                                                                                                                                                   |
| -------------- | ------ | ----- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0 | 20319846                                                                                                                                                                                                                                                 |
| uuid           | 100.0% | 16    |                          | 05807f03-e989-47e3-8494-7964df0a7f12, aa96c2e5-af6d-4135-af44-9d22b9176d92, ea2c6fa3-053f-4cc3-b34c-9bcf519b695f, 40b1a8ca-b35c-451f-9dfd-2c4186bae401, 8ed79c61-2216-477a-a52e-871d7895ca2b                                                             |
| vote_key       | 100.0% | 17    |                          | 05807f03-e989-47e3-8494-7964df0a7f12-20319846-33, aa96c2e5-af6d-4135-af44-9d22b9176d92-20319846-38, ea2c6fa3-053f-4cc3-b34c-9bcf519b695f-20319846-28, 05807f03-e989-47e3-8494-7964df0a7f12-20319846-32, 40b1a8ca-b35c-451f-9dfd-2c4186bae401-20319846-30 |
| episode_id     | 100.0% | 1     | 0.0 -> 0.0               | 0                                                                                                                                                                                                                                                        |
| movie_name     | 100.0% | 16    |                          | Thor: Love and Thunder, Frozen II, Spider-Man: Far From Home, Guardians of the Galaxy Vol. 3, Avatar: The Way of Water                                                                                                                                   |
| series_name    | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                          |
| season_number  | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                          |
| episode_number | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                          |

### episode_comments_last_read_date.csv

- Tipo ipotizzato: `episodes`
- Righe: `2`
- Colonne: `8`

| Colonna                | Piena  | Unici | Range                                      | Esempi                                                       |
| ---------------------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------ |
| tv_show_name           | 100.0% | 2     |                                            | Friends, Raven's Home                                        |
| episode_season_number  | 100.0% | 2     | 1.0 -> 5.0                                 | 5, 1                                                         |
| episode_number         | 100.0% | 2     | 8.0 -> 17.0                                | 17, 8                                                        |
| user_id                | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                     |
| episode_id             | 100.0% | 2     | 303934.0 -> 6247225.0                      | 303934, 6247225                                              |
| last_comment_read_date | 100.0% | 2     |                                            | 2018-04-25 07:54:37 +0000 UTC, 2018-04-25 07:51:53 +0000 UTC |
| created_at             | 100.0% | 2     | 2018-04-25T07:51:53 -> 2018-04-25T07:54:37 | 2018-04-25 07:54:37, 2018-04-25 07:51:53                     |
| updated_at             | 100.0% | 2     | 2018-04-25T07:51:53 -> 2018-04-25T07:54:37 | 2018-04-25 07:54:37, 2018-04-25 07:51:53                     |

### followed_tv_show.csv

- Tipo ipotizzato: `series`
- Righe: `129`
- Colonne: `11`

| Colonna             | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| ------------------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| tv_show_name        | 100.0% | 129   |                                            | Lizzie McGuire, Phil of the Future, Recess, Hercules, Two and a Half Men                                |
| tv_show_id          | 100.0% | 129   | 71119.0 -> 426779.0                        | 71119, 71714, 71780, 72163, 72227                                                                       |
| created_at          | 100.0% | 124   | 2018-04-20T10:23:08 -> 2023-06-20T10:13:28 | 2018-04-20 10:36:59, 2018-04-20 11:00:10, 2018-04-20 10:54:37, 2018-04-20 11:01:17, 2022-08-07 17:03:17 |
| active              | 100.0% | 2     | 0.0 -> 1.0                                 | 1, 0                                                                                                    |
| notification_type   | 100.0% | 1     | 2.0 -> 2.0                                 | 2                                                                                                       |
| folder_id           | 0.0%   | 0     |                                            |                                                                                                         |
| archived            | 100.0% | 1     | 0.0 -> 0.0                                 | 0                                                                                                       |
| notification_offset | 100.0% | 1     | 1440.0 -> 1440.0                           | 1440                                                                                                    |
| user_id             | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |
| updated_at          | 100.0% | 124   | 2018-04-20T10:23:08 -> 2023-06-20T10:13:28 | 2018-04-20 10:36:59, 2018-04-20 11:00:10, 2018-04-20 10:54:37, 2018-04-20 11:01:17, 2022-08-07 17:03:17 |
| diffusion           | 100.0% | 1     |                                            | original                                                                                                |

### followed_tv_show_source.csv

- Tipo ipotizzato: `series`
- Righe: `72`
- Colonne: `6`

| Colonna      | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| ------------ | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| tv_show_id   | 100.0% | 72    | 71119.0 -> 426779.0                        | 71119, 72227, 75760, 78258, 79168                                                                       |
| source       | 100.0% | 3     |                                            | see-season, see-episode, onboarding                                                                     |
| created_at   | 100.0% | 67    | 2018-04-20T10:23:08 -> 2023-06-20T10:13:28 | 2018-04-20 10:36:59, 2022-08-07 17:03:17, 2018-10-31 11:49:14, 2018-04-20 10:37:07, 2018-04-20 10:28:21 |
| updated_at   | 100.0% | 67    | 2018-04-20T10:23:08 -> 2023-06-20T10:13:28 | 2018-04-20 10:36:59, 2022-08-07 17:03:17, 2018-10-31 11:49:14, 2018-04-20 10:37:07, 2018-04-20 10:28:21 |
| tv_show_name | 100.0% | 72    |                                            | Lizzie McGuire, Two and a Half Men, How I Met Your Mother, That's So Raven, Friends                     |
| user_id      | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |

### friend.csv

- Tipo ipotizzato: `people/social`
- Righe: `25`
- Colonne: `5`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| ---------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |
| friend_id  | 100.0% | 25    | 5425228.0 -> 52038137.0                    | 5425228, 6303294, 6577033, 8846683, 9911141                                                             |
| created_at | 100.0% | 13    | 2018-04-20T10:20:41 -> 2021-08-15T17:17:44 | 2018-04-20 10:20:41, 2018-04-23 19:08:12, 2018-04-20 11:00:19, 2018-04-20 12:10:35, 2018-08-24 15:35:42 |
| updated_at | 100.0% | 13    | 2018-04-20T10:20:41 -> 2021-08-15T17:17:44 | 2018-04-20 10:20:41, 2018-04-23 19:08:12, 2018-04-20 11:00:19, 2018-04-20 12:10:35, 2018-08-24 15:35:42 |
| affinity   | 100.0% | 1     | 100.0 -> 100.0                             | 100                                                                                                     |

### gdpr_requests.csv

- Tipo ipotizzato: `comments`
- Righe: `1`
- Colonne: `9`

| Colonna        | Piena  | Unici | Range                                      | Esempi              |
| -------------- | ------ | ----- | ------------------------------------------ | ------------------- |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |
| created_at     | 100.0% | 1     | 2026-07-06T13:32:30 -> 2026-07-06T13:32:30 | 2026-07-06 13:32:30 |
| data_generated | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| s3_key         | 0.0%   | 0     |                                            |                     |
| id             | 100.0% | 1     | 197640.0 -> 197640.0                       | 197640              |
| source         | 100.0% | 1     |                                            | self_service        |
| updated_at     | 100.0% | 1     | 2026-07-06T13:34:37 -> 2026-07-06T13:34:37 | 2026-07-06 13:34:37 |
| locked         | 100.0% | 1     | 1.0 -> 1.0                                 | 1                   |
| error_message  | 0.0%   | 0     |                                            |                     |

### install_tracking.csv

- Tipo ipotizzato: `people/social`
- Righe: `3`
- Colonne: `7`

| Colonna    | Piena  | Unici | Range                                      | Esempi                            |
| ---------- | ------ | ----- | ------------------------------------------ | --------------------------------- |
| created_at | 100.0% | 1     | 2018-04-20T10:21:10 -> 2018-04-20T10:21:10 | 2018-04-20 10:21:10               |
| updated_at | 100.0% | 1     | 2018-04-20T10:21:10 -> 2018-04-20T10:21:10 | 2018-04-20 10:21:10               |
| id         | 100.0% | 3     | 43092561.0 -> 43092563.0                   | 43092561, 43092562, 43092563      |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                          |
| source     | 100.0% | 1     |                                            | AppsFlyer                         |
| name       | 100.0% | 3     |                                            | is_organic, af_status, af_message |
| value      | 100.0% | 3     |                                            | 1, Organic, organic install       |

### installed_app.csv

- Tipo ipotizzato: `people/social`
- Righe: `6`
- Colonne: `6`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                        |
| ---------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------- |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                      |
| device_id  | 100.0% | 1     |                                            | [redacted]                                                    |
| app_id     | 100.0% | 6     |                                            | fb, instagram, nflx, snapchat, twitter                        |
| removed    | 100.0% | 1     | 1.0 -> 1.0                                 | 1                                                             |
| created_at | 100.0% | 3     | 2018-04-20T10:20:22 -> 2018-11-09T15:14:03 | 2018-04-20 10:20:22, 2018-11-09 15:14:03, 2018-10-31 11:46:23 |
| updated_at | 100.0% | 2     | 2019-12-17T17:56:11 -> 2020-03-18T09:08:34 | 2019-12-17 17:56:11, 2020-03-18 09:08:34                      |

### ip_address.csv

- Tipo ipotizzato: `people/social`
- Righe: `59`
- Colonne: `13`

| Colonna      | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| ------------ | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| region_name  | 10.17% | 3     |                                            | Veneto, Emilia-Romagna, Friuli Venezia Giulia                                                           |
| hits         | 100.0% | 7     | 1.0 -> 22.0                                | 5, 2, 1, 22, 3                                                                                          |
| created_at   | 100.0% | 59    | 2018-04-20T10:20:22 -> 2026-07-06T13:27:56 | 2022-12-17 13:15:34, 2023-05-31 09:01:21, 2018-05-24 11:40:00, 2018-06-07 11:55:57, 2018-04-20 10:20:22 |
| ip_address   | 100.0% | 59    |                                            | [redacted]                                                                                              |
| longitude    | 10.17% | 3     | 11.34 -> 13.77                             | 11.54, 11.34, 13.77                                                                                     |
| timezone     | 10.17% | 2     |                                            | +01:00, +02:00                                                                                          |
| user_id      | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |
| country_name | 10.17% | 1     |                                            | Italy                                                                                                   |
| zip_code     | 10.17% | 6     | 34148.0 -> 40141.0                         | [redacted]                                                                                              |
| latitude     | 10.17% | 3     | 44.49 -> 45.65                             | 45.54, 44.49, 45.65                                                                                     |
| updated_at   | 100.0% | 59    | 2018-04-20T12:24:34 -> 2026-07-06T13:29:11 | 2022-12-17 13:38:46, 2023-05-31 09:15:17, 2018-05-24 11:40:00, 2018-06-26 07:58:59, 2018-04-24 07:45:06 |
| country_code | 10.17% | 1     |                                            | IT                                                                                                      |
| city_name    | 10.17% | 3     |                                            | Vicenza, Bologna, Trieste                                                                               |

### lists-prod-lists.csv

- Tipo ipotizzato: `episodes`
- Righe: `2`
- Colonne: `15`

| Colonna        | Piena  | Unici | Range                                      | Esempi                                                       |
| -------------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------ |
| s_key          | 100.0% | 2     |                                            | collection, favorite-movies                                  |
| lists          | 50.0%  | 1     |                                            | [map[created_at:1.621288901e+09 description:<nil> fanart:<ni |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                     |
| created_at     | 50.0%  | 1     | 2020-01-23T22:02:50 -> 2020-01-23T22:02:50 | 2020-01-23 22:02:50                                          |
| description    | 0.0%   | 0     |                                            |                                                              |
| name           | 50.0%  | 1     |                                            | Favorite Movies                                              |
| ordering       | 50.0%  | 1     | 1.0 -> 1.0                                 | 1                                                            |
| type           | 50.0%  | 1     |                                            | list                                                         |
| updated_at     | 50.0%  | 1     | 2020-01-23T22:02:50 -> 2020-01-23T22:02:50 | 2020-01-23 22:02:50                                          |
| is_public      | 50.0%  | 1     |                                            | true                                                         |
| objects        | 50.0%  | 1     |                                            | [map[created_at:1.579816992e+09 filter:<nil> id:0 meta:<nil> |
| movie_name     | 0.0%   | 0     |                                            |                                                              |
| series_name    | 0.0%   | 0     |                                            |                                                              |
| season_number  | 0.0%   | 0     |                                            |                                                              |
| episode_number | 0.0%   | 0     |                                            |                                                              |

### ratings-3-prod-episode_votes.csv

- Tipo ipotizzato: `episodes`
- Righe: `4`
- Colonne: `7`

| Colonna        | Piena  | Unici | Range                    | Esempi                                                                             |
| -------------- | ------ | ----- | ------------------------ | ---------------------------------------------------------------------------------- |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0 | 20319846                                                                           |
| episode_id     | 100.0% | 4     | 5648788.0 -> 7059062.0   | 5648788, 5801751, 6927356, 7059062                                                 |
| vote_key       | 100.0% | 4     |                          | 5648788-20319846-29, 5801751-20319846-27, 6927356-20319846-29, 7059062-20319846-29 |
| movie_name     | 0.0%   | 0     |                          |                                                                                    |
| series_name    | 100.0% | 4     |                          | The Good Place, Once Upon a Time (2011), Sex Education, Euphoria (US)              |
| season_number  | 100.0% | 2     | 1.0 -> 6.0               | 1, 6                                                                               |
| episode_number | 100.0% | 2     | 1.0 -> 11.0              | 1, 11                                                                              |

### ratings-live-votes.csv

- Tipo ipotizzato: `episodes`
- Righe: `312`
- Colonne: `8`

| Colonna        | Piena  | Unici | Range                    | Esempi                                                                                                                                                                                                                                                 |
| -------------- | ------ | ----- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| vote_key       | 100.0% | 312   |                          | 69eac434-2b1f-48af-ab17-f4d89e0e254d-20319846-27, 7e43368d-eb1c-4e03-8ecf-86c598245419-20319846-3, f8bdc653-9ab8-4fa5-a02c-5623f5166485-20319846-28, 95f78654-bf49-4a1e-ba96-87fe62a9ae38-20319846-1, b76dd8fe-8dfd-4a6a-b296-402dc39f077a-20319846-29 |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0 | 20319846                                                                                                                                                                                                                                               |
| episode_id     | 100.0% | 1     | 0.0 -> 0.0               | 0                                                                                                                                                                                                                                                      |
| uuid           | 100.0% | 312   |                          | 69eac434-2b1f-48af-ab17-f4d89e0e254d, 7e43368d-eb1c-4e03-8ecf-86c598245419, f8bdc653-9ab8-4fa5-a02c-5623f5166485, 95f78654-bf49-4a1e-ba96-87fe62a9ae38, b76dd8fe-8dfd-4a6a-b296-402dc39f077a                                                           |
| movie_name     | 100.0% | 310   |                          | Her, The Imitation Game, The Hunger Games: Catching Fire, Midnight Sun, Captain America: Civil War                                                                                                                                                     |
| series_name    | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                        |
| season_number  | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                        |
| episode_number | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                        |

### ratings-v2-prod-votes.csv

- Tipo ipotizzato: `episodes`
- Righe: `16`
- Colonne: `8`

| Colonna        | Piena  | Unici | Range                    | Esempi                                                                                                                                                                                                                                                  |
| -------------- | ------ | ----- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| episode_id     | 100.0% | 1     | 0.0 -> 0.0               | 0                                                                                                                                                                                                                                                       |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0 | 20319846                                                                                                                                                                                                                                                |
| uuid           | 100.0% | 16    |                          | 8b9f98b4-5ad6-4aed-b2d5-82f478dcd822, 6ac9f995-6070-4f2d-add9-5cee9b0de835, af8c08be-80bf-430e-8122-5a588fdbb8bd, f13d0f33-5d14-4e74-8dc0-a58d00e0433b, f00f5dda-cebe-496e-b43b-3dbcb2953dee                                                            |
| vote_key       | 100.0% | 16    |                          | 8b9f98b4-5ad6-4aed-b2d5-82f478dcd822-20319846-29, 6ac9f995-6070-4f2d-add9-5cee9b0de835-20319846-29, af8c08be-80bf-430e-8122-5a588fdbb8bd-20319846-3, f13d0f33-5d14-4e74-8dc0-a58d00e0433b-20319846-28, f00f5dda-cebe-496e-b43b-3dbcb2953dee-20319846-29 |
| movie_name     | 100.0% | 16    |                          | Pirates of the Caribbean: Dead Man's Chest, Midnight in Paris, The Golden Compass, Grown Ups, Harry Potter and the Deathly Hallows: Part 1                                                                                                              |
| series_name    | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                         |
| season_number  | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                         |
| episode_number | 0.0%   | 0     |                          |                                                                                                                                                                                                                                                         |

### recommendations-prod-user-scores.csv

- Tipo ipotizzato: `episodes`
- Righe: `1`
- Colonne: `8`

| Colonna        | Piena  | Unici | Range                    | Esempi                                                       |
| -------------- | ------ | ----- | ------------------------ | ------------------------------------------------------------ |
| user_variance  | 100.0% | 1     | 6.616393 -> 6.616393     | 6.616393                                                     |
| tv_shows       | 100.0% | 1     |                          | [map[id:79316 percentile:99 score:4.961776 user_mean:-6.0967 |
| user_mean      | 100.0% | 1     | -6.096744 -> -6.096744   | -6.096744                                                    |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0 | 20319846                                                     |
| movie_name     | 0.0%   | 0     |                          |                                                              |
| series_name    | 0.0%   | 0     |                          |                                                              |
| season_number  | 0.0%   | 0     |                          |                                                              |
| episode_number | 0.0%   | 0     |                          |                                                              |

### recommendations-prod-user-shows.csv

- Tipo ipotizzato: `episodes`
- Righe: `1`
- Colonne: `6`

| Colonna          | Piena  | Unici | Range                    | Esempi                                                       |
| ---------------- | ------ | ----- | ------------------------ | ------------------------------------------------------------ |
| watched_show_ids | 100.0% | 1     |                          | [346328 82493 302218 367146 74189 252312 362392 80925 249882 |
| user_id          | 100.0% | 1     | 20319846.0 -> 20319846.0 | 20319846                                                     |
| movie_name       | 0.0%   | 0     |                          |                                                              |
| series_name      | 0.0%   | 0     |                          |                                                              |
| season_number    | 0.0%   | 0     |                          |                                                              |
| episode_number   | 0.0%   | 0     |                          |                                                              |

### referral.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `9`

| Colonna     | Piena  | Unici | Range                                      | Esempi               |
| ----------- | ------ | ----- | ------------------------------------------ | -------------------- |
| consumed    | 100.0% | 1     | 1.0 -> 1.0                                 | 1                    |
| created_at  | 100.0% | 1     | 2018-04-20T12:09:50 -> 2018-04-20T12:09:50 | 2018-04-20 12:09:50  |
| user_id     | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846             |
| referree_id | 100.0% | 1     | 2032-10-04T00:00:00 -> 2032-10-04T00:00:00 | 20321004             |
| days        | 0.0%   | 0     |                                            |                      |
| state       | 100.0% | 1     |                                            | completed-onboarding |
| updated_at  | 100.0% | 1     | 2018-04-20T12:13:49 -> 2018-04-20T12:13:49 | 2018-04-20 12:13:49  |
| credited    | 100.0% | 1     | 1.0 -> 1.0                                 | 1                    |
| credits     | 100.0% | 1     | 1.0 -> 1.0                                 | 1                    |

### refresh_token.csv

- Tipo ipotizzato: `people/social`
- Righe: `2`
- Colonne: `6`

| Colonna     | Piena  | Unici | Range                                      | Esempi                                   |
| ----------- | ------ | ----- | ------------------------------------------ | ---------------------------------------- |
| user_id     | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                 |
| device_id   | 50.0%  | 1     |                                            | [redacted]                               |
| token       | 100.0% | 2     |                                            | [redacted]                               |
| blacklisted | 100.0% | 1     | 0.0 -> 0.0                                 | 0                                        |
| created_at  | 100.0% | 2     | 2019-10-07T19:06:21 -> 2021-12-20T12:09:20 | 2021-12-20 12:09:20, 2019-10-07 19:06:21 |
| updated_at  | 100.0% | 2     | 2019-10-07T19:06:21 -> 2021-12-20T12:09:20 | 2021-12-20 12:09:20, 2019-10-07 19:06:21 |

### rewatched_episode.csv

- Tipo ipotizzato: `episodes`
- Righe: `121`
- Colonne: `8`

| Colonna               | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| --------------------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| episode_id            | 100.0% | 121   | 335761.0 -> 4398279.0                      | 335761, 335762, 335763, 338039, 338040                                                                  |
| cpt                   | 100.0% | 1     | 1.0 -> 1.0                                 | 1                                                                                                       |
| created_at            | 100.0% | 6     | 2019-11-09T15:35:27 -> 2019-11-09T15:35:43 | 2019-11-09 15:35:27, 2019-11-09 15:35:31, 2019-11-09 15:35:35, 2019-11-09 15:35:38, 2019-11-09 15:35:40 |
| updated_at            | 100.0% | 6     | 2019-11-09T15:35:27 -> 2019-11-09T15:35:43 | 2019-11-09 15:35:27, 2019-11-09 15:35:31, 2019-11-09 15:35:35, 2019-11-09 15:35:38, 2019-11-09 15:35:40 |
| tv_show_name          | 100.0% | 1     |                                            | Gossip Girl                                                                                             |
| episode_season_number | 100.0% | 6     | 1.0 -> 6.0                                 | 1, 2, 3, 4, 5                                                                                           |
| episode_number        | 100.0% | 25    | 1.0 -> 25.0                                | 1, 2, 3, 4, 5                                                                                           |
| user_id               | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |

### seen_episode_source.csv

- Tipo ipotizzato: `episodes`
- Righe: `132`
- Colonne: `8`

| Colonna               | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| --------------------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| created_at            | 100.0% | 89    | 2018-04-20T10:25:52 -> 2018-10-31T11:49:16 | 2018-04-20 13:54:32, 2018-04-20 10:57:21, 2018-04-20 10:57:22, 2018-04-20 10:57:23, 2018-04-20 10:57:24 |
| updated_at            | 100.0% | 89    | 2018-04-20T10:25:52 -> 2018-10-31T11:49:16 | 2018-04-20 13:54:32, 2018-04-20 10:57:21, 2018-04-20 10:57:22, 2018-04-20 10:57:23, 2018-04-20 10:57:24 |
| tv_show_name          | 100.0% | 19    |                                            | Code Lyoko, Tokyo Mew Mew, How I Met Your Mother, Scrubs, Friends                                       |
| episode_season_number | 100.0% | 7     | 1.0 -> 9.0                                 | 1, 5, 8, 9, 4                                                                                           |
| episode_number        | 100.0% | 22    | 1.0 -> 22.0                                | 1, 2, 3, 4, 5                                                                                           |
| user_id               | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |
| episode_id            | 100.0% | 132   | 142447.0 -> 6674474.0                      | 142447, 149645, 149646, 149647, 149648                                                                  |
| source                | 100.0% | 2     |                                            | season-detail, episode-detail                                                                           |

### show_addiction_score.csv

- Tipo ipotizzato: `series`
- Righe: `46`
- Colonne: `7`

| Colonna               | Piena  | Unici | Range                        | Esempi                                                                    |
| --------------------- | ------ | ----- | ---------------------------- | ------------------------------------------------------------------------- |
| daily_score           | 100.0% | 3     | 35.0 -> 100.0                | 35, 100, 70                                                               |
| weekly_score          | 100.0% | 3     | 35.0 -> 100.0                | 35, 100, 70                                                               |
| monthly_score         | 100.0% | 3     | 35.0 -> 100.0                | 35, 100, 70                                                               |
| tv_show_name          | 100.0% | 46    |                              | Two and a Half Men, The Office (US), Winx Club, Code Lyoko, Tokyo Mew Mew |
| user_id               | 100.0% | 1     | 20319846.0 -> 20319846.0     | 20319846                                                                  |
| tv_show_id            | 100.0% | 46    | 72227.0 -> 443312.0          | 72227, 73244, 74256, 74280, 74598                                         |
| last_action_timestamp | 100.0% | 46    | 1524220284.0 -> 1781309367.0 | 1659891812, 1746984731, 1524221042, 1524232472, 1524555911                |

### show_seen_episode_latest.csv

- Tipo ipotizzato: `episodes`
- Righe: `46`
- Colonne: `6`

| Colonna      | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| ------------ | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| tv_show_id   | 100.0% | 46    | 72227.0 -> 443312.0                        | 72227, 73244, 74256, 74280, 74598                                                                       |
| episode_id   | 100.0% | 46    | 78322.0 -> 11267772.0                      | 78322, 110417, 1265571, 142447, 149666                                                                  |
| created_at   | 100.0% | 46    | 2018-04-20T10:31:23 -> 2026-03-10T09:58:01 | 2022-08-07 17:03:31, 2025-05-11 17:32:11, 2018-04-20 10:44:06, 2018-04-20 13:54:32, 2018-04-24 07:45:11 |
| updated_at   | 100.0% | 46    | 2018-04-20T10:31:23 -> 2026-06-13T00:09:27 | 2022-08-07 17:03:31, 2025-05-11 17:32:11, 2018-04-20 10:44:06, 2018-04-20 13:54:32, 2018-04-24 07:45:11 |
| tv_show_name | 100.0% | 46    |                                            | Two and a Half Men, The Office (US), Winx Club, Code Lyoko, Tokyo Mew Mew                               |
| user_id      | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |

### stats-prod-cache.csv

- Tipo ipotizzato: `episodes`
- Righe: `2`
- Colonne: `12`

| Colonna          | Piena  | Unici | Range                        | Esempi                                                                                                                     |
| ---------------- | ------ | ----- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| stats            | 100.0% | 2     |                              | map[biggest-marathon:[map[highlight:false x:Mercoledì y:[1 0, map[count-by-month:[map[highlight:false x:2025-8 y:0] map[hi |
| version          | 100.0% | 1     | 1.0 -> 1.0                   | 1                                                                                                                          |
| user_id          | 100.0% | 1     | 20319846.0 -> 20319846.0     | 20319846                                                                                                                   |
| entity_type      | 100.0% | 2     |                              | episode, movie                                                                                                             |
| timestamp        | 100.0% | 1     | 1783344559.0 -> 1783344559.0 | 1783344559                                                                                                                 |
| stat_type        | 100.0% | 1     |                              | watched                                                                                                                    |
| type             | 100.0% | 2     |                              | episode-watched, movie-watched                                                                                             |
| interaction_type | 0.0%   | 0     |                              |                                                                                                                            |
| movie_name       | 0.0%   | 0     |                              |                                                                                                                            |
| series_name      | 0.0%   | 0     |                              |                                                                                                                            |
| season_number    | 0.0%   | 0     |                              |                                                                                                                            |
| episode_number   | 0.0%   | 0     |                              |                                                                                                                            |

### tracking-deployment-prod-tracks.csv

- Tipo ipotizzato: `episodes`
- Righe: `1`
- Colonne: `7`

| Colonna        | Piena  | Unici | Range                                      | Esempi              |
| -------------- | ------ | ----- | ------------------------------------------ | ------------------- |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |
| created_at     | 100.0% | 1     | 2023-09-04T00:48:32 -> 2023-09-04T00:48:32 | 2023-09-04 00:48:32 |
| day            | 100.0% | 1     |                                            | new                 |
| movie_name     | 0.0%   | 0     |                                            |                     |
| series_name    | 0.0%   | 0     |                                            |                     |
| season_number  | 0.0%   | 0     |                                            |                     |
| episode_number | 0.0%   | 0     |                                            |                     |

### tracking-prod-count-by-timeframe.csv

- Tipo ipotizzato: `episodes`
- Righe: `2`
- Colonne: `9`

| Colonna        | Piena  | Unici | Range                        | Esempi                      |
| -------------- | ------ | ----- | ---------------------------- | --------------------------- |
| count          | 100.0% | 1     | 75.0 -> 75.0                 | 75                          |
| expires_at     | 100.0% | 1     | 1763854937.0 -> 1763854937.0 | 1763854937                  |
| runtime        | 100.0% | 1     | 177840.0 -> 177840.0         | 177840                      |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0     | 20319846                    |
| type           | 100.0% | 2     |                              | month-2024-11, week-2024-47 |
| movie_name     | 0.0%   | 0     |                              |                             |
| series_name    | 0.0%   | 0     |                              |                             |
| season_number  | 0.0%   | 0     |                              |                             |
| episode_number | 0.0%   | 0     |                              |                             |

### tracking-prod-records-v2.csv

- Tipo ipotizzato: `episodes`
- Righe: `6197`
- Colonne: `29`

| Colonna                | Piena  | Unici | Range                                      | Esempi                                                                                                                                                                                                                                                                                                               |
| ---------------------- | ------ | ----- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| key                    | 100.0% | 6197  |                                            | [redacted-long-token], tracking-stats, user-series-043c7cb1-73e9-4642-8ba1-ae48d024c4a6, user-series-07ba252b-8193-4fdd-8e7b-334d35a2d8e4, user-series-085b1e9e-f1cd-4b45-84ed-9d3895608bf0                                                                                                                          |
| user_id                | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                                                                                                                                                                                                                             |
| created_at             | 100.0% | 660   | 2018-04-20T10:23:08 -> 2026-06-10T19:57:41 | 2019-11-09 15:35:43, 2019-11-09 15:35:40, 2019-11-09 15:35:31, 2019-11-09 15:35:38, 2019-11-09 15:35:27                                                                                                                                                                                                              |
| s_id                   | 99.98% | 137   | 71119.0 -> 443312.0                        | 80547, 76156, 378746, 80726, 412493                                                                                                                                                                                                                                                                                  |
| ep_id                  | 97.77% | 5938  | 34776.0 -> 11560129.0                      | 4332242, 4218072, 388835, 2724271, 400267                                                                                                                                                                                                                                                                            |
| gsi                    | 8.44%  | 314   |                                            | watch-episode-1573313743, watch-episode-1573313740, watch-episode-1573313731, watch-episode-1573313738, watch-episode-1573313727                                                                                                                                                                                     |
| movie_watch_count      | 0.02%  | 1     | 307.0 -> 307.0                             | 307                                                                                                                                                                                                                                                                                                                  |
| updated_at             | 98.05% | 655   | 2018-04-20T10:23:08 -> 2026-06-10T19:57:41 | 2026-06-10 19:57:41, 2018-04-20 10:33:11, 2023-06-20 10:11:25, 2022-12-17 13:32:47, 2023-05-31 08:49:04                                                                                                                                                                                                              |
| ep_watch_count         | 1.97%  | 66    | 0.0 -> 5938.0                              | 5938, 8, 40, 107, 15                                                                                                                                                                                                                                                                                                 |
| total_series_runtime   | 0.02%  | 1     | 10894920.0 -> 10894920.0                   | 10894920                                                                                                                                                                                                                                                                                                             |
| total_movies_runtime   | 0.02%  | 1     | 2184720.0 -> 2184720.0                     | 2184720                                                                                                                                                                                                                                                                                                              |
| series_follow_count    | 0.02%  | 1     | 133.0 -> 133.0                             | 133                                                                                                                                                                                                                                                                                                                  |
| is_followed            | 2.21%  | 2     |                                            | false, true                                                                                                                                                                                                                                                                                                          |
| is_archived            | 2.21%  | 1     |                                            | false                                                                                                                                                                                                                                                                                                                |
| is_for_later           | 2.21%  | 1     |                                            | false                                                                                                                                                                                                                                                                                                                |
| most_recent_ep_watched | 1.92%  | 119   |                                            | map[ep_id:184609 ep_no:8 s_no:1 uuid:c52f22a2-0f90-4c4f-b3d5, map[ep_id:9.734301e+06 ep_no:10 s_no:4 uuid:0a5132eb-f1f1-40, map[ep_id:7.659644e+06 ep_no:28 s_no:4 uuid:702dcf55-91b5-4d, map[ep_id:9.735967e+06 ep_no:7 s_no:2 uuid:4a95c9d7-3760-41a, map[ep_id:441797 ep_no:13 s_no:2 uuid:c3cf051f-80b7-4122-9f9 |
| uuid                   | 2.21%  | 137   |                                            | 043c7cb1-73e9-4642-8ba1-ae48d024c4a6, 07ba252b-8193-4fdd-8e7b-334d35a2d8e4, 085b1e9e-f1cd-4b45-84ed-9d3895608bf0, 097ac527-de03-4b74-b2f0-8a4a83c00afb, 0b0b2628-c873-45ad-81ad-2018a4aa54a7                                                                                                                         |
| followed_at            | 0.61%  | 38    | 1642600032372243.0 -> 1773136681052769.0   | 1685522942350045, 1642600061008605, 1671283166229463, 1674311593134368, 1659891760873209                                                                                                                                                                                                                             |
| s_no                   | 95.82% | 21    | 0.0 -> 20.0                                | 1, 3, 4, 2, 0                                                                                                                                                                                                                                                                                                        |
| rewatch_count          | 72.21% | 2     | 0.0 -> 1.0                                 | 0, 1                                                                                                                                                                                                                                                                                                                 |
| ep_no                  | 95.82% | 140   | 0.0 -> 139.0                               | 6, 7, 5, 4, 8                                                                                                                                                                                                                                                                                                        |
| is_unitary             | 95.69% | 2     |                                            | true, false                                                                                                                                                                                                                                                                                                          |
| bulk_type              | 21.69% | 2     |                                            | season, fill-previous                                                                                                                                                                                                                                                                                                |
| runtime                | 23.61% | 35    | 0.0 -> 4260.0                              | 1680, 1740, 1560, 1920, 0                                                                                                                                                                                                                                                                                            |
| is_special             | 0.05%  | 1     |                                            | true                                                                                                                                                                                                                                                                                                                 |
| movie_name             | 0.0%   | 0     |                                            |                                                                                                                                                                                                                                                                                                                      |
| series_name            | 99.98% | 137   |                                            | Gossip Girl, Scrubs, Never Have I Ever, Wizards of Waverly Place, The Ferragnez                                                                                                                                                                                                                                      |
| season_number          | 97.77% | 21    | 0.0 -> 20.0                                | 6, 5, 2, 4, 1                                                                                                                                                                                                                                                                                                        |
| episode_number         | 97.77% | 140   | 0.0 -> 139.0                               | 3, 11, 8, 7, 9                                                                                                                                                                                                                                                                                                       |

### tracking-prod-records.csv

- Tipo ipotizzato: `episodes`
- Righe: `985`
- Colonne: `30`

| Colonna                   | Piena  | Unici | Range                                      | Esempi                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ------ | ----- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| series_id                 | 36.55% | 8     | 80725.0 -> 378746.0                        | 378746, 356317, 248835, 80725, 311711                                                                                                                                                                                                                                                                                |
| user_id                   | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                                                                                                                                                                                                                             |
| uuid                      | 99.7%  | 733   |                                            | 07ba252b-8193-4fdd-8e7b-334d35a2d8e4, 2ca857f5-aa12-4c60-8f01-3615da41dc09, 427f6a44-13e7-454b-8b19-50528691cb1b, 6b0bb9e1-b277-4a0a-8f34-3b601c4c35eb, b10ec69c-0988-4e2a-8097-beba7cf0bde0                                                                                                                         |
| updated_at                | 99.9%  | 467   | 2019-11-09T14:49:10 -> 2024-01-10T00:41:41 | 2021-10-17 17:30:17, 2021-10-17 17:28:43, 2021-07-22 10:33:38, 2021-10-17 17:29:07, 2021-07-22 10:32:36                                                                                                                                                                                                              |
| type-uuid-n               | 100.0% | 985   |                                            | count-watch-episode-series-07ba252b-8193-4fdd-8e7b-334d35a2d, count-watch-episode-series-2ca857f5-aa12-4c60-8f01-3615da41d, count-watch-episode-series-427f6a44-13e7-454b-8b19-50528691c, count-watch-episode-series-6b0bb9e1-b277-4a0a-8f34-3b601c4c3, count-watch-episode-series-b10ec69c-0988-4e2a-8097-beba7cf0b |
| watch_count               | 1.02%  | 9     | 8.0 -> 344.0                               | 11, 8, 44, 216, 13                                                                                                                                                                                                                                                                                                   |
| created_at                | 99.9%  | 468   | 2019-11-09T14:49:10 -> 2024-01-10T00:41:41 | 2021-10-17 17:30:15, 2021-10-17 17:28:26, 2021-07-22 10:33:13, 2021-07-22 13:05:54, 2021-07-22 10:32:36                                                                                                                                                                                                              |
| type                      | 99.9%  | 8     |                                            | count-watch-episode-series, count-watch-episode-total, follow, last-episode-watched, rewatch_count                                                                                                                                                                                                                   |
| watches                   | 0.1%   | 1     |                                            | [78a0d677-5e7e-423d-a0ab-b669754885f1 08c1f0a2-581f-476c-bbd                                                                                                                                                                                                                                                         |
| release_date              | 63.15% | 272   | 0001-01-01T00:00:00 -> 2023-12-14T00:00:00 | 2021-11-26 00:00:00, 2023-07-20 00:00:00, 1993-12-15 00:00:00, 2021-10-25 00:00:00, 2019-05-22 00:00:00                                                                                                                                                                                                              |
| release_date_range_key    | 18.98% | 182   |                                            | follow-release-date-2021-11-26, follow-release-date-2023-07-20, follow-release-date-2021-10-25, follow-release-date-2022-07-08, follow-release-date-2021-12-23                                                                                                                                                       |
| alpha_range_key           | 18.98% | 187   |                                            | follow-alpha-encanto, follow-alpha-barbie, follow-alpha-time-is-up, follow-alpha-thor-love-and-thunder, follow-alpha-sing-2                                                                                                                                                                                          |
| entity_type               | 98.88% | 2     |                                            | movie, episode                                                                                                                                                                                                                                                                                                       |
| follow_date_range_key     | 31.57% | 257   |                                            | follow-follow-date-1642600357, follow-follow-date-1704847110, follow-follow-date-1573311962, follow-follow-date-1674312124, follow-follow-date-1573311559                                                                                                                                                            |
| runtime                   | 48.22% | 59    | 900.0 -> 11520.0                           | 6180, 6840, 6480, 6600, 4800                                                                                                                                                                                                                                                                                         |
| rewatch_count             | 49.95% | 1     | 0.0 -> 0.0                                 | 0                                                                                                                                                                                                                                                                                                                    |
| series_uuid               | 35.74% | 8     |                                            | 07ba252b-8193-4fdd-8e7b-334d35a2d8e4, 2ca857f5-aa12-4c60-8f01-3615da41dc09, 427f6a44-13e7-454b-8b19-50528691cb1b, 6b0bb9e1-b277-4a0a-8f34-3b601c4c35eb, b10ec69c-0988-4e2a-8097-beba7cf0bde0                                                                                                                         |
| watch_date                | 4.77%  | 35    | 1626949912.0 -> 1634491817.0               | 1634491817, 1634491723, 1626950018, 1634491747, 1626949956                                                                                                                                                                                                                                                           |
| season_number             | 35.74% | 15    | 1.0 -> 15.0                                | 2, 3, 7, 15, 4                                                                                                                                                                                                                                                                                                       |
| episode_number            | 35.74% | 22    | 1.0 -> 22.0                                | 1, 8, 22, 2, 13                                                                                                                                                                                                                                                                                                      |
| episode_id                | 35.74% | 344   | 366998.0 -> 8507469.0                      | 8483111, 8507469, 6600220, 6751264, 7468772                                                                                                                                                                                                                                                                          |
| total_movies_runtime      | 0.1%   | 1     | 2199180.0 -> 2199180.0                     | 2199180                                                                                                                                                                                                                                                                                                              |
| total_series_runtime      | 0.1%   | 1     | 7813620.0 -> 7813620.0                     | 7813620                                                                                                                                                                                                                                                                                                              |
| unitarian                 | 34.92% | 2     |                                            | false, true                                                                                                                                                                                                                                                                                                          |
| country                   | 41.32% | 2     |                                            | us, IT                                                                                                                                                                                                                                                                                                               |
| watch_date_range_key      | 41.32% | 114   |                                            | watch-date-1634491723, watch-date-1671284175, watch-date-1704847110, watch-date-1626959158, watch-date-1674312124                                                                                                                                                                                                    |
| bulk_type                 | 30.96% | 2     |                                            | season, fill-previous                                                                                                                                                                                                                                                                                                |
| watched_episode_range_key | 34.92% | 344   |                                            | [redacted-long-token]                                                                                                                                                                                                                                                                                                |
| movie_name                | 62.94% | 378   |                                            | Encanto, Barbie, Schindler's List, Time Is Up, Rocketman                                                                                                                                                                                                                                                             |
| series_name               | 36.55% | 8     |                                            | Never Have I Ever, Sex Education, Once Upon a Time (2011), Keeping Up with the Kardashians, The Good Place                                                                                                                                                                                                           |

### tv_show_user_emotion_count.csv

- Tipo ipotizzato: `series`
- Righe: `5`
- Colonne: `7`

| Colonna      | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| ------------ | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| emotion_id   | 100.0% | 3     | 1.0 -> 7.0                                 | 6, 7, 1                                                                                                 |
| count        | 100.0% | 4     | 0.0 -> 3.0                                 | 1, 0, 2, 3                                                                                              |
| created_at   | 100.0% | 5     | 2019-11-09T15:38:41 -> 2021-07-23T00:49:10 | 2021-07-23 00:49:01, 2021-07-23 00:49:10, 2019-11-22 21:47:58, 2019-11-09 15:38:41, 2020-01-27 12:26:39 |
| updated_at   | 100.0% | 5     | 2019-11-09T15:42:48 -> 2021-07-23T00:52:42 | 2021-07-23 00:49:01, 2021-07-23 00:52:42, 2019-11-22 21:48:31, 2019-11-09 15:42:48, 2020-01-27 12:26:39 |
| tv_show_name | 100.0% | 4     |                                            | Once Upon a Time (2011), The Good Place, Sex Education, Euphoria (US)                                   |
| tv_show_id   | 100.0% | 4     | 248835.0 -> 360261.0                       | 248835, 311711, 356317, 360261                                                                          |
| user_id      | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |

### user.csv

- Tipo ipotizzato: `series`
- Righe: `1`
- Colonne: `48`

| Colonna                     | Piena  | Unici | Range                                      | Esempi                        |
| --------------------------- | ------ | ----- | ------------------------------------------ | ----------------------------- |
| badge                       | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| device_token                | 0.0%   | 0     |                                            |                               |
| excluded_shows              | 0.0%   | 0     |                                            |                               |
| nb_weeks_active             | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| last_time_synced_drive      | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| name                        | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                      |
| posted_on_wall              | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| notif_webseries_new_video   | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| version_number              | 100.0% | 1     | 1804-10-05T00:00:00 -> 1804-10-05T00:00:00 | 18041005                      |
| fake_account                | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| fb_expiration_date          | 100.0% | 1     |                                            | 2018-06-19 00:00:00 +0000 UTC |
| newsletter_activated        | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| default_diffusion           | 0.0%   | 0     |                                            |                               |
| password_new                | 100.0% | 1     |                                            | [redacted]                    |
| automatic_account           | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| last_updated                | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| publish_on_twitter          | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| last_opened                 | 100.0% | 1     | 1783344551.0 -> 1783344551.0               | 1783344551                    |
| last_time_loaded_towatch    | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| tumblr_oauth_token          | 0.0%   | 0     |                                            |                               |
| default_notification_offset | 100.0% | 1     | 1440.0 -> 1440.0                           | 1440                          |
| public_profile              | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| language                    | 100.0% | 1     |                                            | en                            |
| backward_days               | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| publish_on_ticker           | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| twitter_connect_time        | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| notif_webseries_reco        | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| password                    | 0.0%   | 0     |                                            |                               |
| facebook_id                 | 100.0% | 1     | 1826457200982268.0 -> 1826457200982268.0   | [redacted]                    |
| mail                        | 100.0% | 1     |                                            | [redacted]                    |
| tumblr_id                   | 0.0%   | 0     |                                            |                               |
| id                          | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                      |
| excluded_networks           | 0.0%   | 0     |                                            |                               |
| notif_news                  | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| nb_months_active            | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| nb_days_active              | 100.0% | 1     | 0.0 -> 0.0                                 | 0                             |
| updated_at                  | 100.0% | 1     | 2026-07-06T13:29:11 -> 2026-07-06T13:29:11 | 2026-07-06 13:29:11           |
| fb_access_token             | 100.0% | 1     |                                            | [redacted]                    |
| fb_connect_time             | 100.0% | 1     | 1524219634.0 -> 1524219634.0               | 1524219634                    |
| timezone                    | 100.0% | 1     |                                            | Europe/Rome                   |
| mail_status                 | 100.0% | 1     | 1.0 -> 1.0                                 | [redacted]                    |
| hash                        | 0.0%   | 0     |                                            |                               |
| tumblr_oauth_token_secret   | 0.0%   | 0     |                                            |                               |
| created_at                  | 100.0% | 1     | 2018-04-20T10:20:22 -> 2018-04-20T10:20:22 | 2018-04-20 10:20:22           |
| twitter_id                  | 0.0%   | 0     |                                            |                               |
| twitter_oauth_token         | 0.0%   | 0     |                                            |                               |
| twitter_oauth_token_secret  | 0.0%   | 0     |                                            |                               |
| notif_friend_join           | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |

### user_badge.csv

- Tipo ipotizzato: `people/social`
- Righe: `3`
- Colonne: `4`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                        |
| ---------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------- |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                      |
| badge_id   | 100.0% | 3     |                                            | chose-emotion, used-mobile-version, viewed-profile            |
| created_at | 100.0% | 3     | 2018-04-20T10:20:35 -> 2019-11-09T15:38:42 | 2019-11-09 15:38:42, 2018-04-20 10:20:35, 2018-04-20 12:24:34 |
| updated_at | 100.0% | 3     | 2018-04-20T10:20:35 -> 2019-11-09T15:38:42 | 2019-11-09 15:38:42, 2018-04-20 10:20:35, 2018-04-20 12:24:34 |

### user_connection.csv

- Tipo ipotizzato: `people/social`
- Righe: `75`
- Colonne: `5`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                                                                                                                    |
| ---------- | ------ | ----- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                                                                  |
| date       | 100.0% | 75    |                                            | 2018-04-20 00:00:00 +0000 UTC, 2018-04-21 00:00:00 +0000 UTC, 2018-04-23 00:00:00 +0000 UTC, 2018-04-24 00:00:00 +0000 UTC, 2018-04-25 00:00:00 +0000 UTC |
| created_at | 100.0% | 75    | 2018-04-20T10:20:22 -> 2026-07-06T13:27:56 | 2018-04-20 10:20:22, 2018-04-21 08:26:29, 2018-04-23 13:57:25, 2018-04-24 07:45:06, 2018-04-25 07:51:22                                                   |
| updated_at | 100.0% | 75    | 2018-04-20T10:20:22 -> 2026-07-06T13:27:56 | 2018-04-20 10:20:22, 2018-04-21 08:26:29, 2018-04-23 13:57:25, 2018-04-24 07:45:06, 2018-04-25 07:51:22                                                   |
| source     | 74.67% | 1     |                                            | ios                                                                                                                                                       |

### user_device.csv

- Tipo ipotizzato: `people/social`
- Righe: `3`
- Colonne: `5`

| Colonna      | Piena  | Unici | Range                                      | Esempi                                                        |
| ------------ | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------- |
| user_id      | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                      |
| device_id    | 100.0% | 3     |                                            | [redacted]                                                    |
| version_code | 100.0% | 3     | 2025082201.0 -> 202205122587.0             | 20200228815, 2025082201, 202205122587                         |
| created_at   | 100.0% | 3     | 2018-04-20T10:23:18 -> 2023-07-14T15:33:06 | 2018-04-20 10:23:18, 2023-07-14 15:33:06, 2021-07-22 10:29:50 |
| updated_at   | 100.0% | 3     | 2020-03-18T09:08:33 -> 2025-10-21T11:19:40 | 2020-03-18 09:08:33, 2025-10-21 11:19:40, 2022-08-07 16:59:03 |

### user_facebook_data.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `10`

| Colonna     | Piena  | Unici | Range                                      | Esempi                        |
| ----------- | ------ | ----- | ------------------------------------------ | ----------------------------- |
| timezone    | 100.0% | 1     | 2.0 -> 2.0                                 | 2                             |
| facebook_id | 100.0% | 1     | 1826457200982268.0 -> 1826457200982268.0   | [redacted]                    |
| user_id     | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                      |
| name        | 100.0% | 1     |                                            | Chiara Callegari              |
| username    | 0.0%   | 0     |                                            |                               |
| gender      | 100.0% | 1     |                                            | female                        |
| created_at  | 100.0% | 1     | 2018-04-20T10:20:40 -> 2018-04-20T10:20:40 | 2018-04-20 10:20:40           |
| updated_at  | 100.0% | 1     | 2018-04-20T10:20:40 -> 2018-04-20T10:20:40 | 2018-04-20 10:20:40           |
| location    | 0.0%   | 0     |                                            |                               |
| birthday    | 100.0% | 1     |                                            | 0001-01-01 00:00:00 +0000 UTC |

### user_facebook_like.csv

- Tipo ipotizzato: `people/social`
- Righe: `181`
- Colonne: `6`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                                                                  |
| ---------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                |
| category   | 100.0% | 69    |                                            | Community, Government Organization, Company, TV Show, Dance & Night Club                                |
| name       | 100.0% | 181   |                                            | Maturità 2017 - Tocca a Me, MIUR Social, CHANEL, Winx Club, Aquarius Club @ Zrce beach                  |
| object_id  | 100.0% | 181   | 5845317146.0 -> 1878827992369285.0         | 1001254699921448, 100924280069563, 10109514234, 102291403210901, 102716746432780                        |
| created_at | 100.0% | 9     | 2018-04-20T10:20:35 -> 2018-08-29T12:19:59 | 2018-05-01 21:31:02, 2018-04-20 10:20:35, 2018-05-31 11:12:13, 2018-06-18 21:38:19, 2018-06-22 07:41:56 |
| updated_at | 100.0% | 9     | 2018-04-20T10:20:35 -> 2018-08-29T12:19:59 | 2018-05-01 21:31:02, 2018-04-20 10:20:35, 2018-05-31 11:12:13, 2018-06-18 21:38:19, 2018-06-22 07:41:56 |

### user_last_updated.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `4`

| Colonna      | Piena  | Unici | Range                                      | Esempi              |
| ------------ | ------ | ----- | ------------------------------------------ | ------------------- |
| user_id      | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |
| last_updated | 100.0% | 1     | 1783344737.0 -> 1783344737.0               | 1783344737          |
| created_at   | 100.0% | 1     | 2018-04-20T10:23:09 -> 2018-04-20T10:23:09 | 2018-04-20 10:23:09 |
| updated_at   | 100.0% | 1     | 2026-07-06T13:32:17 -> 2026-07-06T13:32:17 | 2026-07-06 13:32:17 |

### user_mail_sent_status.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `11`

| Colonna               | Piena  | Unici | Range                                      | Esempi              |
| --------------------- | ------ | ----- | ------------------------------------------ | ------------------- |
| sent_active           | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| sent_unfinished       | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| sent_last_chance      | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| sent_discover         | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| last_weekly           | 0.0%   | 0     |                                            |                     |
| user_id               | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |
| sent_2weeks_inactive  | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| created_at            | 100.0% | 1     | 2018-04-20T11:30:22 -> 2018-04-20T11:30:22 | 2018-04-20 11:30:22 |
| sent_welcome_mail     | 100.0% | 1     | 1.0 -> 1.0                                 | [redacted]          |
| sent_2months_inactive | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| updated_at            | 100.0% | 1     | 2018-04-20T11:30:22 -> 2018-04-20T11:30:22 | 2018-04-20 11:30:22 |

### user_membership.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `9`

| Colonna         | Piena  | Unici | Range                                      | Esempi                        |
| --------------- | ------ | ----- | ------------------------------------------ | ----------------------------- |
| gifted          | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| canceled        | 100.0% | 1     | 1.0 -> 1.0                                 | 1                             |
| user_id         | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                      |
| membership_type | 100.0% | 1     |                                            | [redacted]                    |
| end_date        | 100.0% | 1     |                                            | 2100-01-01 00:00:00 +0000 UTC |
| updated_at      | 100.0% | 1     | 2018-04-20T12:13:49 -> 2018-04-20T12:13:49 | 2018-04-20 12:13:49           |
| custom_data     | 0.0%   | 0     |                                            |                               |
| start_date      | 100.0% | 1     |                                            | 2018-04-20 12:13:49 +0000 UTC |
| created_at      | 100.0% | 1     | 2018-04-20T12:13:49 -> 2018-04-20T12:13:49 | 2018-04-20 12:13:49           |

### user_personal_data.csv

- Tipo ipotizzato: `people/social`
- Righe: `4`
- Colonne: `6`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                                   |
| ---------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------------------ |
| updated_at | 100.0% | 3     | 2018-04-20T11:06:33 -> 2020-01-27T12:32:00 | 2020-01-27 12:28:53, 2018-04-20 11:06:33, 2020-01-27 12:32:00            |
| id         | 100.0% | 4     | 6575250.0 -> 10863254.0                    | 6575250, 6575252, 6575253, 10863254                                      |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                 |
| name       | 100.0% | 4     |                                            | cover, country-code, bio, favorite-character                             |
| value      | 75.0%  | 3     |                                            | https://dg31sz3gwrwan.cloudfront.net/fanart/80547/104811-7-q, it, 529323 |
| created_at | 100.0% | 3     | 2018-04-20T11:05:23 -> 2020-01-27T12:32:00 | 2018-04-20 11:05:23, 2018-04-20 11:06:33, 2020-01-27 12:32:00            |

### user_platform.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `8`

| Colonna       | Piena  | Unici | Range                                      | Esempi              |
| ------------- | ------ | ----- | ------------------------------------------ | ------------------- |
| registered_on | 100.0% | 1     |                                            | iphone              |
| iphone_cnt    | 100.0% | 1     | 121.0 -> 121.0                             | [redacted]          |
| ipad_cnt      | 100.0% | 1     | 0.0 -> 0.0                                 | [redacted]          |
| android_cnt   | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| web_cnt       | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| created_at    | 100.0% | 1     | 2018-04-20T10:20:22 -> 2018-04-20T10:20:22 | 2018-04-20 10:20:22 |
| updated_at    | 100.0% | 1     | 2023-06-20T10:12:51 -> 2023-06-20T10:12:51 | 2023-06-20 10:12:51 |
| user_id       | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |

### user_session.csv

- Tipo ipotizzato: `people/social`
- Righe: `4`
- Colonne: `10`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                                                                                       |
| ---------- | ------ | ----- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                                     |
| platform   | 100.0% | 1     |                                            | ios                                                                                                                          |
| source     | 100.0% | 3     |                                            | notification-friend-joined, notification-badge-unlocked, deeplink                                                            |
| updated_at | 100.0% | 4     | 2018-04-20T12:24:34 -> 2020-10-19T18:42:54 | 2018-04-20 12:24:34, 2018-04-20 12:37:11, 2018-04-23 19:48:57, 2020-10-19 18:42:54                                           |
| medium     | 0.0%   | 0     |                                            |                                                                                                                              |
| campaign   | 0.0%   | 0     |                                            |                                                                                                                              |
| id         | 100.0% | 4     | 15489638.0 -> 38706172.0                   | 15489638, 15489850, 15628520, 38706172                                                                                       |
| created_at | 100.0% | 4     | 2018-04-20T12:24:34 -> 2020-10-19T18:42:54 | 2018-04-20 12:24:34, 2018-04-20 12:37:11, 2018-04-23 19:48:57, 2020-10-19 18:42:54                                           |
| content    | 0.0%   | 0     |                                            |                                                                                                                              |
| deeplink   | 100.0% | 4     |                                            | tvst://user/20321004/detail, tvst://user/20319846/badges?badge_id=viewed-profile, tvst://user/9957877/detail, tvst://r/1viva |

### user_setting.csv

- Tipo ipotizzato: `people/social`
- Righe: `32`
- Colonne: `6`

| Colonna    | Piena  | Unici | Range                                      | Esempi                                                                                                    |
| ---------- | ------ | ----- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| id         | 100.0% | 32    | 132781623.0 -> 1017245233.0                | 132781623, 132781624, 132781625, 132781626, 132781627                                                     |
| user_id    | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                  |
| name       | 100.0% | 32    |                                            | signup-hint, signup-hint-color, latest-version, show_skip_signup, show_personal_info_screen_in_onboarding |
| value      | 100.0% | 22    |                                            | faster-setup, #8ed43d, smart-categories-v2, 1, 0                                                          |
| created_at | 100.0% | 18    | 2018-04-20T10:20:22 -> 2026-07-06T13:29:12 | 2018-04-20 10:20:22, 2018-04-20 10:20:35, 2018-04-20 10:23:09, 2018-04-20 10:24:09, 2018-04-20 10:27:22   |
| updated_at | 100.0% | 21    | 2018-04-20T10:20:22 -> 2026-07-06T13:29:12 | 2018-04-20 10:20:22, 2018-04-20 10:25:03, 2018-04-20 10:20:35, 2020-09-03 21:01:54, 2019-03-23 22:34:14   |

### user_social_data.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `8`

| Colonna     | Piena  | Unici | Range                                      | Esempi                        |
| ----------- | ------ | ----- | ------------------------------------------ | ----------------------------- |
| user_id     | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                      |
| screen_name | 100.0% | 1     |                                            | Chiara Callegari              |
| picture_url | 0.0%   | 0     |                                            |                               |
| created_at  | 100.0% | 1     | 2018-04-20T10:20:35 -> 2018-04-20T10:20:35 | 2018-04-20 10:20:35           |
| updated_at  | 100.0% | 1     | 2020-01-27T12:32:02 -> 2020-01-27T12:32:02 | 2020-01-27 12:32:02           |
| image_id    | 100.0% | 1     |                                            | 5ad9bef7d8322                 |
| gender      | 100.0% | 1     |                                            | female                        |
| birthday    | 100.0% | 1     |                                            | 1998-11-27 00:00:00 +0000 UTC |

### user_statistics.csv

- Tipo ipotizzato: `episodes`
- Righe: `1`
- Colonne: `13`

| Colonna             | Piena  | Unici | Range                                      | Esempi              |
| ------------------- | ------ | ----- | ------------------------------------------ | ------------------- |
| nb_memes            | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| score               | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| created_at          | 100.0% | 1     | 2018-04-20T10:23:09 -> 2018-04-20T10:23:09 | 2018-04-20 10:23:09 |
| updated_at          | 100.0% | 1     | 2026-07-04T04:16:38 -> 2026-07-04T04:16:38 | 2026-07-04 04:16:38 |
| nb_episodes_watched | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| id                  | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |
| nb_shows_followed   | 100.0% | 1     | 223.0 -> 223.0                             | 223                 |
| nb_likes            | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| user_id             | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |
| time_spent          | 100.0% | 1     | 133983.0 -> 133983.0                       | 133983              |
| nb_comments         | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| nb_friends          | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |
| nb_reviews          | 100.0% | 1     | 0.0 -> 0.0                                 | 0                   |

### user_tv_show_data.csv

- Tipo ipotizzato: `episodes`
- Righe: `137`
- Colonne: `6`

| Colonna          | Piena  | Unici | Range                    | Esempi                                                         |
| ---------------- | ------ | ----- | ------------------------ | -------------------------------------------------------------- |
| is_followed      | 100.0% | 2     | 0.0 -> 1.0               | 1, 0                                                           |
| is_favorited     | 100.0% | 1     | 0.0 -> 0.0               | 0                                                              |
| nb_episodes_seen | 100.0% | 69    | 0.0 -> 281.0             | 65, 43, 67, 92, 11                                             |
| tv_show_name     | 100.0% | 137   |                          | Lizzie McGuire, Phil of the Future, Recess, Hercules, The O.C. |
| user_id          | 100.0% | 1     | 20319846.0 -> 20319846.0 | 20319846                                                       |
| tv_show_id       | 100.0% | 137   | 71119.0 -> 443312.0      | 71119, 71714, 71780, 72163, 72164                              |

### watched_on_episode.csv

- Tipo ipotizzato: `episodes`
- Righe: `1`
- Colonne: `8`

| Colonna               | Piena  | Unici | Range                                      | Esempi              |
| --------------------- | ------ | ----- | ------------------------------------------ | ------------------- |
| episode_number        | 100.0% | 1     | 1.0 -> 1.0                                 | 1                   |
| user_id               | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846            |
| episode_id            | 100.0% | 1     | 10147190.0 -> 10147190.0                   | 10147190            |
| watched_on_source_id  | 100.0% | 1     | 4.0 -> 4.0                                 | 4                   |
| created_at            | 100.0% | 1     | 2024-01-10T00:31:46 -> 2024-01-10T00:31:46 | 2024-01-10 00:31:46 |
| updated_at            | 100.0% | 1     | 2024-01-10T00:31:46 -> 2024-01-10T00:31:46 | 2024-01-10 00:31:46 |
| tv_show_name          | 100.0% | 1     |                                            | What If…?           |
| episode_season_number | 100.0% | 1     | 2.0 -> 2.0                                 | 2                   |

### webhook_data.csv

- Tipo ipotizzato: `people/social`
- Righe: `1`
- Colonne: `8`

| Colonna        | Piena  | Unici | Range                                      | Esempi                                                       |
| -------------- | ------ | ----- | ------------------------------------------ | ------------------------------------------------------------ |
| updated_at     | 100.0% | 1     | 2018-04-21T00:41:51 -> 2018-04-21T00:41:51 | 2018-04-21 00:41:51                                          |
| data_processed | 100.0% | 1     | 1.0 -> 1.0                                 | 1                                                            |
| user_id        | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                     |
| id             | 100.0% | 1     | 5153284.0 -> 5153284.0                     | 5153284                                                      |
| source         | 100.0% | 1     |                                            | AppsFlyer                                                    |
| external_id    | 100.0% | 1     |                                            | 1524226808567-3175832                                        |
| data_received  | 100.0% | 1     |                                            | {"mac":null,"idfv":"1CDBBBB1-E458-4363-9F82-B7F45D8A1E47","a |
| created_at     | 100.0% | 1     | 2018-04-20T10:21:10 -> 2018-04-20T10:21:10 | 2018-04-20 10:21:10                                          |

### where-to-watch-prod-table.csv

- Tipo ipotizzato: `episodes`
- Righe: `56`
- Colonne: `13`

| Colonna          | Piena  | Unici | Range                                      | Esempi                                                                                                                                                                                                                                                                                                               |
| ---------------- | ------ | ----- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vote_type        | 100.0% | 2     |                                            | how-did-you, where-did-you                                                                                                                                                                                                                                                                                           |
| user_id          | 100.0% | 1     | 20319846.0 -> 20319846.0                   | 20319846                                                                                                                                                                                                                                                                                                             |
| type             | 100.0% | 1     |                                            | selection                                                                                                                                                                                                                                                                                                            |
| hash_key         | 100.0% | 54    |                                            | aefb2fc2-75b2-4c73-8eaa-5729b794b025, e5c578d0-d2c5-4f69-b45a-65198841c8ab, af73cb4c-0e19-4d8a-8f2e-e0a560962031, 758d716d-5a34-4c48-8a79-4fa2416e2a91, 9ccb2445-ef51-4a54-91c3-8885df405746                                                                                                                         |
| episode_id       | 100.0% | 7     | 0.0 -> 10147193.0                          | 0, 796411, 7912769, 5801751, 10147192                                                                                                                                                                                                                                                                                |
| created_at       | 100.0% | 56    | 2021-07-22T10:30:47 -> 2026-03-19T11:28:27 | 2021-07-22 10:35:30, 2021-11-14 15:10:08, 2021-07-22 10:38:05, 2022-01-19 13:52:46, 2021-07-22 10:37:40                                                                                                                                                                                                              |
| id               | 100.0% | 56    |                                            | 658224ed-17c5-46bb-b21f-88cf5d9e88a0, a55d7e1b-c3f6-4d19-9862-5bafaf960d7b, cefb201c-cfb3-40e7-a0bf-43575a45e64c, 17bb07f3-f2ed-4d40-a765-1e94b704ebf0, f958ab66-c4c7-432f-893b-29ed42f81336                                                                                                                         |
| range_key        | 100.0% | 7     | 20319846.0 -> 20319846.0                   | 20319846, 796411-20319846, 7912769-20319846, 5801751-20319846, 10147192-20319846                                                                                                                                                                                                                                     |
| network_platform | 100.0% | 30    |                                            | map[app_bundle_id:<nil> app_download_link:<nil> app_link:<ni, map[app_bundle_id:<nil> app_download_link:<nil> app_link:<ni, map[app_bundle_id:<nil> app_download_link:<nil> app_link:<ni, map[app_bundle_id:<nil> app_download_link:<nil> app_link:<ni, map[app_bundle_id:tv.mirada.iris.android.inspire.skygo app_d |
| movie_name       | 0.0%   | 0     |                                            |                                                                                                                                                                                                                                                                                                                      |
| series_name      | 10.71% | 4     |                                            | The Office (US), Emily in Paris, Once Upon a Time (2011), What If…?                                                                                                                                                                                                                                                  |
| season_number    | 10.71% | 3     | 1.0 -> 6.0                                 | 6, 1, 2                                                                                                                                                                                                                                                                                                              |
| episode_number   | 10.71% | 6     | 1.0 -> 11.0                                | 1, 5, 11, 3, 2                                                                                                                                                                                                                                                                                                       |

## Prime domande per il sito

- Quali file contengono le azioni personali, non solo il catalogo?
- Esistono date di visione affidabili per costruire una timeline?
- I voti/commenti sono completi abbastanza per una vista dei preferiti?
- Ci sono ID comuni per collegare episodi, serie e film senza ambiguita?