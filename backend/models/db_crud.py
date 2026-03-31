import sqlite3
from backend.models.db_connect import get_connection


""" 

# --------------------- CREATE ---------------------
def add_user(first_name, last_name, email, password, phone_number, address):

 
    """Insert a new user into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (first_name, last_name, email, password, phone_number, address)
             VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, password, phone_number, address))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise ValueError(f"Email '{email}' already exists.") from e
    finally:
        conn.close()



# --------------------- READ (for search) -----------------------
def get_user_by_email(email):
    """Fetch a single user by email."""
    conn = get_connection()
    cursor = conn.cursor()
    # the trailing comma is needed for Python to consider email as a single-item tuple instead of an iterable string
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,)) 
    # fetchone returns a user tuple if user is found and None if the user is not found
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_id(id):
    """Fetch a single user by id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,)) 
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
    """Fetch all users."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users







"""