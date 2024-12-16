from connection import Connection

def create_subject(subject):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = "INSERT INTO Subject (name, room, teacherID, weekday, startTime, endTime) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (subject.name, subject.room, subject.teacher_id, subject.weekday, subject.start_time, subject.end_time)

        cursor.execute(query, values)
        conn.commit()

        return {"ok": True, "msg": "Subject created"}
    except Exception as error:
        return {"ok": False, "error": f"Error: {error}"}
    finally:
        Connection.close()