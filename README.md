# 🐍 Python Solution for CAPITAL group Screening TEST

# 📜 Problem Statement

1. Build an ETL process for stock pricing data ingestion into a database.

## 🛠️ Constraints:

1. Data: 10 CSV files (total 100GB) in random order.
1. Server Resources:
    1. Memory: 32 GB
    1. CPU: 4 cores
    1. Disk Space: 100 GB free

## SRC
 
| Column        | Data Type | Description                        |
|---------------|-----------|------------------------------------|
| date          | datetime  | Date in format `%Y-%m-%d`          |
| id            | int       | Stock ID (ranging from 1 to 200)   |
| price         | float     | Stock price                        |
| trade_volume  | int       | Number of shares traded            |


## TARGET:
1. Price Table:
Each stock’s price goes into corresponding stock column.

| Column  | Data Type | Description                 |
|---------|-----------|-----------------------------|
| date    | datetime  | Date in format `%Y-%m-%d`   |
| stk_001 | float     | Price for stock ID 1        |
| stk_002 | float     | Price for stock ID 2        |
| ...     | float     | ...                         |
| stk_200 | float     | Price for stock ID 200      |


1. Volume Table:
Each stock’s trade volume goes into corresponding stock column.

| Column  | Data Type | Description                         |
|---------|-----------|-------------------------------------|
| date    | datetime  | Date in format `%Y-%m-%d`           |
| stk_001 | int       | Trade volume for stock ID 1         |
| stk_002 | int       | Trade volume for stock ID 2         |
| ...     | int       | ...                                 |
| stk_200 | int       | Trade volume for stock ID 200       |


# 🚀 Solution Approach
This repository contains a clean and efficient Python solution for the problem.

## The key steps involved are:
1. Input Parsing: Accept the input in a structured format (list, string, tree, etc.).
1. Core Logic: Apply an optimized algorithm (e.g., hash maps, recursion, dynamic programming) to solve the problem efficiently.
1. Output Generation: Return the results in the expected format.

## FLOW 

 ┌─────────────────────┐
 │ 10 CSV Files (100GB)│
 └─────────┬───────────┘
           │ (Read in chunks to handle memory limits)
           ▼
 ┌───────────────────────────────────────────────────┐
 │  Chunked DataFrame (date, id, price, trade_volume)│
 └─────────┬────────────────────┬────────────────────┘
           │                    │
           ▼                    ▼
 ┌────────────────────┐     ┌───────────────────────┐
 │ Pivot for Price    │     │ Pivot for Volume      │
 │ (id → columns)     │     │ (id → columns)        │
 │ Columns: date, stk_001...│    │ Columns: date, stk_001... │
 └─────────┬───────────┘    └──────────┬────────────┘
           │                           │
           ▼                           ▼
 ┌─────────────────────┐    ┌───────────────────────┐
 │ Insert into Price   │    │ Insert into Volume    │
 │ Table in Database   │    │ Table in Database     │
 └─────────────────────┘    └───────────────────────┘


## 🛠️ Technologies Used
1. Python 3.x
1. PySpark
1. Standard PyPi Libraries Only https://pypi.org/project/emoji/ 
