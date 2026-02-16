# Compliance & Responsible Use (RMGA)

This project is an external, moderator-operated governance and audit archive for subreddits I moderate (initially: r/synthetic_options). It is designed to support moderation transparency, auditability, and compliance reporting using structured metadata.

## Scope and Intended Use
- **Moderator-only tool** used for governance reporting for subreddits I moderate.
- **Off-platform**: runs on infrastructure I control; not a Devvit app and not hosted on Reddit.
- **Read-only with respect to Reddit**: retrieves moderation log metadata for reporting.

## What this tool does
- Retrieves moderation log entries and related metadata (action type, timestamps, IDs, actor/subject usernames).
- Stores structured event metadata in a local database for audit/reporting.
- Generates exportable CSV reports and summary metrics.
- Applies retention controls (deletion of stored records beyond configured retention).

## What this tool does NOT do
- **No automated actions on Reddit** (no moderation actions, no posting, no commenting, no voting).
- **No user messaging** (no DMs, no chat, no replies).
- **No engagement manipulation** (no karma/vote manipulation, no growth tactics).
- **No scraping/crawling** outside approved API access.
- **No profiling or sensitive inference** (no health/politics/sexual orientation inference; no de-anonymisation).
- **No AI/ML training** using Reddit data.

## Data minimisation
- Stores only metadata necessary for governance reporting (e.g., action type, timestamps, identifiers).
- Does not store full post/comment bodies as a long-term dataset.
- Report outputs are derived from stored moderation metadata.

## Retention and deletion
- Stored records are subject to a configurable retention policy (e.g., 90 days).
- Records older than the retention threshold are deleted via an off-platform pruning job.
- This deletion is internal housekeeping on stored records and does not perform actions on Reddit.

## Transparency
- Uses a clear and descriptive `User-Agent` string that identifies the tool and operator account.
- The project README describes purpose and limitations to prevent misuse.

## Security
- Secrets (API credentials) are stored in a local `.env` file and excluded from version control.
- Access is limited to accounts/subreddits the operator is authorised to moderate.

## Subreddit scope
- Initial target: **r/synthetic_options**
- Additional subreddits only if the operator has explicit moderator authorisation.