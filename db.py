import mysql.connector

class MySQLConnection:
    def __init__(self, host, user, password, database) -> None:
        self.db = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    def get_all(self):
        self.cursor.execute("SELECT * FROM articles")
        res = self.cursor.fetchall()
        return [{"id": article[0], "title": article[1], "content": article[2]} for article in res]

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM articles WHERE id = {id}")
        res = self.cursor.fetchall()
        return [{"id": article[0], "title": article[1], "content": article[2]} for article in res]

    def add_article(self, article):
        self.cursor.execute(f"INSERT INTO articles (title, content) VALUES ('{article['title']}', '{article['content']}')")
        self.db.commit()

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM articles WHERE id = {id}")
        self.db.commit()

    def update(self, article):
        self.cursor.execute(f"UPDATE articles SET title = '{article['title']}', content = '{article['content']}' WHERE id = {article['id']}")
        self.db.commit()