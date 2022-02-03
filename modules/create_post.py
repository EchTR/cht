import sqlite3
def create_post(post_date, post_title, post_text, post_author):
    SQL_PATH = "C://Users//echtr//Desktop//cht//database//db_posts.db"
    connect = sqlite3.connect(SQL_PATH)
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO posts VALUES
    ("{post_date}", "{post_title}", "{post_text}", 0, 0, "{post_author}", 0)""")
    connect.commit()
    connect.close()
