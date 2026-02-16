# API Access Plan

RMGA will use Reddit’s Data API with the minimum necessary access.

## Intended Access

- Read-only moderation log retrieval
- Retrieval limited to subreddits the operator moderates

## Intended Scope Principles

- No write actions
- No user messaging
- No voting
- No automated moderation actions
- No content scraping outside API

## Authentication

- OAuth-based script application
- Clear and descriptive User-Agent string
- Credentials stored locally via environment variables
- No credential storage in version control

## Rate Limiting

- Respect Reddit API rate limits
- No excessive polling
- Configurable ingestion interval

## Commercial Use

- Non-commercial use only
- No resale, licensing, or monetization