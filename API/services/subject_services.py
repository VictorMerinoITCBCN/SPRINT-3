from connection import Connection
from services import users_services

def formate(subject):
    return {
        "id": subject[0],
        "name": subject[1],
        "room": subject[2],
        "weekday": subject[3],
        "start_time": subject[4],
        "end_time": subject[5],
        "teacher" : users_services.formate(subject[6:15])
    }

def get(id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            Subject.id,
            Subject.name,
            Subject.room,
            Subject.weekday,
            Subject.startTime,
            Subject.endTime,
            User.id,
            User.name,
            User.lastName,
            User.email,
            UserGroup.*,
            UserRole.*
        FROM Subject
        JOIN User ON teacherID = User.id
        JOIN UserGroup ON User.groupID = UserGroup.id
        JOIN UserRole ON User.roleID = UserRole.id
        WHERE Subject.id = %s
        """

        cursor.execute(query, (id,))
        subject = cursor.fetchone()

        return {"ok": True, "subject": formate(subject)}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()

def create(subject):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        INSERT INTO Subject (name, room, teacherID, weekday, startTime, endTime)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            subject.name,
            subject.room,
            subject.teacher_id,
            subject.weekday,
            subject.start_time,
            subject.end_time
            )
        
        cursor.execute(query, values)
        conn.commit()

        id = cursor.lastrowid

        return {"ok":True, "msg": f"Created subject with id: {id}"}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()

def matriculate(user_id, subject_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO UserSubject (userID, subjectID) VALUES (%s, %s)"
        values = (user_id, subject_id)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": f"Usuari amb id: {user_id} matriculat"}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()

def get_users(id):
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
            UserRole.*,
            Assistance.assistance_status,
            Assistance.date
        FROM UserSubject
        JOIN User ON userID = User.id
        JOIN UserGroup ON User.groupID = UserGroup.id
        JOIN UserRole ON User.roleID = UserRole.id
        JOIN Assistance ON userId = studentID 
        AND UserSubject.subjectID = Assistance.subjectID
        WHERE UserSubject.subjectID = %s
        """
        cursor.execute(query, (id,))

        users = cursor.fetchall()

        return {"ok": True, "users": [users_services.formate_assitance(user) for user in users]}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()