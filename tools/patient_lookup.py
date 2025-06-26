import json
import logging
from typing import List, Dict, Optional

# Logging setup
logging.basicConfig(filename="logs/patient_lookup.log", level=logging.INFO)

# Load data once
with open("data/patients.json", "r") as f:
    patients_data = json.load(f)

def lookup_patient_by_name(name: str) -> Optional[List[Dict]]:
    """Return all matches (can be >1 if names are similar)."""
    name_lower = name.lower()
    matches = [p for p in patients_data if name_lower in p["name"].lower()]
    
    logging.info(f"Patient lookup attempted for name='{name}'. Matches found: {len(matches)}")
    
    return matches if matches else None
