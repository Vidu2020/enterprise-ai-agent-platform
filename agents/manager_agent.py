from services.gemini_service import ask_gemini


def generate_summary(intent_output, solution, ticket_id):

    prompt = f"""
You are an IT Service Manager.

Use the information below to create an executive incident summary.

STRICT RULES:
- Do not repeat the analysis word-for-word.
- Use the Priority and SLA from the analysis.
- Include the incident number.
- Keep the summary concise and professional.

Analysis:
{intent_output}

Known Solution:
{solution}

Incident Number:
{ticket_id}

Return ONLY in this format:

Incident Number:
<ticket_id>

Incident Summary:
<summary>

Business Impact:
<impact>

Recommended Action:
<action>

Priority:
<priority>

SLA:
<sla>
"""

    return ask_gemini(prompt)