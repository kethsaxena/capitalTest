import os
import pandas as pd

# INPUT VARIABLES
CSV_FOLDER = '/path/to/csv/folder'  # folder containing 10 csv files
OUTPUT_FOLDER = '/path/to/csv/folder'
CHUNK_SIZE = 500_000                # number of rows per chunk to control memory
PRICE_OUTPUT = f"{OUTPUT_FOLDER}/price_table.csv"    # intermediate merged price file
VOLUME_OUTPUT = f"{OUTPUT_FOLDER}/volume_table.csv"  # intermediate merged volume file
RETURNS_OUTPUT = f"{OUTPUT_FOLDER}/returns_table.csv"


## HELPER FUNCTIONS 

def pivot_chunk(df_chunk, value_column):
    """Pivot a chunk DataFrame on 'date' and 'id' into wide format with value_column."""
    pivoted = df_chunk.pivot_table(index='date', columns='id', values=value_column, aggfunc='first')
    pivoted.columns = [f'stk_{int(col):03d}' for col in pivoted.columns]
    pivoted = pivoted.reset_index()
    return pivoted


def process_files():
    # Initialize empty DataFrames
    price_table = None
    volume_table = None
    
    # STEP 1 Read the data from a sever directory with 10 CSV files in Chunks
    # List all CSV files
    csv_files = [os.path.join(CSV_FOLDER, file) for file in os.listdir(CSV_FOLDER) if file.endswith('.csv')]
    

    # STEP 2 Apply The transformation PIVOTS
    for csv_file in csv_files:
        print(f"Reading {csv_file}...")
        chunk_iter = pd.read_csv(csv_file, chunksize=CHUNK_SIZE, parse_dates=['date'])

        for chunk in chunk_iter:
            # Pivot chunk
            price_pivot = pivot_chunk(chunk, 'price')
            volume_pivot = pivot_chunk(chunk, 'trade_volume')

            # Merge
            if price_table is None:
                price_table = price_pivot
            else:
                price_table = pd.concat([price_table, price_pivot])

            if volume_table is None:
                volume_table = volume_pivot
            else:
                volume_table = pd.concat([volume_table, volume_pivot])
       

    # Aggregate and sort final tables
    print("Final aggregation and sorting...")
    price_table = price_table.groupby('date').first().sort_index().reset_index()
    volume_table = volume_table.groupby('date').first().sort_index().reset_index()
    
    # STEP 3 Persist Data into Itntermediary CSV Tables   
    # Save CSV tables
    print(f"Saving price table to {PRICE_OUTPUT}...")
    price_table.to_csv(PRICE_OUTPUT, index=False)
    print(f"Saving volume table to {VOLUME_OUTPUT}...")
    volume_table.to_csv(VOLUME_OUTPUT, index=False)

    # STEP 4 Calculate returns
    print("Calculating stock returns...")
    returns_df = price_table.copy()
    for col in returns_df.columns:
        if col != 'date':
            returns_df[col] = returns_df[col].pct_change()

    # Save returns
    print(f"Saving returns table to {RETURNS_OUTPUT}...")
    returns_df.to_csv(RETURNS_OUTPUT, index=False)

    print("ETL process completed successfully...")

def main():
    process_files()


if __name__ == "__main__":
    main()


