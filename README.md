# Retail-Favorita

## Table of contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Architecture](#architecture)
- [Data Organization](#data-organization)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api-layer)
- [Roadmap](#roadmap)
- [Tech Stack](#tech-stack)


## Project Overview

This project aims to simulate a realistic retail data platform using a public dataset.
It focuses on designing an end-to-end data workflow including data ingestion, transformation, and data serving through an API layer.

The goal is to demonstrate practical data engineering and analytics skills such as:

- data pipeline structuring  
- dataset lifecycle management  
- API-based data exposure  
- preparation of analytics-ready datasets  
- integration with downstream use cases (BI, machine learning)

The project is intentionally built incrementally to reflect real-world data platform development. It uses the Favorita Store Sales dataset from Kaggle as an external data source to simulate a retail analytics environment.

The platform is intentionally simplified and designed for learning purposes while following realistic industry patterns.

[Back to top](#retail-favorita)

## Objectives

- Build a clean and reproducible data project structure
- Simulate multiple operational data sources in a retail context
- Implement a layered data architecture (raw → curated)
- Expose data through a lightweight API service
- Prepare datasets for analytical and machine learning use cases
- Follow incremental and production-oriented development practices

[Back to top](#retail-favorita)

## Architecture

The project follows a simplified modern data platform design:

```text
External Data Sources (Kaggle dataset)
        ↓
Simulated Source APIs (FastAPI)
        ↓
Ingestion Layer (Raw data)
        ↓
Transformation Layer (Interim datasets)
        ↓
Analytics Layer (Curated datasets)
        ↓
Data Consumption (BI / ML)
```

This structure enables clear separation of concerns and reproducible data workflows.

[Back to top](#retail-favorita)

## Data Organization

The project follows a simplified data platform layout inspired by modern data engineering practices.
The goal is to clearly separate the different stages of the data lifecycle, from external sources to business-ready datasets.

```bash
data/
├── external/
├── raw/
├── interim/
└── curated/
```

`external/`

This directory contains external source data provided to the project, such as public datasets or files received from third parties.
These datasets are stored as-is and are never modified.
They represent the initial data supply used to simulate a realistic retail environment.

**Example**

```bash
data/external/kaggle/train.csv
```

`raw/ (Bronze layer)`

This directory represents the data ingestion landing zone.
Data stored here is collected from operational sources (e.g. APIs, file drops, external systems) with minimal or no transformation.
The objective is to ensure:

- traceability
- reproducibility
- auditability

Raw data may contain inconsistencies, duplicates or technical formats.

**Example**

```bash
data/raw/sales_api/2024-01-01/data.json
```

`interim/ (Silver layer)`

This directory contains cleaned and standardized datasets.
Typical operations at this stage include:

- schema normalization
- data type correction
- filtering and basic quality checks
- table joins and enrichment

The data is technically reliable but may not yet be fully shaped for business consumption.

**Example**

```bash
data/interim/sales_clean.parquet
```

`curated/ (Gold layer)`

This directory stores analytics-ready datasets designed for direct use by downstream applications such as:

- dashboards
- machine learning models
- reporting tools
- analytical APIs

Data in this layer reflects business logic, aggregations and feature engineering.

**Example**

```bash
data/curated/daily_store_product_sales.parquet
```

[Back to top](#retail-favorita)

## Installation

### Create the conda environment

You can create and activate the conda environment using the commands as follow.

- Create the conda environment:

```bash
conda env create -f environment.yml 
```

- Activate the conda environment :

```bash
conda activate retail-favorita 
```

You can as well deactivate it using this command :

```bash
conda deactivate
```

[Back to top](#retail-favorita)

## Usage

The project will progressively provide scripts and services to:

- download external datasets
- simulate operational data sources
- ingest and transform retail data
- expose curated datasets through an API

[Back to top](#retail-favorita)

## API Layer

The project includes a FastAPI application that simulates multiple operational data sources in a retail environment.

The API exposes three main domains:

- **Retail**: operational sales and store data
- **Government**: calendar events and holidays
- **Finance**: external economic indicators (oil prices)

### Available endpoints

#### Retail
- `GET /retail/stores`
- `GET /retail/stores/{store_nbr}`
- `GET /retail/sales`

#### Government
- `GET /government/holidays`

#### Finance
- `GET /finance/oil`

All endpoints support filtering through query parameters such as:
- date ranges (`start_date`, `end_date`)
- store identifiers
- locale and event filters

The API is designed to simulate real-world data sources and will be used as input for ingestion pipelines.

### Run the API

```bash
uvicorn retail_api.main:app --reload
```

Then access:
- API: http://127.0.0.1:8000
- Documentation: http://127.0.0.1/8000/docs

[Back to top](#retail-favorita)

## Roadmap

Planned development steps:

- [x] External dataset ingestion automation
- [x] Dataset analysis
- [x] Dataset preparation for API
- [x] Creation of simulated retail source APIs
- [ ] Raw data ingestion pipeline
- [ ] Data cleaning and standardization
- [ ] Curated analytics dataset creation
- [x] API endpoints for data access
- [ ] Integration with BI and machine learning workflows

[Back to top](#retail-favorita)

## Tech Stack

- Python  
- FastAPI  
- Pandas  
- Pytest  
- Conda environment management  

Additional tools will be integrated progressively.

[Back to top](#retail-favorita)