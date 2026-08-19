Since you've now added Apache Airflow, Docker, Incident Analytics, and SLA Monitoring, your README should be updated to reflect the enhanced architecture.

Updated README.md
# 🤖 Enterprise AI Agent Platform

An intelligent AI-powered IT Service Management (ITSM) platform built using:

- Streamlit
- Google Gemini
- Apache Airflow
- Docker
- Python

The platform analyzes IT incidents, retrieves solutions, generates tickets, creates executive summaries, logs incidents, performs analytics, and monitors SLA compliance.

---

# 🚀 Features

## 🎯 Intent Agent

Uses Google Gemini to classify user-reported issues.

### Output

- Category
- Priority
- Business Impact
- Recommendation
- SLA

### Example

Input:

```text
VPN not working
```

Output:

```text
Category: Network
Priority: High
Business Impact: User unable to access internal resources.
Recommendation: Assign to Network Team.
SLA: 4 Hours
```

---

## 📚 Knowledge Agent

Searches an internal knowledge base and recommends solutions.

Example:

```text
Issue:
VPN not working

Solution:
Restart VPN client and reconnect.
```

---

## 🎫 Execution Agent

Automatically creates incident tickets.

Example:

```text
INC684901
```

---

## 👔 Manager Copilot

Generates management-level incident summaries.

Example:

```text
Incident Number:
INC684901

Incident Summary:
User cannot connect to the corporate VPN.

Business Impact:
Employee productivity is impacted.

Recommended Action:
Restart VPN client and verify connectivity.

Priority:
High

SLA:
4 Hours
```

---

## 📝 Incident Logging

Every incident is stored in:

```text
incident_logs.json
```

Used for:

- Auditing
- Reporting
- Analytics
- Historical Tracking

---

## 📊 Incident Analytics

Airflow Analytics DAG automatically analyzes logged incidents.

Outputs:

- Total Incidents
- Top Categories
- Incident Trends
- Management Reports

Generated report:

```text
reports/incident_report.json
```

Example:

```json
{
    "generated_at": "2026-08-19T19:00:00",
    "total_incidents": 11,
    "category_summary": {
        "Network": 3,
        "Password Reset": 2,
        "Software Request": 1
    }
}
```

---

## ⏱️ SLA Monitoring

Airflow SLA Monitoring DAG checks incident aging.

Capabilities:

- SLA Tracking
- Breach Detection
- Monitoring Reports

Example:

```text
Checking SLA for INC471597
Checking SLA for INC824561

Total Incidents Checked: 11
```

---

# 🏗️ System Architecture

```text
                   ┌────────────┐
                   │   User     │
                   └─────┬──────┘
                         │
                         ▼
                ┌────────────────┐
                │   Streamlit UI │
                └─────┬──────────┘
                      │
                      ▼
             ┌───────────────────┐
             │   Intent Agent    │
             └─────┬─────────────┘
                   │
                   ▼
             ┌───────────────────┐
             │ Knowledge Agent   │
             └─────┬─────────────┘
                   │
                   ▼
             ┌───────────────────┐
             │ Execution Agent   │
             └─────┬─────────────┘
                   │
                   ▼
             ┌───────────────────┐
             │ Manager Copilot   │
             └─────┬─────────────┘
                   │
                   ▼
             ┌───────────────────┐
             │ Incident Logs     │
             └─────┬─────────────┘
                   │
      ┌────────────┴─────────────┐
      ▼                          ▼

┌───────────────┐        ┌────────────────┐
│ Analytics DAG │        │ SLA Monitor DAG│
└───────────────┘        └────────────────┘
```

---

# 🔄 Airflow DAGs

## 1. Enterprise Incident Workflow

```text
Intent Agent
      ↓
Knowledge Agent
      ↓
Decision Agent
      ↓
Execution Agent
      ↓
Manager Agent
      ↓
Logging Agent
```

---

## 2. Incident Analytics DAG

```text
incident_logs.json
        ↓
Category Analysis
        ↓
Incident Reporting
        ↓
incident_report.json
```

---

## 3. SLA Monitoring DAG

```text
incident_logs.json
        ↓
SLA Validation
        ↓
Breach Analysis
```

---

# 📂 Project Structure

```text
enterprise-ai-agent-platform/
│
├── app.py
├── .env
├── requirements.txt
├── docker-compose.yml
│
├── incident_logs.json
│
├── reports/
│   └── incident_report.json
│
├── dags/
│   ├── incident_workflow_dag.py
│   ├── incident_analytics_dag.py
│   └── sla_monitoring_dag.py
│
├── agents/
│   ├── intent_agent.py
│   ├── knowledge_agent.py
│   ├── execution_agent.py
│   ├── decision_agent.py
│   └── manager_agent.py
│
├── services/
│   └── gemini_service.py
│
├── utils/
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

### Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

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
apache-airflow
requests
```

---

# 🔑 Configure Gemini API

Create `.env`

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# 🐳 Run Airflow

```bash
docker compose up
```

Airflow URL:

```text
http://localhost:8080
```

---

# ▶️ Run Streamlit

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

# ✅ Airflow Verification

Available DAGs:

```text
enterprise_incident_workflow
incident_analytics
sla_monitoring
```

---

# 🎯 Future Enhancements

- ServiceNow Integration
- Microsoft Teams Integration
- Azure OpenAI Support
- Email Notifications
- RAG-based Search
- Vector Database
- Trend Prediction
- GenAI Incident Analytics
- SLA Breach Notifications

---

# 👨‍💻 Technology Stack

- Python
- Streamlit
- Google Gemini
- Apache Airflow
- Docker
- JSON
- Multi-Agent Systems
- Workflow Orchestration

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Parth**

Enterprise AI Agent Platform for Intelligent IT Incident Management 🚀
