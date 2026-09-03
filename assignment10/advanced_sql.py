import sqlite3


# Define the path to the database file
db_path = "../db/lesson.db"

# Task 1: Complex JOINs with Aggregation
sql_statement = """
    SELECT o.order_id, SUM(l.quantity * p.price) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5
"""

with sqlite3.connect(db_path) as conn:
    # Use column names as keys for the rows returned from the query.  
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        results = cursor.fetchall()

        print("Order ID | Total Price")
        print("-----------------------")
        for row in results:
            print(f"{row['order_id']} | {row['total_price']:.2f}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")


# Task 2: Understanding Subqueries
sql_statement = """
    SELECT c.customer_name, AVG(total_price) AS average_total_price
    FROM customers c
    JOIN (
        SELECT o.customer_id AS customer_id_b, SUM(l.quantity * p.price) AS total_price
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id
        JOIN products p on l.product_id = p.product_id
        GROUP BY o.order_id
    ) ON c.customer_id = customer_id_b
    GROUP BY c.customer_id    
"""

with sqlite3.connect(db_path) as conn:
    # Use column names as keys for the rows returned from the query.  
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        results = cursor.fetchall()

        print("Customer Name | Average Total Price")
        print("-----------------------------------")
        for row in results:
            print(f"{row['customer_name']} | {row['average_total_price']:.2f}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")


# Task 3: An Insert Transaction Based on Data
with sqlite3.connect(db_path) as conn:
    # Enforce valid foreign keys right after connecting
    conn.execute("PRAGMA foreign_keys = 1")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        # Get customer_id for "Perez and Sons"
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = ?", ("Perez and Sons",))
        customer_id = cursor.fetchone()["customer_id"]

        # Get employee_id for "Miranda Harris"
        cursor.execute("SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?", ("Miranda", "Harris"))
        employee_id = cursor.fetchone()["employee_id"]

        # Get the 5 least expensive products
        cursor.execute("SELECT product_id FROM products ORDER by price ASC LIMIT 5")
        product_ids = [row["product_id"] for row in cursor.fetchall()]

        # Insert a new order for "Perez and Sons" handled by "Miranda Harris"
        cursor.execute("""
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id
        """, (customer_id, employee_id))

        order_id = cursor.fetchone()["order_id"]

        # Insert line items for the 5 least expensive products, each with a quantity of 10
        for p_id in product_ids:
            cursor.execute("""
                INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)
            """, (order_id, p_id, 10))


        cursor.execute("""
            SELECT l.line_item_id, l.quantity, p.product_name
            FROM line_items l
            JOIN products p ON l.product_id = p.product_id
            WHERE l.order_id = ?
        """, (order_id, ))

        final_results = cursor.fetchall()
        print(f"{'Line Item ID':<15} | {'Quantity':<10} | {'Product Name'}")
        print("-" * 50)
        
        for row in final_results:
            print(f"{row['line_item_id']:<15} | {row['quantity']:<10} | {row['product_name']}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()


# Task 4: Aggregation with HAVING
sql_statement = """
    SELECT e.first_name, e.last_name, COUNT(*) as orders_count 
    FROM employees e 
    JOIN orders o ON e.employee_id = o.employee_id 
    GROUP BY e.employee_id 
    HAVING COUNT(*) > 5;
"""

with sqlite3.connect(db_path) as conn:
    # Use column names as keys for the rows returned from the query.  
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        results = cursor.fetchall()

        print("First Name | Last Name | Orders Count")
        print("-------------------------------------")
        for row in results:
            print(f"{row['first_name']} | {row['last_name']} | {row['orders_count']}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
