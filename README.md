# Reddit Moderator Governance Archive (RMGA)

RMGA is a non-commercial, moderator-operated external governance and audit archive
for subreddits I moderate.

It is designed to provide structured moderation transparency, auditability,
and reporting using moderation log metadata retrieved via Reddit’s Data API.

---

## Purpose

This tool enables:

- Historical moderation activity tracking
- Governance transparency reporting
- Exportable audit summaries
- Structured moderation analytics
- Configurable data retention controls

It is strictly limited to subreddits for which the operator has moderator authorisation.

Initial target:
- r/synthetic_options

---

## Explicit Non-Goals

RMGA is NOT:

- A Devvit app
- A Reddit-hosted community application
- A content classifier
- An engagement bot
- A growth automation tool
- A moderation automation engine
- A user messaging tool
- A scraping or crawling utility
- An AI/ML training pipeline

---

## Functional Scope

The application reads moderation log metadata only, including:

- Action type (e.g., remove, approve, ban, lock)
- Event timestamps
- Moderator username
- Target author username
- Target content identifiers
- Rule/removal reason references (where available)

The application does NOT:

- Post comments
- Perform moderation actions
- Vote or influence ranking
- Send messages
- Modify content
- Infer sensitive user attributes
- De-anonymise users
- Store full post/comment bodies as a dataset

---

## Architecture Overview

- Python backend
- OAuth-based Reddit API access (read-only)
- Structured relational storage (SQLAlchemy)
- Idempotent ingestion design
- Configurable retention-based pruning
- CSV export generation
- REST API endpoints for metrics and summaries
- Fully off-platform execution

---

## Data Governance Principles

- Data minimisation (metadata only)
- Configurable retention window (default: 90 days)
- Internal deletion of expired records
- No commercial use
- No data resale or redistribution
- No AI training or derivative dataset creation

---

## Repository Structure

- `collector/` — ingestion logic
- `storage/` — database models and schema
- `retention/` — retention pruning
- `reports/` — metrics and exports
- `app/` — FastAPI service layer

---

## License

MIT