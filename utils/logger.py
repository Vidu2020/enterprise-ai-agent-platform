import json
from datetime import datetime


def log_incident(ticket, issue, intent, solution, summary):

    record = {
        "timestamp": datetime.now().isoformat(),
        "ticket_id": ticket,
        "issue": issue,
        "intent": intent,
        "solution": solution,
        "summary": summary
    }

    try:
        with open("logs/incident_logs.json", "r") as f:
            data = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(record)

    with open("logs/incident_logs.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved Incident: {ticket}")