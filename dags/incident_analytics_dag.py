import json
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def incident_analytics():

    try:

        with open(
            "/opt/airflow/project/incident_logs.json",
            "r",
            encoding="utf-8"
        ) as f:

            incidents = json.load(f)

    except Exception:

        incidents = []

    print("\n========== REPORT ==========\n")

    total_incidents = len(incidents)

    print(
        f"Total Incidents: {total_incidents}"
    )

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

    print("\nTop Categories:\n")

    for category, count in categories.items():

        print(
            f"{category}: {count}"
        )

    report = {
        "generated_at": datetime.now().isoformat(),
        "total_incidents": total_incidents,
        "category_summary": categories
    }

    report_path = (
        "/opt/airflow/project/reports/incident_report.json"
    )

    with open(
        report_path,
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
    tags=["analytics"]
) as dag:

    analytics_task = PythonOperator(
        task_id="incident_analytics",
        python_callable=incident_analytics
    )