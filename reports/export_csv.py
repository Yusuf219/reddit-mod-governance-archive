import os
import csv
from datetime import datetime, timezone
from dotenv import load_dotenv

from storage.db import SessionLocal
from storage.models import ModerationEvent

load_dotenv()

SUBREDDIT_NAME = os.getenv("SUBREDDIT_NAME", "synthetic_options")
EXPORT_DIR = os.getenv("EXPORT_DIR", "./exports")

def export_mod_events_csv():
    os.makedirs(EXPORT_DIR, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"mod_events_{SUBREDDIT_NAME}_{ts}.csv"
    path = os.path.join(EXPORT_DIR, filename)

    db = SessionLocal()
    try:
        rows = (
            db.query(ModerationEvent)
            .filter(ModerationEvent.subreddit == SUBREDDIT_NAME)
            .order_by(ModerationEvent.created_utc.asc())
            .all()
        )

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "modlog_id",
                "subreddit",
                "action",
                "created_utc",
                "moderator",
                "target_author",
                "target_fullname",
                "details",
                "description",
                "permalink",
            ])

            for r in rows:
                writer.writerow([
                    r.modlog_id,
                    r.subreddit,
                    r.action,
                    r.created_utc.isoformat(),
                    r.moderator,
                    r.target_author,
                    r.target_fullname,
                    r.details,
                    r.description,
                    r.permalink,
                ])

        return {"exported": len(rows), "path": path}
    finally:
        db.close()

if __name__ == "__main__":
    print(export_mod_events_csv())