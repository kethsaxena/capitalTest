🐍 Python Solution for CAPITAL group Screening TEST

📜 Problem Statement

1. Build an ETL process for stock pricing data ingestion into a database.

🛠️ Constraints:

1. Data: 10 CSV files (total 100GB) in random order.
2. Server Resources:
3. Memory: 32 GB
4. CPU: 4 cores
5. Disk Space: 100 GB free

SRC
 
Data Structure of CSVs:
date → datetime (format: %Y-%m-%d)
id → int (1 to 200) (stock IDs)
price → float
trade_volume → int

TARGET:
1. Price Table:
Columns: date, stk_001, stk_002, ..., stk_200
Each stock’s price goes into corresponding stock column.

2. Volume Table:
Columns: date, stk_001, stk_002, ..., stk_200
Each stock’s trade volume goes into corresponding stock column.

🚀 Solution Approach
This repository contains a clean and efficient Python solution for the problem.

The key steps involved are:
1. Input Parsing: Accept the input in a structured format (list, string, tree, etc.).
2. Core Logic: Apply an optimized algorithm (e.g., hash maps, recursion, dynamic programming) to solve the problem efficiently.
3. Output Generation: Return the results in the expected format.

🛠️ Technologies Used
1. Python 3.x
2. Standard Libraries Only (no external dependencies)
