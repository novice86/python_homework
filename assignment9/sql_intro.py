import sqlite3
import os


def create_tables(conn):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
            );
        """)
        print("Publishers table checked/created.")
    except sqlite3.Error as e:
        print(f"Database error while creating 'publishers' table: {e}")
    
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(id)
            );
        """)
        print("Magazines table checked/created.")
    except sqlite3.Error as e:
        print(f"Database error while creating 'magazines' table: {e}")
        
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                UNIQUE(name, address)
            );
        """)
        print("Subscribers table checked/created.")
    except sqlite3.Error as e:
        print(f"Database error while creating 'subscribers' table: {e}")

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                PRIMARY KEY (subscriber_id, magazine_id),
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(id)
            );
        """)
        print("Subscriptions table checked/created.")
    except sqlite3.Error as e:
        print(f"Database error while creating 'subscriptions' table: {e}")


def add_publisher(conn, name):
    """Add a new publisher to the publishers table."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")
        cursor.execute("SELECT id FROM publishers WHERE name = ?", (name,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Database error in add_publisher: {e}")


def add_magazine(conn, name, publisher_id):
    """Add a new magazine to the magazines table."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
            (name, publisher_id)
        )
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists.")
        cursor.execute("SELECT id FROM magazines WHERE name = ?", (name,))
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        print(f"Database error in add_magazine: {e}")


def add_subscriber(conn, name, address):
    """Add a new subscriber to the subscribers table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        existing_subscriber = cursor.fetchone()
        if existing_subscriber:
            print(f"Subscriber '{name}' with address '{address}' already exists.")
            return existing_subscriber[0]

        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)",
            (name, address)
        )
        return cursor.lastrowid

    except sqlite3.Error as e:
        print(f"Database error in add_subscriber: {e}")


def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    """Add a new subscription to the subscriptions table."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
        )
    except sqlite3.IntegrityError:
        print(f"Subscription for subscriber ID '{subscriber_id}' and magazine ID '{magazine_id}' already exists.")
    except sqlite3.Error as e:
        print(f"Database error in add_subscription: {e}")


def run_queries(conn):
    """Run queries to retrieve data from the database."""
    try:
        cursor = conn.cursor()

        # 1. Retrieve all subscribers
        print("\n All Subscribers:")
        cursor.execute("SELECT * FROM subscribers")
        for row in cursor.fetchall():
            print(row)

        # 2. Retrieve all magazines sorted by Name
        print("\n All Magazines sorted by name:")
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        for row in cursor.fetchall():
            print(row)

        # 3. Find magazines for a particular publisher
        print("\n Magazines for Tech Press:")
        cursor.execute("""
            SELECT magazines.name, publishers.name
            FROM magazines
            JOIN publishers ON magazines.publisher_id = publishers.id
            WHERE publishers.name = ?
        """, ("Tech Press",))
        for row in cursor.fetchall():
            print(row)

    except sqlite3.Error as e:
        print(f"Database error in run_queries: {e}")


# Task 1: Create a New SQLite Database
db_path = "../db/magazines.db"

conn = None
try:
    conn = sqlite3.connect(db_path)
    print("Connected to the database successfully.")

    # Task 2: Define Database Structure
    create_tables(conn) 

    # Task 3: Populate the Database with Sample Data
    # Enable foreign key support
    conn.execute("PRAGMA foreign_keys = 1;")

    # Populate Publishers
    pub1_id = add_publisher(conn, "Tech Press")
    pub2_id = add_publisher(conn, "Food Media")
    pub3_id = add_publisher(conn, "Outdoor Group")
    
    # Populate Magazines
    mag1_id = add_magazine(conn, "Python Weekly", pub1_id)
    mag2_id = add_magazine(conn, "Gourmet Monthly", pub2_id)
    mag3_id = add_magazine(conn, "Camping Life", pub3_id)
    
    # Populate Subscribers
    sub1_id = add_subscriber(conn, "Alice Smith", "123 Main St, NY")
    sub2_id = add_subscriber(conn, "Bob Jones", "456 Oak Rd, CA")
    sub3_id = add_subscriber(conn, "Charlie Brown", "789 Pine Ln, TX")
    
    # Populate Subscriptions
    add_subscription(conn, sub1_id, mag1_id, "2027-01-01")  # Alice subscribes to Python Weekly
    add_subscription(conn, sub1_id, mag2_id, "2026-12-31")  # Alice subscribes to Gourmet Monthly
    add_subscription(conn, sub2_id, mag3_id, "2028-05-15")  # Bob subscribes to Camping Life
    add_subscription(conn, sub3_id, mag1_id, "2027-06-30")  # Charlie subscribes to Python Weekly

    # Commit all the transactions!
    conn.commit()
    print("Data successfully inserted and committed.")

    # Task 4: Run Queries to Retrieve Data
    run_queries(conn)
        
except sqlite3.Error as e:
    print(f"A general SQLite error occurred: {e}")

finally:
    if conn:
        conn.close()
