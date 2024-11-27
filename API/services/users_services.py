from connection import Connection


def formate(user):
    return {
        "id": user[0],
        "name": user[1],
        "last_name": user[2],
        "email": user[3],
        "group": {"id": user[4], "name": user[5]},
        "role": {"id": user[6], "name": user[7]}
    }

def formate_assitance(user):
    return {
        "id": user[0],
        "name": user[1],
        "last_name": user[2],
        "email": user[3],
        "group": {"id": user[4], "name": user[5]},
        "role": {"id": user[6], "name": user[7]},
        "assistance": {"value": user[8], "date": user[9]}
    }

def get(id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT 
            User.id,
            User.name,
            User.lastName,
            User.email,
            UserGroup.*,
            UserRole.*
        FROM User
        JOIN UserGroup ON groupID = UserGroup.id
        JOIN UserRole ON roleID = UserRole.id
        WHERE User.id = %s
        """
        
        cursor.execute(query, (id,))

        user = cursor.fetchone()

        return {"ok": True, "user": formate(user)}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()

def create(user):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO User (name, lastName, email, groupID, roleID) values (%s, %s, %s, %s, %s)"
        values = (user.name, user.last_name, user.email, user.group_id, user.role_id)

        cursor.execute(query, values)
        conn.commit()

        id = cursor.lastrowid

        return {"ok": True, "msg": f"Created user with id: {id}", "id": id}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()