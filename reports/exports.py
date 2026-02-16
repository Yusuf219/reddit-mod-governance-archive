import os
from glob import glob
from datetime import datetime, timezone

from reports.export_csv import export_mod_events_csv

EXPORT_DIR = os.getenv("EXPORT_DIR", "./exports")

def latest_export_path():
    os.makedirs(EXPORT_DIR, exist_ok=True)
    files = glob(os.path.join(EXPORT_DIR, "mod_events_*.csv"))
    if not files:
        return None
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]

def export_now():
    return export_mod_events_csv()