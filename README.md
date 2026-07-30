# Project overview & architecture

## Project Description:

This project implements an end-to-end COVID-19 analytics platform that integrates epidemiological data from Snowflake Marketplace with additional demographic information to provide enriched analytical insights.

The main goal of the platform is to demonstrate a complete modern data engineering workflow:

- Data ingestion from external datasets
- Data cleaning and transformation using SQL
- Data modeling in Snowflake
- Supplementary metadata storage using MongoDB
- Automated Exploratory Data Analysis (EDA)
- REST API development
- Interactive dashboard visualization

## Architecture Diagram:

                    Snowflake Marketplace
                COVID-19 Epidemiological Data
                            |
                            |
                            v
                     Raw Data Layer
                     (Snowflake)
                            |
                            |
                            v
                    Python Data Pipeline
                    - Data ingestion
                    - Data validation
                    - EDA automation
                            |
                            |
            ---------------------------------
            |                               |
            v                               v

    Snowflake Warehouse             MongoDB Atlas

      Clean Layer                 NoSQL Metadata Layer
      - COVID_CLEAN                   - comments
      - DEMOGRAPHICS_CLEAN            - external_information
                            |
                            |
                            v
                      Analytics Layer
                      - COVID_DAILY
                            |
                            |
                            v
                        FastAPI
                            |
                            |
                            v
                  Plotly Dash Dashboard

## Tech Stack:

- Data Warehouse: Snowflake
- Data Engineering: Python 3.11+, Snowflake Connector for Python, SQL, Bash scripting
- API: FastAPI, Uvicorn, Pydantic
- NoSQL Database: MongoDB Atlas
- Analytics & Visualization: Plotly, Dash
- Development Environment: Git, GitHub, dotenv environment configuration

# Repository Structure

├── api/ # Backend API layer
│ ├── app.py # Main API execution file
│ ├── cache.py # API caching logic for frequently requested data
│ ├── config.py # Backend and environment configuration
│ ├── models.py # Data models and schemas
│ ├── mongodb_connection.py # MongoDB client and connection setup
│ ├── mongodb_service.py # MongoDB queries
│ ├── snowflake_connection.py # Snowflake engine and session setup
│ └── snowflake_service.py # Snowflake queries
├── automation/
│ └── run_pipeline.sh # Shell script to automate EDA execution
├── dashboard/ # Frontend data visualization
│ ├── api_client.py # HTTP client connecting frontend to API
│ ├── app.py # Dashboard interface execution file
│ └── charts.py # Chart and data visualization components
├── data/ # Raw data storage
│ └── world_pop_mig_186_countries.csv # Source demographics dataset
├── docs/ # Project documentation and diagrams
├── etl/ # Extract, Transform, Load (ETL) pipeline
│ ├── config.py # Configurations for ETL processes
│ └── ingest_data.py # Script for ingesting CSV data into Snowflake
├── mongodb/
│ └── schema.js # MongoDB collection schema
├── sql/
│ ├── EDA.sql # Exploratory Data Analysis queries
│ └── enhancement.sql # Data transformations scripts
├── README.md # Project description and setup guide
└── requirements.txt # Project Python dependencies

# Deployment & Execution Guide

### Prerequisites

Ensure you have the following installed on your target VM:

- Python 3.10+
- Docker
- Snowflake Account (AWS - Stockholm Region) with the marketplace "COVID-19 Epidemiological Data" dataset active

1. Clone the Repository:
   git clone <https://github.com/Dash1Nova/COVID19_analytics/tree/main>
   Open root directory in your local environment.
2. Environment Configuration
   Create a `.env` file in the root directory and fill in your Snowflake credentials, warehouse targets, and MongoDB connection:
   SNOWFLAKE_USER=your_user
   SNOWFLAKE_PASSWORD=your_password
   SNOWFLAKE_ACCOUNT=your_account
   MONGO_URI=your_mongodb_uri
3. Run the automation file ingest and explore raw data:
   chmod +x automation/run_pipeline.sh
   ./automation/run_pipeline.sh
4. Run docker comand to initialize a pipeline to use the platform: `docker-compose up --build`
5. Once the pipeline initializes successfully:
   **Backend API:** Available at `http://localhost:8000/docs` (Swagger UI)
   **Interactive Dashboard:** Available at `http://localhost:8050`
