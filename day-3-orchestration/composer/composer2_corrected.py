from airflow import DAG
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime

PROJECT = "project-2df9d2ad-b6f5-4ed5-997"
BUCKET = "my-training-bucket3894"
DATASET = "sales_dataset"

with DAG(
    dag_id="gcs_to_bq_pipeline",
    schedule_interval="@daily",
    start_date=datetime(2026, 7, 1),
    catchup=False,
) as dag:

    wait_for_file = GCSObjectExistenceSensor(
        task_id="wait_for_input_file",
        bucket=BUCKET,
        object="daily_sales.csv",
        timeout=600,
        poke_interval=60,
    )

    load_to_bq = GCSToBigQueryOperator(
        task_id="load_csv_to_bigquery",
        bucket=BUCKET,
        source_objects=["daily_sales.csv"],
        destination_project_dataset_table=f"{PROJECT}.{DATASET}.raw_sales",
        source_format="CSV",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    transform = BigQueryInsertJobOperator(
        task_id="aggregate_daily_sales",
        configuration={
            "query": {
                "query": f"""
                SELECT
                    region,
                    SUM(amount) AS total_sales
                FROM `{PROJECT}.{DATASET}.raw_sales`
                GROUP BY region
                """,
                "destinationTable": {
                    "projectId": PROJECT,
                    "datasetId": DATASET,
                    "tableId": "sales_by_region",
                },
                "writeDisposition": "WRITE_TRUNCATE",
                "useLegacySql": False,
            }
        },
    )

    wait_for_file >> load_to_bq >> transform
