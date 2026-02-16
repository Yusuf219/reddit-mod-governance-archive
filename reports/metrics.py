import os
from datetime import datetime, timedelta, timezone
from collections import Counter, defaultdict
from dotenv import load_dotenv

from storage.db import SessionLocal
from storage.models import ModerationEvent

load_dotenv()

SUBREDDIT_NAME = os.getenv("SUBREDDIT_NAME", "synthetic_options")

def get_metrics(days: int = 30):
    """
    Simple governance metrics for a subreddit over the last N days.
    No content bodies, no inference—just event metadata aggregation.
    """
    since = datetime.now(timezone.utc) - timedelta(days=days)

    db = SessionLocal()
    try:
        rows = (
            db.query(ModerationEvent)
            .filter(
                ModerationEvent.subreddit == SUBREDDIT_NAME,
                ModerationEvent.created_utc >= since
            )
            .all()
        )

        total = len(rows)
        by_action = Counter(r.action for r in rows if r.action)
        by_mod = Counter(r.moderator for r in rows if r.moderator)
        by_target_author = Counter(r.target_author for r in rows if r.target_author)

        # Rule-ish breakdown: we stored strings like "rule:1" in details
        by_rule = Counter()
        for r in rows:
            if r.details and "rule:" in r.details:
                by_rule[r.details.strip()] += 1

        return {
            "subreddit": SUBREDDIT_NAME,
            "window_days": days,
            "since": since.isoformat(),
            "total_events": total,
            "by_action": dict(by_action.most_common()),
            "by_moderator": dict(by_mod.most_common()),
            "top_target_authors": dict(by_target_author.most_common(10)),
            "by_rule": dict(by_rule.most_common()),
        }
    finally:
        db.close()
        
def get_summary(days: int = 30):
    m = get_metrics(days=days)
    actions = m.get("by_action", {})
    return {
        "subreddit": m["subreddit"],
        "window_days": days,
        "total_events": m["total_events"],
        "removals": actions.get("removelink", 0) + actions.get("removecomment", 0),
        "approvals": actions.get("approvelink", 0) + actions.get("approvecomment", 0),
        "locks": actions.get("lock", 0),
        "bans": actions.get("banuser", 0),
        "unbans": actions.get("unbanuser", 0),
        "top_rules": list(m.get("by_rule", {}).items())[:5],
        "top_actions": list(actions.items())[:10],
    }