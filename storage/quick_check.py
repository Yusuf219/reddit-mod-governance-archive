from storage.db import SessionLocal
from storage.models import ModerationEvent

db = SessionLocal()
try:
    count = db.query(ModerationEvent).count()
    latest = db.query(ModerationEvent).order_by(ModerationEvent.created_utc.desc()).first()
    print("count:", count)
    if latest:
        print("latest:", latest.modlog_id, latest.action, latest.created_utc, latest.target_author)
finally:
    db.close()