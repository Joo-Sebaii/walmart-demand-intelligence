# System Architecture

## 1. Introduction

The Walmart Demand Intelligence Platform is designed as a modular, end-to-end Machine Learning system for retail demand forecasting and inventory decision support.

The architecture separates data processing, feature engineering, model development, evaluation, serving, monitoring, and optimization into independent components.

This separation supports maintainability, scalability, reproducibility, and future integration of MLOps capabilities.

This document describes the target architecture. Components will be implemented incrementally throughout the project roadmap.

## 2. High-Level Architecture

The platform follows a modular architecture consisting of the following major layers:

1. Data Layer
2. Feature Engineering Layer
3. Machine Learning Layer
4. Evaluation and Experiment Tracking Layer
5. Serving Layer
6. Monitoring Layer
7. Inventory Optimization Layer

### System Flow

```text
             M5 Forecasting Dataset
                       |
                       v
              Data Ingestion
                       |
                       v
              Data Validation
                       |
                       v
               Data Storage
                       |
                       v
             Feature Engineering
                       |
                       v
             Forecasting Models
                       |
                       v
             Model Evaluation
                       |
                       v
              Model Registry
                       |
                       v
                Model Serving
                       |
                       v
             Demand Predictions
                       |
                       v
           Inventory Decision Support
                       |
                       v
             Monitoring & Feedback
                       |
                       v
             Retraining Workflows
```

## 3. Component Architecture

### 3.1 Data Layer

Responsible for acquiring, organizing, validating, and preparing the M5 dataset.

Responsibilities:

- Dataset ingestion.
- Raw data preservation.
- Data quality validation.
- Missing-value analysis.
- Data consistency checks.
- Intermediate and processed data management.

Directory:

`src/walmart_demand/data/`

Storage structure:

- `data/raw/`
- `data/interim/`
- `data/processed/`

### 3.2 Feature Engineering Layer

Transforms validated historical data into meaningful forecasting features.

Potential features include:

- Lag features.
- Rolling statistics.
- Temporal features.
- Calendar indicators.
- Price-related features.
- Event-related features.

Directory:

`src/walmart_demand/features/`

### 3.3 Machine Learning Layer

Responsible for developing, training, and managing forecasting models.

Responsibilities:

- Baseline model development.
- Deep Learning model development.
- Training workflows.
- Model configuration.
- Model checkpoint management.

Directories:

- `src/walmart_demand/models/`
- `src/walmart_demand/training/`

PyTorch will be used for Deep Learning development.

### 3.4 Evaluation and Experiment Tracking

Provides systematic model evaluation and experiment reproducibility.

Responsibilities:

- Forecast accuracy evaluation.
- Multi-horizon performance analysis.
- Model comparison.
- Experiment tracking.
- Model selection.

Directory:

`src/walmart_demand/evaluation/`

MLflow is planned for experiment tracking and model lifecycle management.

### 3.5 Serving Layer

Exposes trained forecasting models through application interfaces.

Responsibilities:

- Loading trained models.
- Processing prediction requests.
- Generating demand forecasts.
- Returning structured prediction results.

Directory:

`src/walmart_demand/serving/`

FastAPI is planned for model serving.

### 3.6 Monitoring Layer

Monitors the reliability and performance of the deployed forecasting system.

Responsibilities:

- Data quality monitoring.
- Data drift detection.
- Prediction monitoring.
- Model performance tracking.
- Retraining triggers.

Directory:

`src/walmart_demand/monitoring/`

### 3.7 Inventory Optimization Layer

Transforms demand forecasts into inventory decision support.

Responsibilities:

- Using forecasts as optimization inputs.
- Evaluating inventory-related constraints.
- Generating inventory recommendations.
- Supporting operational decision-making.

Directory:

`src/walmart_demand/optimization/`

OR-Tools is planned for optimization workflows.

## 4. Data Flow

The expected data flow is:

1. Historical retail data is ingested from the M5 dataset.
2. Raw data is validated and organized.
3. Data is transformed into forecasting-ready datasets.
4. Feature engineering generates temporal and contextual features.
5. Forecasting models are trained using prepared data.
6. Models are evaluated against appropriate forecasting metrics.
7. Selected models are made available for inference.
8. Forecast outputs are used by inventory decision-support components.
9. Monitoring components track data and model behavior.
10. Retraining workflows can be triggered when necessary.

## 5. Configuration Management

Project configuration is separated from application logic.

Primary configuration:

`configs/base.yaml`

Configuration loading is implemented in:

`src/walmart_demand/config.py`

The configuration system will be extended as additional components and environments are introduced.

## 6. Logging and Error Handling

The project uses Python's standard logging infrastructure.

Logging implementation:

`src/walmart_demand/logging_config.py`

The current implementation supports:

- Console logging.
- Rotating file logging.
- Configurable logging levels.
- UTF-8 log files.

Logging will be integrated into data, training, serving, and monitoring workflows as they are developed.

## 7. Testing Strategy

The testing structure separates tests by scope:

- `tests/unit/`: Individual component tests.
- `tests/integration/`: Interactions between components.
- `tests/api/`: API behavior and endpoint tests.

Pytest is used as the testing framework.

Code quality is enforced using:

- Ruff.
- Black.
- Pre-commit hooks.

## 8. CI Architecture

GitHub Actions provides automated Continuous Integration.

The current CI workflow:

`.github/workflows/ci.yml`

It runs on pushes and pull requests targeting the `main` branch.

Current automated checks:

1. Repository checkout.
2. Python environment setup.
3. Poetry installation.
4. Dependency installation.
5. Ruff linting.
6. Black formatting verification.
7. Pytest execution.

## 9. Technology Decisions

| Concern | Selected Technology |
|---|---|
| Programming Language | Python |
| Dependency Management | Poetry |
| Configuration | YAML |
| Data Processing | Pandas, NumPy |
| Deep Learning | PyTorch |
| Experiment Tracking | MLflow |
| Database | PostgreSQL |
| API | FastAPI |
| Optimization | OR-Tools |
| Containerization | Docker |
| Workflow Orchestration | Apache Airflow |
| Testing | Pytest |
| Linting | Ruff |
| Formatting | Black |
| CI | GitHub Actions |

The architecture allows these technologies to be introduced as needed rather than requiring the entire stack during initial development.

## 10. Architectural Principles

The system follows these principles:

- Modularity: Each component has a clear responsibility.
- Separation of concerns: Data, models, serving, and monitoring remain independent.
- Reproducibility: Dependencies and configurations are version-controlled.
- Testability: Components are designed to support automated testing.
- Scalability: Data and model workflows can expand progressively.
- Maintainability: Reusable logic belongs in the application package.
- Observability: Logging and monitoring are incorporated into the system design.

## 11. Current Implementation Status

The initial project foundation is complete.

Implemented:

- Repository structure.
- Poetry environment.
- Dependency management.
- YAML configuration loading.
- Logging infrastructure.
- Initial unit tests.
- Ruff and Black.
- Pre-commit hooks.
- GitHub Actions CI.

Planned for subsequent phases:

- M5 data ingestion.
- Data validation and processing.
- Feature engineering.
- Forecasting models.
- Experiment tracking.
- Inventory optimization.
- Model serving.
- Monitoring and automated retraining.

This architecture will evolve as implementation progresses.
