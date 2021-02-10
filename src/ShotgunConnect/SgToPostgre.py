import psycopg2 

class PostgreConnection(object):
    def __init__(self) -> None:
        self.Connection = psycopg2.connect(host='localhost', database='sgtest',user ='shotgundb', password='Huevo1234#')

        cursor =  self.Connection.cursor()

        print('PostgreSQL version:')
        cursor.execute('Select version()')

        db_version = cursor.fetchone()
        print(db_version)

        cursor.close()


if __name__ == '__main__':
    test = PostgreConnection()
