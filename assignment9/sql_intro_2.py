import pandas as pd
import sqlite3

# Task 5: Read Data into a DataFrame
# Read data into a DataFrame, as described in the lesson. 
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT l.line_item_id, l.quantity, l.product_id, p.product_name, p.price
    FROM line_items AS l
    JOIN products as p ON l.product_id = p.product_id
    """
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head())

    # Add new column total to the DataFrame
    df["total"] = df["quantity"] * df["price"]
    print("\n DataFrame with total column:\n")
    print(df.head())

    # Add groupby() code to group by the product_id. 
    df_grouped = df.groupby(by="product_id").agg({
        "line_item_id": "count",
        "total": "sum",
        "product_name": "first"
    }).reset_index()
    print("Grouped DataFrame:\n")
    print(df_grouped.head())

    # Sort the DataFrame by the product_name column.
    df_sorted = df_grouped.sort_values(by="product_name")
    df_sorted.to_csv("order_summary.csv", index=False, encoding="utf-8-sig")
