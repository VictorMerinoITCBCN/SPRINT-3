from connection import Connection

def register_user(user, role_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO User (name, lastName, email, groupID, roleID) VALUES (%s, %s, %s, %s, %s)"
        values = (user.name, user.last_name, user.email, user.group_id, role_id)

        cursor.execute(query, values)
        conn.commit()

        id = cursor.lastrowid

        return {"ok": True, "msg": f"User {user.name} {user.last_name} registed", "id": id}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()