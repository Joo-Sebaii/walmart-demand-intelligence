# Walmart Demand Intelligence Platform

An end-to-end Deep Learning and MLOps platform for retail demand forecasting and inventory decision support, built using the M5 Forecasting dataset.

## Overview

The Walmart Demand Intelligence Platform aims to transform historical retail sales data into reliable demand forecasts and actionable inventory insights.

The platform is designed to forecast product demand over a 28-day horizon, quantify forecasting uncertainty, and support inventory planning decisions through data-driven recommendations.

The project follows production-oriented Machine Learning Engineering and MLOps practices, covering the complete lifecycle from data ingestion and validation to model training, deployment, and monitoring.

## Business Problem

Retail businesses face several challenges when planning inventory:

- Demand fluctuations across products and stores.
- Seasonal patterns and special events.
- Overstocking and unnecessary inventory costs.
- Understocking and lost sales opportunities.
- Uncertainty in future demand.

This platform aims to address these challenges through scalable demand forecasting and inventory decision support.

## Project Objectives

- Build reliable multi-horizon demand forecasting pipelines.
- Understand and process hierarchical retail sales data.
- Engineer meaningful temporal and contextual features.
- Develop and evaluate Deep Learning forecasting models.
- Quantify predictive uncertainty.
- Translate forecasts into inventory decision support.
- Establish reproducible ML workflows and experiment tracking.
- Monitor model performance and data drift.
- Support automated model retraining workflows.

## Dataset

The project uses the M5 Forecasting dataset, which contains Walmart retail sales information.

The dataset includes:

- Historical daily sales.
- Calendar information and special events.
- Product selling prices.
- Hierarchical relationships across stores, departments, categories, and products.

The initial development and experimentation will focus on a manageable subset of store-item time series, with gradual expansion as the pipeline matures.

## Planned System Capabilities

- Data ingestion and validation.
- Exploratory data analysis.
- Feature engineering.
- Multi-horizon demand forecasting.
- Probabilistic forecasting and uncertainty estimation.
- Model evaluation and experiment tracking.
- Inventory decision support.
- Model serving through APIs.
- Data and model monitoring.
- Drift detection and retraining workflows.

These capabilities represent the planned system scope and will be implemented incrementally throughout the project roadmap.

## Technology Stack

| Area | Technologies |
|---|---|
| Programming Language | Python |
| Dependency Management | Poetry |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Deep Learning | PyTorch |
| Experiment Tracking | MLflow |
| Data Storage | PostgreSQL |
| API Development | FastAPI |
| Optimization | OR-Tools |
| Containerization | Docker |
| Workflow Orchestration | Apache Airflow |
| Code Quality | Ruff, Black |
| Testing | Pytest |
| CI/CD | GitHub Actions |
| Version Control | Git, GitHub |

Technologies will be introduced progressively as the corresponding project components are implemented.

## Project Structure

```text
walmart-demand-intelligence/
│
├── configs/
│   └── base.yaml
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── docs/
│   └── architecture.md
│
├── notebooks/
│   └── exploratory/
│
├── reports/
│
├── scripts/
│
├── src/
│   └── walmart_demand/
│       ├── data/
│       ├── features/
│       ├── models/
│       ├── training/
│       ├── evaluation/
│       ├── serving/
│       ├── monitoring/
│       ├── optimization/
│       ├── config.py
│       └── logging_config.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── api/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── .pre-commit-config.yaml
├── poetry.lock
├── pyproject.toml
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.14
- Poetry 2.4.1
- Git

### Clone the Repository

```bash
git clone https://github.com/Joo-Sebaii/walmart-demand-intelligence.git

cd walmart-demand-intelligence
```

### Install Dependencies

```bash
poetry install
```

### Activate the Virtual Environment

```bash
poetry shell
```

Alternatively, execute commands directly through Poetry:

```bash
poetry run python --version
```

### Run Tests

```bash
poetry run pytest
```

### Run Code Quality Checks

```bash
poetry run ruff check .
poetry run black --check .
```

### Run Pre-commit Hooks

```bash
poetry run pre-commit run --all-files
```

## Development Standards

The project follows these engineering practices:

- Modular and maintainable source code.
- Separation of configuration from application logic.
- Type hints and meaningful documentation.
- Structured logging.
- Unit and integration testing.
- Reproducible dependency management.
- Automated code quality checks.
- Continuous Integration through GitHub Actions.
- Version-controlled development workflows.

Exploratory notebooks are used for investigation and experimentation, while reusable application logic belongs in the `src/` package.

## Project Roadmap

The project is developed through incremental phases:

1. Project Foundation and Environment Setup.
2. Data Engineering and Data Understanding.
3. Exploratory Data Analysis.
4. Feature Engineering.
5. Baseline Forecasting Models.
6. Deep Learning Forecasting.
7. Probabilistic Forecasting and Uncertainty.
8. Model Evaluation and Experiment Tracking.
9. Inventory Decision Support.
10. Model Serving and API Development.
11. Monitoring and Drift Detection.
12. MLOps Automation and Deployment.

## Current Development Status

**Phase 0 — Project Foundation & Setup: Completed.**

The repository currently includes:

- Modular project structure.
- Python and Poetry environment.
- Dependency management.
- YAML configuration loading.
- Logging infrastructure.
- Ruff and Black configuration.
- Pre-commit hooks.
- Initial unit tests.
- GitHub Actions CI workflow.

Data engineering and forecasting capabilities will be implemented in subsequent phases.

## License

This project is currently under development. Licensing details will be added when finalized.
