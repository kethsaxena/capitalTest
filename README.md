# 🐍 Python Solution for CAPITAL group Screening TEST

# 📜 Problem Statement

1. Build an ETL process for stock pricing data ingestion into a database.

## 🛠️ Constraints:

1. Data: 10 CSV files (total 100GB) in random order.
1. Server Resources:
    1. Memory: 32 GB
    1. CPU: 4 cores
    1. Disk Space: 100 GB free

## SRC Table Schema 
 
| Column        | Data Type | Description                        |
|---------------|-----------|------------------------------------|
| date          | datetime  | Date in format `%Y-%m-%d`          |
| id            | int       | Stock ID (ranging from 1 to 200)   |
| price         | float     | Stock price                        |
| trade_volume  | int       | Number of shares traded            |

## TARGET Table Scehma
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

1. Return  Table:
Each stock's returns

| Column      | Data Type | Description                                       |
|-------------|-----------|---------------------------------------------------|
| date        | datetime  | Date in format `%Y-%m-%d`                          |
| stk_001     | float     | Return for stock ID 1 (`(price_today - price_yesterday) / price_yesterday`) |
| stk_002     | float     | Return for stock ID 2                              |
| ...         | float     | ...                                                |
| stk_200     | float     | Return for stock ID 200                            |

# 🚀 Solution Approach
This repository contains Python script solution.py for the problem.

## The key steps involved are:
1. Input Parsing: Accept the input in a structured format using Pandas dataframe with chunking 
1. Core Logic: Pivot the stock
1. Output Generation: Persist Price, Volume and Returns table

## 🛠️ Technologies Used
1. Python 3.x
1. Standard PyPi Libraries Only https://pypi.org/project/emoji/
