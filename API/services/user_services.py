from connection import Connection

def formate_user(user):
    return {
        "id": user[0],
        "name": user[1],
        "last_name": user[2],
        "email": user[3]
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
            "email": subject[6],
        },
        "weekday": subject[7],
        "start_time": subject[8],
        "end_time": subject[9]
    }

def formate_subject_min(subject):
    return {
        "id": subject[0],
        "name": subject[1],
        "room": subject[2],
        "weekday": subject[3],
        "start_time": subject[4],
        "end_time": subject[5]
    }

def formate_assistance(assistance):
    return {
        "status": assistance[0],
        "date": assistance[1],
        "subject": {
            "id": assistance[2],
            "name": assistance[3],
            "room": assistance[4]
        }
    }

def get_schedule(user_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT 
            s.id,
            s.name,
            s.room,
            t.id,
            t.name,
            t.lastName,
            t.email,
            s.weekday,
            s.startTime,
            s.endTime
        FROM UserSubject
        JOIN Subject s ON subjectID = s.id 
        JOIN User t ON s.teacherID = t.id
        WHERE userID = %s
        ORDER BY s.weekday, s.startTime
        """
        values = (user_id, )

        cursor.execute(query, values)
        
        subjects = cursor.fetchall()
        formated_subjects = [formate_subject(subject) for subject in subjects]

        monday = [subject for subject in formated_subjects if subject["weekday"] == 0]
        tuesday = [subject for subject in formated_subjects if subject["weekday"] == 1]
        wednesday = [subject for subject in formated_subjects if subject["weekday"] == 2]
        thursday = [subject for subject in formated_subjects if subject["weekday"] == 3]
        friday = [subject for subject in formated_subjects if subject["weekday"] == 4]

        schedule = {
            "monday": monday,
            "tuesday": tuesday,
            "wednesday": wednesday,
            "thursday": thursday,
            "friday": friday
        }

        return {"ok": True, "schedule": schedule}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def get_assistances(user_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            a.assistance_status,
            a.date,
            s.id,
            s.name,
            s.room
        FROM Assistance as a
        JOIN Subject s ON s.id = a.subjectID
        WHERE
        a.studentID = %s 
        """
        values = (user_id, )

        cursor.execute(query, values)

        assistances = cursor.fetchall()

        return {"ok":  True, "assistances": [formate_assistance(a) for a in assistances]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def get_users():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            id,
            name,
            lastName,
            email
        FROM User
        WHERE roleID = 1
        """

        cursor.execute(query)

        users = cursor.fetchall()

        return {"ok": True, "users": [formate_user(user) for user in users]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()

def get_subjects():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            id,
            name,
            room,
            weekday,
            startTime,
            endTime
        FROM Subject
        """

        cursor.execute(query)

        subjects = cursor.fetchall()

        return {"ok": True, "subjects": [formate_subject_min(subject) for subject in subjects]}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()