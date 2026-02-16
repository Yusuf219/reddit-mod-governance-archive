from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.sql import func
from .db import Base

class ModerationEvent(Base):
    __tablename__ = "moderation_events"

    id = Column(Integer, primary_key=True, index=True)

    subreddit = Column(String(100), nullable=False, index=True)

    # Unique ID for the modlog entry (when available). We’ll use this for idempotency.
    modlog_id = Column(String(128), nullable=True, unique=True, index=True)

    action = Column(String(64), nullable=False, index=True)  # e.g. removecomment, removelink
    target_fullname = Column(String(32), nullable=True, index=True)  # t1_/t3_ ID
    target_author = Column(String(64), nullable=True, index=True)
    moderator = Column(String(64), nullable=True, index=True)

    # UTC timestamp from Reddit (stored as a DateTime)
    created_utc = Column(DateTime(timezone=True), nullable=False, index=True)

    # Reason / rule fields (may be null depending on modlog record)
    details = Column(String(512), nullable=True)
    description = Column(String(512), nullable=True)

    # Optional permalink (may be null if not derivable)
    permalink = Column(String(512), nullable=True)

    inserted_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

Index("ix_mod_events_subreddit_created", ModerationEvent.subreddit, ModerationEvent.created_utc)
