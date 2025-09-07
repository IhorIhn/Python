from app import get_connection, insert_user, update_user, delete_user, select_users, create_table


def test_connection():
    conn = get_connection()
    assert conn is not None
    conn.close()


def test_crud():
    create_table()

    # Insert
    uid = insert_user("Bob", 30)
    users = select_users()
    assert any(u[0] == uid for u in users)

    # Update
    update_user(uid, age=31)
    users = select_users()
    assert any(u[0] == uid and u[2] == 31 for u in users)

    # Delete
    delete_user(uid)
    users = select_users()
    assert all(u[0] != uid for u in users)
