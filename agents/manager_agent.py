from services.gemini_service import ask_gemini


def generate_summary(
    issue,
    ticket_id,
    intent_result,
    solution
):

    prompt = f"""
    Generate an executive incident summary.

    Ticket Number:
    {ticket_id}

    User Issue:
    {issue}

    Intent Analysis:
    {intent_result}

    Suggested Solution:
    {solution}

    Include:

    Incident Summary
    Business Impact
    Recommended Action
    Priority
    SLA
    """

    return ask_gemini(prompt)