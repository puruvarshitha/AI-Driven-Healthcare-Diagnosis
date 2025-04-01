import sqlite3
import bcrypt

# Create Users Table (Run once)
def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to Register User
def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    #hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')

    
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Database error: {e}")
        conn.close()
        return False
'''
    except sqlite3.IntegrityError:
        conn.close()
        return False'''
    
    

# Function to Verify Login
def verify_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    user = c.fetchone()
    
    conn.close()
    
    if user and bcrypt.checkpw(password.encode(), user[0].encode()):
    #if user and bcrypt.checkpw(password.encode(), user[0]):
        return True
    return False

# Initialize the table
create_user_table()
