from connection import Connection

def get_by_student_and_subject(student_id, subject_id):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            *
        FROM Assistance
        WHERE studentID = %s
        AND subjectID = %s
        """
        values = (student_id, subject_id)
        cursor.execute(query, values)
        assistance = cursor.fetchone()

        return {"ok": True, "assitance": assistance}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()

def create(assistance):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO Assistance (studentID, teacherID, subjectID, assistance_status) VALUES (%s, %s, %s, %s)"
        values = (
            assistance.student_id,
            assistance.teacher_id,
            assistance.subject_id,
            assistance.assistance_status
        )

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": f"Assistance created."}
    except Exception as e:
        return {"ok": False, "error": f"Error: {e}"}
    finally:
        Connection.close()