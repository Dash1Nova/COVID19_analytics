#!/bin/bash
echo "Pipeline started"

echo "Loading demographic data"

python etl/ingest_data.py

if [ $? -ne 0 ]
then
    echo "Data ingestion failed"
    exit 1
fi

echo "Running automated EDA."

snowsql \
-a gdlvltj-wt58849 \
-u DARJA \
-r ACCOUNTADMIN \
-w COMPUTE_WH \
-f sql/EDA.sql \
-o output_format=csv \
-o output_file=EDA_REPORT.csv

if [ $? -ne 0 ]
then
    echo "EDA failed"
    exit 1
fi

echo "Pipeline completed"
echo "EDA report generated and saved to file:"
echo "EDA_REPORT.csv"