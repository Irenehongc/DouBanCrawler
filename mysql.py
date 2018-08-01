# __*__coding:utf-8 __*__
import pymysql


class MyConnection:
    username = "root"
    password = ""
    connection = None
    cursor = None
    host = "127.0.0.1"
    dbname = "DouBanMovieReview"

    def __init__(self):
        self.connection = pymysql.connect(self.host, self.username, self.password, self.dbname,
                                          cursorclass=pymysql.cursors.DictCursor,
                                          use_unicode=True, charset="utf8mb4")
        self.cursor = self.connection.cursor()
        pass

    def execute(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()
        pass

    def get_infor(self):
        print(self.connection.db)
        pass

    def get_result(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.connection.close()
        pass
