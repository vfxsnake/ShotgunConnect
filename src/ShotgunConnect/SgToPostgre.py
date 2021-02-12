import psycopg2 

class ShotgunToPostgreConnection(object):
    def __init__(self):
        self.Connection = psycopg2.connect(host='localhost', database='sgtest',user ='shotgundb', password='Huevo1234#')

        self.cursor =  self.Connection.cursor()
        print("conection succes")

    def CloseConnection(self):
        self.CreateTable.close()
    
    def CreateTable(self, dictionaryData=None):
        
        self.DropTableIExists('assets')
        NewTable = "CREATE TABLE assets(id serial PRIMARY KEY, name varchar(100), code varchar(100))"
        self.cursor.execute(NewTable)
        self.Connection.commit()
        print ('New table commit')


    def InserDataToTable(self, TableName, Datata):
        pass

    def DropDataBase(self):
        pass
    
    def DropTableIExists(self, TableName):
        command = "DROP TABLE IF EXISTS {0}".format(TableName)
        self.cursor.execute(command) 



if __name__ == '__main__':
    test = ShotgunToPostgreConnection()
    test.CreateTable()
