from backend.db_connect import get_db_connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            phone_number TEXT,
            address TEXT,
            status TEXT DEFAULT 'active',
            type TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()