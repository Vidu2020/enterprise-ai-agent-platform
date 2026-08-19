import json

from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime


def monitor_sla():

    try:

        with open(
            "/opt/airflow/project/incident_logs.json",
            "r",
            encoding="utf-8"
        ) as f:

            incidents = json.load(f)

    except Exception:

        incidents = []

    print("\n===== SLA MONITORING REPORT =====\n")

    for incident in incidents:

        ticket_id = incident.get(
            "ticket_id",
            "Unknown"
        )

        print(
            f"Checking SLA for {ticket_id}"
        )

    print(
        f"\nTotal Incidents Checked: {len(incidents)}"
    )


with DAG(
    dag_id="sla_monitoring",
    start_date=datetime(2025, 1, 1),
    schedule="@hourly",
    catchup=False,
    tags=["sla", "monitoring"]
) as dag:

    sla_monitor_task = PythonOperator(
        task_id="monitor_sla",
        python_callable=monitor_sla
    )
