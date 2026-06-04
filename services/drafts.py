from typing import Dict, Optional
from schemas import ApplicationData

_drafts_db: Dict[str, ApplicationData] = {}

def save_draft(user_id: str, data: ApplicationData) -> bool:
    _drafts_db[user_id] = data
    return True

def load_draft(user_id: str) -> Optional[ApplicationData]:
    return _drafts_db.get(user_id)

def clear_draft(user_id: str) -> bool:
    if user_id in _drafts_db:
        del _drafts_db[user_id]
        return True
    return False