# 0 - nickname / 1- email / 2- password
import sqlite3
def get():
    SQL_PATH = "C://Users//echtr//Desktop//cht//database//db_users.db"
    connect = sqlite3.connect(SQL_PATH)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    connect.close()
    return rows

def post(username, email, password):
    SQL_PATH = "C://Users//echtr//Desktop//cht//database//db_users.db"
    connect = sqlite3.connect(SQL_PATH)
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO users VALUES
    ("{username}", "{email}", "{password}")""")
    connect.commit()
    connect.close()
if __name__ == "__main__":
    post("efe içke", "my mail", "123")
    input()