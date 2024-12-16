from connection import Connection

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

def get_assistances(user_id, date):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            *
        FROM Assistance as a
        JOIN Subject s ON s.id = a.subjectID
        WHERE
        a.studentID = %s 
        AND DATE(a.date) = %s
        """
        values = (user_id, date)

        cursor.execute(query, values)

        assistances = cursor.fetchall()

        return {"ok":  True, "assistances": assistances}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()