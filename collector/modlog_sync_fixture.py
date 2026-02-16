import json
import os
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

from storage.db import SessionLocal
from storage.models import ModerationEvent

load_dotenv()

SUBREDDIT_NAME = os.getenv("SUBREDDIT_NAME", "synthetic_options")

FIXTURE_PATH = Path(__file__).parent / "fixtures" / "modlog_sample.json"


def to_dt_utc(ts: float) -> datetime:
    return datetime.fromtimestamp(ts, tz=timezone.utc)


def ingest_fixture_events():
    if not FIXTURE_PATH.exists():
        raise FileNotFoundError(f"Fixture file not found: {FIXTURE_PATH}")

    with FIXTURE_PATH.open("r", encoding="utf-8") as f:
        events = json.load(f)

    db = SessionLocal()
    inserted = 0
    skipped = 0

    try:
        for e in events:
            modlog_id = e.get("id")
            if not modlog_id:
                # For safety: fixtures must include id
                continue

            exists = (
                db.query(ModerationEvent)
                .filter(ModerationEvent.modlog_id == modlog_id)
                .first()
            )
            if exists:
                skipped += 1
                continue

            created_utc_ts = float(e.get("created_utc", 0))
            created_dt = to_dt_utc(created_utc_ts)

            row = ModerationEvent(
                subreddit=SUBREDDIT_NAME,
                modlog_id=modlog_id,
                action=e.get("action", "unknown"),
                target_fullname=e.get("target_fullname"),
                target_author=e.get("target_author"),
                moderator=e.get("mod"),
                created_utc=created_dt,
                details=e.get("details"),
                description=e.get("description"),
                permalink=e.get("permalink"),
            )

            db.add(row)
            inserted += 1

        db.commit()
        return {"inserted": inserted, "skipped": skipped, "fixture": str(FIXTURE_PATH)}
    finally:
        db.close()


if __name__ == "__main__":
    result = ingest_fixture_events()
    print(result)