import json
import os
from datetime import datetime


def log_incident(
    ticket_id,
    issue,
    intent,
    solution,
    summary
):

    log_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "incident_logs.json"
    )

    try:

        with open(
            log_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

    except Exception:

        data = []

    incident = {
        "timestamp": datetime.now().isoformat(),
        "ticket_id": ticket_id,
        "issue": issue,
        "intent": intent,
        "solution": solution,
        "summary": summary
    }

    data.append(incident)

    with open(
        log_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )