# 🤖 Enterprise AI Agent Platform

An intelligent multi-agent IT Service Management (ITSM) platform powered by Google Gemini and Streamlit.

The platform analyzes user-reported IT issues, identifies intent, retrieves knowledge base solutions, generates incident tickets, produces management summaries, and logs incidents for reporting and auditing.

---

# 🚀 Features

## 🎯 Intent Agent
Analyzes user issues using Gemini AI and determines:

- Category
- Priority
- Business Impact
- Recommendation
- SLA

Example:

```text
Input:
VPN not working

Output:
Category: Network
Priority: High
Business Impact: User unable to access internal resources.
Recommendation: Assign to Network Team.
SLA: 4 Hours
```

---

## 📚 Knowledge Agent

Searches an internal knowledge base and suggests predefined solutions.

Example:

```text
Issue:
VPN not working

Solution:
Restart VPN client and reconnect.
```

---

## 🎫 Execution Agent

Automatically creates an incident number.

Example:

```text
INC684901
```

---

## 👔 Manager Copilot

Generates an executive-level incident summary using AI.

Example:

```text
Incident Number:
INC684901

Incident Summary:
User cannot connect to the corporate VPN, preventing access to internal systems.

Business Impact:
Employee productivity is impacted due to lack of access to business resources.

Recommended Action:
Restart VPN client and verify network connectivity.

Priority:
High

SLA:
4 Hours
```

---

## 📊 Incident Dashboard

Displays:

- Total Incidents
- Latest Ticket Number

via Streamlit sidebar metrics.

---

## 📝 Incident Logging

Every incident is automatically logged into:

```text
incident_logs.json
```

for:

- Auditing
- Reporting
- Analytics
- Historical Tracking

---

# 🏗️ Architecture

```text
┌───────────────────┐
│       User        │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│   Intent Agent    │
│  Gemini Analysis  │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Knowledge Agent   │
│ Solution Lookup   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Execution Agent   │
│ Create Incident   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Manager Copilot   │
│ Executive Summary │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Incident Logging  │
└───────────────────┘
```

---

# 📂 Project Structure

```text
enterprise-ai-agent-platform/
│
├── app.py
├── .env
├── requirements.txt
├── incident_logs.json
│
├── agents/
│   ├── __init__.py
│   ├── intent_agent.py
│   ├── knowledge_agent.py
│   ├── execution_agent.py
│   └── manager_agent.py
│
├── services/
│   ├── __init__.py
│   └── gemini_service.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
└── data/
    └── knowledge_base.json
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-org/enterprise-ai-agent-platform.git

cd enterprise-ai-agent-platform
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

```text
streamlit
google-genai
python-dotenv
```

Install manually:

```bash
pip install streamlit google-genai python-dotenv
```

---

# 🔑 Configure Gemini API

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Example:

```env
GOOGLE_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxx
```

---

# 📚 Knowledge Base Configuration

File:

```text
data/knowledge_base.json
```

Example:

```json
[
    {
        "category": "VPN",
        "solution": "Restart VPN client and reconnect."
    },
    {
        "category": "Password",
        "solution": "Reset password from self-service portal."
    },
    {
        "category": "Software",
        "solution": "Raise installation request."
    }
]
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

# 🧪 Sample Test Cases

## VPN Issue

Input:

```text
VPN not working
```

Expected:

```text
Category: Network
Priority: High

Solution:
Restart VPN client and reconnect.
```

---

## Password Issue

Input:

```text
I forgot my password
```

Expected:

```text
Category: Password Reset
Priority: High

Solution:
Reset password from self-service portal.
```

---

## Software Request

Input:

```text
Install Microsoft Visio
```

Expected:

```text
Category: Software Request

Solution:
Raise installation request.
```

---

# 📄 Example Incident Log

```json
[
  {
    "timestamp": "2026-08-19T15:00:00",
    "ticket_id": "INC707378",
    "issue": "I forgot my password",
    "intent": "Category: Password Reset...",
    "solution": "Reset password from self-service portal.",
    "summary": "User unable to access systems..."
  }
]
```

---

# 🎯 Future Enhancements

- Microsoft Teams Integration
- ServiceNow Integration
- Azure OpenAI Support
- Incident Analytics Dashboard
- Multi-Agent Orchestration
- Email Notifications
- Real-Time Monitoring
- RAG-based Knowledge Search
- Vector Database Integration
- Incident Trend Analysis
- SLA Breach Detection

---

# 🔒 Security Considerations

- Keep API keys in `.env`
- Never commit `.env` to Git
- Restrict access to incident logs
- Use role-based authentication
- Mask sensitive ticket information

---

# 👨‍💻 Technology Stack

- Streamlit
- Google Gemini
- Python
- JSON Knowledge Base
- dotenv
- Multi-Agent Architecture

---

# 📜 License

MIT License

---

# 🙌 Acknowledgements

- Google Gemini
- Streamlit
- Python Community

---

## Author

**Parth**

Enterprise AI Agent Platform for Intelligent IT Incident Management 🚀