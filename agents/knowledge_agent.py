import json


def get_solution(issue):
    issue = issue.lower()

    with open("data/knowledge_base.json", "r") as f:
        kb = json.load(f)

    for item in kb:
        if item["category"].lower() in issue:
            return item["solution"]

    return "No known solution found. Escalate to Service Desk."