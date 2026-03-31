from backend.db_connect import get_db_connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            phone_number TEXT,
            address TEXT
            status TEXT DEFAULT 'active'
        )
    """)


    #testing my gitHub connection
    conn.commit()

    print("Table created")

    cursor.execute("""
        INSERT INTO users (first_name, last_name, email, password, phone_number, address)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("John", "Doe", "john.doe@example.com", "password123", "123-456-7890", "123 Main St"))
    conn.commit()
    print("Sample user inserted")
    conn.close()

init_db()