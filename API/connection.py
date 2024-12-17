from mysql import connector

class Connection:

    _connection = None

    @staticmethod
    def connect():
        try:
            Connection._connection = connector.connect(
                host="localhost",
                port="3306",
                user="admin",
                password="super",
                database="schoolControll"
            )
        except Exception as e:
            print(f"Error connectiong to the DB: {e}")

    @staticmethod
    def get():
        if not Connection._connection: Connection.connect()

        return Connection._connection
    
    @staticmethod
    def close():
        if Connection._connection: 
            Connection._connection.close()
            Connection._connection = None