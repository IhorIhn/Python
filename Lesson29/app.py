import psycopg2

# Параметри підключення до бази
DB_HOST = "localhost"
DB_NAME = "testdb"
DB_USER = "user"
DB_PASS = "pass"

def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id", (name, age))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

def update_user(user_id, name=None, age=None):
    conn = get_connection()
    cur = conn.cursor()
    if name:
        cur.execute("UPDATE users SET name=%s WHERE id=%s", (name, user_id))
    if age:
        cur.execute("UPDATE users SET age=%s WHERE id=%s", (age, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def select_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

if __name__ == "__main__":
    create_table()
    print("Current users:", select_users())
    uid = insert_user("Alice", 25)
    print("After insert:", select_users())
    update_user(uid, age=26)
    print("After update:", select_users())
    delete_user(uid)
    print("After delete:", select_users())
