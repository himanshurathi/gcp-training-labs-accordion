# GCP Training Program — Hands-On Notebook Labs

All hands-on labs for the 5-day Google Cloud Platform training program live in this repo.
Click any **Open in Colab** badge below to launch that lab directly — no setup, no cloning, no local Python environment required.

> **First time here?** Run [`_shared/setup_check.ipynb`](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/_shared/setup_check.ipynb) once before Day 1. It confirms your GCP project, billing, and required APIs are ready.
>
> **Before you run any lab:** open it in Colab, click **File → Save a copy in Drive**, then edit only the **Configuration** cell near the top (your project ID, region, bucket name). Everything else runs as-is.

---

## Day 1 — GCP Foundations
<sub>![Day 1](https://img.shields.io/badge/Day%201-GCP%20Foundations-4285F4)</sub>

| Lab | Topics | Open |
|---|---|---|
| 01 — GCS, Storage & Lifecycle | Buckets, storage classes, object lifecycle, ACLs | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/day1-foundations/01_gcs_storage_lifecycle.ipynb) |
| 02 — Pub/Sub & Schema Ingestion | Subscriptions, pull/push, schema registry, contract-driven ingestion | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/day1-foundations/02_pubsub_schema_ingestion.ipynb) |
| 03 — BigQuery Basics | Datasets, tables, views, materialized views, partitioning & clustering | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/day1-foundations/03_bigquery_basics.ipynb) |

## Day 2 — BigQuery Advanced & Governance
<sub>![Day 2](https://img.shields.io/badge/Day%202-BigQuery%20Advanced-34A853)</sub>

| Lab | Topics | Open |
|---|---|---|
| 01 — External Tables & BigLake | GCS/Iceberg/Parquet querying, pricing & reservations, IAM | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/day2-bigquery-advanced/01_biglake_external_tables.ipynb) |
| 02 — BQML & Vector Search | BigQuery ML, Iceberg/change history/time travel, vector search for RAG | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/day2-bigquery-advanced/02_bqml_vector_search.ipynb) |
| 03 — Lineage, RLS & Encryption | Remote functions, Dataplex lineage, row-level security, CMEK/AEAD | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/day2-bigquery-advanced/03_lineage_rls_cmek.ipynb) |

## Day 3 — Orchestration, Pipelines & Security
<sub>![Day 3](https://img.shields.io/badge/Day%203-Orchestration%20%26%20Security-FBBC05)</sub>

*Labs coming soon — Cloud Composer, Dataflow patterns, Datastream CDC, Data Fusion, Dataproc serverless, Data Catalog & policy tags, audit logs.*

## Day 4 — Vertex AI Platform & Gen AI
<sub>![Day 4](https://img.shields.io/badge/Day%204-Vertex%20AI%20%26%20Gen%20AI-A142F4)</sub>

*Labs coming soon — Vertex architecture, managed notebooks & Colab Enterprise, AutoML/HPT/custom training, Feature Store, Gemini, Model Garden, Matching Engine, Agent Builder.*

## Day 5 — MLOps & Infra Reliability
<sub>![Day 5](https://img.shields.io/badge/Day%205-MLOps%20%26%20Infra-EA4335)</sub>

*Labs coming soon — Vertex AI Pipelines, Model Registry, CI/CD for ML, model monitoring, GenAI evaluation, GKE, multi-project topology, monitoring & logging.*

## Capstone
| Lab | Open |
|---|---|
| Capstone starter | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/capstone/capstone_starter.ipynb) |

---

### Shared utilities
- [`_shared/setup_check.ipynb`](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/_shared/setup_check.ipynb) — run once before Day 1: verifies auth, enables required APIs, checks billing.
- [`_shared/cleanup.ipynb`](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/_shared/cleanup.ipynb) — run at the end of each day to tear down buckets, reservations, and other billed resources.
- [`_shared/template_notebook.ipynb`](https://colab.research.google.com/github/YOUR-ORG/gcp-training-labs/blob/main/_shared/template_notebook.ipynb) — standard structure used to author every lab in this repo (for internal use when building Day 3–5).

### Notes
- Replace `YOUR-ORG/gcp-training-labs` in every link above with your actual GitHub org/repo name once the repo is created.
- All labs run on **Google Colab (free tier)**. Day 4 additionally introduces **Colab Enterprise** as a managed alternative.
- Every lab's Configuration cell uses the same four variables (`PROJECT_ID`, `REGION`, `BUCKET_NAME`, `DATASET_NAME`) — edit those once per notebook and the rest runs unchanged.
- Some labs touch billed operations (BigQuery reservations, Vertex training jobs, etc.) — cost warnings are called out inline before any such cell.
