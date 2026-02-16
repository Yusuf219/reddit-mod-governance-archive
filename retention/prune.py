import os
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

from storage.db import SessionLocal
from storage.models import ModerationEvent

load_dotenv()

RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "90"))
SUBREDDIT_NAME = os.getenv("SUBREDDIT_NAME", "synthetic_options")

def prune_old_events():
    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)

    db = SessionLocal()
    try:
        q = db.query(ModerationEvent).filter(
            ModerationEvent.subreddit == SUBREDDIT_NAME,
            ModerationEvent.created_utc < cutoff
        )
        count = q.count()
        q.delete(synchronize_session=False)
        db.commit()
        return {
            "deleted": count,
            "cutoff": cutoff.isoformat(),
            "retention_days": RETENTION_DAYS
        }
    finally:
        db.close()

if __name__ == "__main__":
    print(prune_old_events())