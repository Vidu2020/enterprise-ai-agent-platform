import json
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def generate_report():

    try:

        with open(
            "/opt/airflow/project/incident_logs.json",
            "r",
            encoding="utf-8"
        ) as f:

            incidents = json.load(f)

    except Exception:

        incidents = []

    total_incidents = len(incidents)

    categories = {}

    for incident in incidents:

        intent = incident.get(
            "intent",
            "Unknown"
        )

        category = intent.split("\n")[0]

        categories[category] = (
            categories.get(category, 0) + 1
        )

    report = {
        "generated_at": datetime.now().isoformat(),
        "total_incidents": total_incidents,
        "category_summary": categories
    }

    print("\n========== INCIDENT REPORT ==========")
    print(json.dumps(report, indent=4))

    with open(
        "/opt/airflow/project/reports/incident_report.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4
        )

    print(
        "\nReport saved successfully."
    )


with DAG(
    dag_id="incident_analytics",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["analytics", "reporting"],
) as dag:

    report_task = PythonOperator(
        task_id="generate_incident_report",
        python_callable=generate_report
    )