from connection import Connection

def formate_assistance(assistance):
    return {
        "id": assistance[10],
        "status": assistance[11],
        "date": assistance[12],
        "student" : {
            "id": assistance[0],
            "name": assistance[1],
            "last_name": assistance[2],
            "email": assistance[3]
        },
        "subject": {
            "id": assistance[4],
            "name": assistance[5]
        },
        "teacher": {
            "id": assistance[6],
            "name": assistance[7],
            "last_name": assistance[8],
            "email": assistance[9]
        },
    }

def formate_subject(subject):
    return {
        "id": subject[0],
        "name": subject[1],
        "room": subject[2],
        "teacher": {
            "id": subject[3],
            "name": subject[4],
            "last_name": subject[5],
            "email": subject[6]
        },
        "weekday": subject[7],
        "start_time": subject[8],
        "ent_time": subject[9]
    }

def get_subjects(teacher_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            Subject.id,
            Subject.name,
            Subject.room,
            User.id,
            User.name,
            User.lastName,
            User.email,
            Subject.weekday,
            Subject.startTime,
            Subject.endTime
        FROM Subject 
        JOIN User ON User.id = teacherID
        WHERE teacherID = %s
        """
        cursor.execute(query, (teacher_id, ))

        subjects = cursor.fetchall()

        return {"ok": True, "subjects": [formate_subject(subject) for subject in subjects]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
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

        return {"ok": True, "msg": "User matriculated"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def read_assistances(subject_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT 
            u.id,
            u.name,
            u.lastName,
            u.email,
            s.id,
            s.name,
            t.id,
            t.name,
            t.lastName,
            t.email,
            COALESCE(a.id, 0) AS assistance_id,
            COALESCE(a.assistance_status, 'absent') AS assistance_status,
            a.date AS assistance_date
        FROM 
            UserSubject us
        INNER JOIN 
            User u ON us.userID = u.id
        INNER JOIN 
            Subject s ON us.subjectID = s.id
        INNER JOIN
            User t ON s.teacherID = t.id
        LEFT JOIN 
            Assistance a ON u.id = a.studentID AND s.id = a.subjectID
        WHERE 
            s.id = %s
        """

        cursor.execute(query, (subject_id, ))

        assistances = cursor.fetchall()

        return {"ok": True, "assistances": [formate_assistance(a) for a in assistances]}

    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def create_assistance(assistance):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        INSERT INTO Assistance 
            (studentID, subjectID, assistance_status)
        VALUES (%s, %s, %s)
        """
        values = (
            assistance.student_id,
            assistance.subject_id,
            assistance.assistance_status
        )

        cursor.execute(query, values)
        conn.commit()

        id = cursor.lastrowid

        return {"ok": True, "msg": f"Created assistance with id: {id}", "id": id}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def modify_assistance(id,assistance):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        UPDATE Assistance
            SET studentID = %s,
            subjectID = %s,
            assistance_status = %s
        WHERE id = %s
        """
        values = (
            assistance.student_id,
            assistance.subject_id,
            assistance.assistance_status,
            id
        )

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Assistance modified"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()