import json
import os


def get_solution(issue):

    issue = issue.lower()

    kb_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "data",
        "knowledge_base.json"
    )

    with open(kb_path, "r", encoding="utf-8") as f:
        kb = json.load(f)

    for item in kb:

        category = item["category"].lower()

        if category in issue:
            return item["solution"]

    return "No known solution found. Escalate to Service Desk."