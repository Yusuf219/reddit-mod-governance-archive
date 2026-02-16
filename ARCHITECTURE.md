# System Architecture

RMGA is an external, off-platform governance reporting service.

## High-Level Flow

1. Moderation metadata is retrieved via Reddit’s Data API (read-only).
2. Events are normalised into structured database records.
3. Idempotent ingestion prevents duplicate records.
4. Records are stored in a relational database.
5. Retention policy prunes expired records.
6. Reports and metrics are generated via REST endpoints.
7. CSV exports are generated for audit portability.

## Why This Is Not a Devvit App

Devvit apps run within Reddit’s hosted platform and are scoped to
in-subreddit UI customisation and bot-like interactions.

RMGA requires:

- External persistent storage
- Cross-timeframe aggregation
- Portable export generation
- Retention-managed archival
- Infrastructure-level audit capability

These features are intentionally external and not designed to run
inside Reddit’s community app ecosystem.

## Data Storage Model

Only structured moderation event metadata is stored:

- modlog_id
- action
- timestamps
- moderator username
- target author username
- rule reference
- content identifier
- optional permalink

No sensitive inference or profiling is performed.

## Retention Model

A configurable retention window controls data lifespan.
Expired records are deleted via a pruning job.

Deletion affects only locally stored records.
No deletion operations are performed against Reddit.