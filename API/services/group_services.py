from connection import Connection

def formate(group):
    return {
        "id": group[0],
        "name": group[1]
    }

def get(id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT * FROM UserGroup WHERE id = %s"
        cursor.execute(query, (id,))

        group = cursor.fetchone()

        return {"ok": True, "group": formate(group)}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()

def create(group):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO UserGroup (name) VALUES (%s)"
        values = (group.name,)
        cursor.execute(query, values)

        conn.commit()

        id = cursor.lastrowid

        return {"ok": True, "msg": f"Created group with id: {id}", "id": id}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()