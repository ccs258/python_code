import MySQLdb
'''https://github.com/mingli95/python-operational-monitoring'''
class Db(object):
    def __init__(self,sql):
        self.sql = sql
        self.db = MySQLdb.connect("192.168.1.180",'liming','sbdscaaas123','yunwei')
        self.cursor = self.db.cursor()

    def Insert(self):
        try:
            self.cursor.execute(self.sql)
            self.db.commit()

        except:
            self.db.rollback()
        self.cursor.close()
        self.db.close()


    def update(self):
        try:
            self.cursor.execute(self.sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.cursor.close()
        self.db.close()

    def Select(self):
        self.cursor.execute(self.sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return results

    def Create(self):
        self.cursor.execute(self.sql)
        self.db.commit()
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    data = """NSERT INTO yuwei.systeminfo (netname,address,hostname)
        VALUES ('eno111','192.168.1.190','localhost.localhost')"""
    Db(data).Insert()