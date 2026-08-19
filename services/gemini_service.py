from google import genai
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Initialize Gemini Client
client = genai.Client(api_key=api_key)


def ask_gemini(ticket_description):
    """
    Analyze an IT support ticket using Gemini.
    Returns structured output.
    """

    prompt = f"""
Analyze the IT support ticket and respond ONLY in the following format.

Category: <value>
Priority: <value>
Business Impact: <one line>
Recommendation: <one line>
SLA: <value>

Ticket:
{ticket_description}
"""

    for attempt in range(3):

        try:
            chat = client.chats.create(
            model="gemini-2.5-flash-lite"
            )

            response = chat.send_message(prompt)

            return response.text.strip()

            

        except Exception as e:

            error_text = str(e)

            print(f"Attempt {attempt + 1} failed: {error_text}")

            # Quota exceeded
            if "RESOURCE_EXHAUSTED" in error_text or "429" in error_text:
                return """
Category: General Support
Priority: Medium

Business Impact:
AI quota exceeded.

Recommendation:
Route ticket to Service Desk.

SLA:
Business Hours
"""

            # Service temporarily unavailable
            if "503" in error_text or "UNAVAILABLE" in error_text:
                return """
Category: General Support
Priority: Medium

Business Impact:
AI service temporarily unavailable.

Recommendation:
Retry after a few minutes or route to Service Desk.

SLA:
Business Hours
"""

            # Retry for other errors
            if attempt < 2:
                time.sleep(5)

            else:
                return f"Gemini API Error: {error_text}"