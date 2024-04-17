import sqlite3


class DataBase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self):
        with self.conn:
            self.cur.execute("CREATE TABLE IF NOT EXISTS passwords"
                             "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                             "Service varchar(50),"
                             "Password varchar(50)"
                             ")")
            return self.conn.commit()

    def insert_password(self, password, service):
        with self.conn:
            self.cur.execute("INSERT INTO passwords (Password, Service) VALUES (?, ?)",  (password, service))
            return self.conn.commit()

    def get_password(self):
        with self.conn:
            return self.cur.execute('SELECT * FROM passwords').fetchall()

