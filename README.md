# Reddit Moderator Governance Archive (RMGA)

A non-commercial, moderator-operated external governance and audit archive
for subreddits I moderate.

This project is an external moderation infrastructure tool that uses Reddit's
Data API to ingest structured moderation event metadata and store it in a
centralised database for audit, reporting, and compliance purposes.

This is NOT:
- A Devvit App
- A Reddit Community App
- An engagement automation bot
- A content classifier
- A growth tool

This tool:
- Runs off-platform
- Stores structured moderation event metadata
- Provides audit exports and reporting
- Implements configurable retention policies
- Operates only on authorized subreddits

Initial target subreddit:
- r/synthetic_options

## Scope

The application reads:
- Moderation log events
- Associated metadata (IDs, timestamps, moderator username, author username)
- Rule/removal reason identifiers

The application does NOT:
- Post comments
- Vote on content
- Send private messages
- Automate moderation actions
- Train AI models
- Infer sensitive attributes
- Scrape data

## Architecture Overview

- Python-based backend
- OAuth-based Reddit API access
- Structured relational storage
- Retention-controlled deletion jobs
- Exportable CSV audit reports

## License

MIT
