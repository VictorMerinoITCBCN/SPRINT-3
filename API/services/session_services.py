from connection import Connection
import uuid

def formate_user(user):
    return {
        "id": user[0],
        "name": user[1],
        "last_name": user[2],
        "email": user[3],
        "group": {"id": user[4], "name": user[5]},
        "role": {"id": user[6], "name": user[7]},
        "token": user[8]
    }

def register(role_id, user):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        INSERT INTO User 
            (name, lastName, email, hashedPassword, token, groupID, roleID)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s)
        """
        token = str(uuid.uuid4())
        values = (user.name, user.last_name, user.email, user.password, token, user.group_id, role_id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "User created", "token": token}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def login(user, password, context):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "SELECT hashedPassword FROM User WHERE email = %s"
        cursor.execute(query, (user, ))
        hashed_pwd = cursor.fetchone()


        if not hashed_pwd:
            return {"ok": False, "error": f"The user {user} do not exist"}
        
        correct_pwd = context.verify(password, hashed_pwd[0])

        if correct_pwd:
            query = "SELECT token FROM User WHERE email = %s AND hashedPassword= %s"
            values = (user, hashed_pwd[0])

            cursor.execute(query, values)
            token = cursor.fetchone()

            return {"ok": True, "token": token[0]}
        else:
            return {"ok": False, "error": "Incorrect password"}


    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()
    
def get_user(token):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT  
            u.id,
            u.name,
            u.lastName,
            u.email,
            g.id,
            g.name,
            r.id,
            r.name,
            u.token
        FROM User u
        JOIN UserGroup g ON g.id = groupID
        JOIN UserRole r ON r.id = roleID
        WHERE token = %s
        """

        cursor.execute(query, (token, ))
        user = cursor.fetchone()

        return {"ok": True, "user": formate_user(user)}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def validate_role(token, valid_role_ids):
    user = get_user(token)
    if not user["ok"]:
        return  {"ok": False, "error": "User not found"}
    role_id = user["user"]["role"]["id"]
    if role_id not in valid_role_ids:
        return {"ok": False, "error": "User not allowed"}
    return user