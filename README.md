# batch-metric-aggregation
This repository contains a simple PySpark batch job that processes time-series metric data and aggregates it into daily buckets.

## Challenge Objective
Given a dataset of metrics with values and timestamps:
- Group by `metric` and 24-hour `time bucket`
- Caluculate:
  - Average value
  - Minimum value
  - Maximum value

## Sample Input Given

| metric        | value | timestamp                   |
|---------------|-------|-----------------------------|
| temperature   | 88.0  | 2022-06-04T12:01:00.000Z    |
| temperature   | 89.0  | 2022-06-04T12:01:30.000Z    |
| precipitation | 0.5   | 2022-06-04T14:23:32.000Z    |

## Output 

| date       | metric        | avg_value | min_value | max_value |
|------------|---------------|-----------|-----------|-----------|
| 2022-06-04 | temperature   | 88.5      | 88.0      | 89.0      |
| 2022-06-04 | precipitation | 0.5       | 0.5       | 0.5       |

## How to Run

1. Open the `batch_aggregation.py` file in Databricks or any PySpark-enabled environment.
2. Run the script on any active cluster.
3. The output will be displayed as a grouped and aggregated DataFrame.

## Notes

- This is a proof-of-concept implementation.
- Input format is simplified and hardcoded for clarity, but can be replaced with file-based input for real-world use.
