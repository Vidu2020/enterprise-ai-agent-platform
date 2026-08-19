def make_decision(intent_result, solution):

    decision = {
        "assignment_group": "Service Desk",
        "solution": solution,
        "intent": intent_result
    }

    if "network" in intent_result.lower():
        decision["assignment_group"] = "Network Team"

    elif "password" in intent_result.lower():
        decision["assignment_group"] = "Identity Access Team"

    elif "software" in intent_result.lower():
        decision["assignment_group"] = "Application Support"

    return decision