from services.gemini_service import ask_gemini

def detect_intent(user_query):

    prompt = f"""

    classify:

    {user_query}

    Return:

    Category
    Priority:
    """

    return ask_gemini(prompt)



