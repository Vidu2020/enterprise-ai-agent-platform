from services.gemini_service import ask_gemini


def detect_intent(user_query):

    prompt = f"""
    Analyze the following IT issue.

    Issue:
    {user_query}

    Return:

    Category:
    Priority:
    Business Impact:
    Recommendation:
    SLA:
    """

    response = ask_gemini(prompt)

    return response