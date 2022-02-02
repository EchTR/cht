import sqlite3
def get_posts(mode, user=None):
    SQL_PATH = "C://Users//echtr//Desktop//cht//database//db_posts.db"
    POSTS = []
    connect = sqlite3.connect(SQL_PATH)
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM posts")
    rows = cursor.fetchall()
    connect.close()
    if user == None:
        if mode == "new":
            rows = rows[::-1]
            for i in range(len(rows)):
                POSTS.append(rows[i])

        elif mode == "top":
            rows.sort(key=lambda x:x[3])
            for i in range(len(rows)):
                POSTS.append(rows[i])
    else:
        rows = rows[::-1]
        for i in rows:
            if i[5].lower() == user.lower():
                POSTS.append(i)

    return POSTS
if __name__ == "__main__":
    print(get_posts("top",user="echtr"))
    input()