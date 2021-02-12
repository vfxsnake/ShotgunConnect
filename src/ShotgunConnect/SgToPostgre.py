import psycopg2 
import json

class ShotgunToPostgreConnection(object):
    def __init__(self):
        # self.Connection = psycopg2.connect(host='localhost', database='sgtest',user ='shotgundb', password='Huevo1234#')
        self.cursor = None
        # self.cursor =  self.Connection.cursor()
        print("conection succes")

    def CloseConnection(self):
        self.Connection.close()
    
    def CreateTable(self, TableName, ColumnNamesList):
        ColumnNameString = ' JSON UNIQUE Constraint, '.join(ColumnNamesList)
        

        # self.DropTableIfExists('assets')
        NewTable = "CREATE TABLE assets (id serial PRIMARY KEY, {0}".format(ColumnNameString)
        print (NewTable)
        # self.cursor.execute(NewTable)
        # self.Connection.commit()
        # print ('New table commit')

    def InserDataToTable(self, assets, Datata):
        IsertData = None
        self.cursor()

    def DropDataBase(self):
        pass
    
    def DropTableIfExists(self, TableName):
        command = "DROP TABLE IF EXISTS {0}".format(TableName)
        self.cursor.execute(command) 
            

if __name__ == '__main__':
    # test = ShotgunToPostgreConnection()
    # test.CreateTable()
    from SgQuery import *

    query = SGQuery()
    postgresBridge = ShotgunToPostgreConnection()

    AllAssets = query.GetAllAsstes(query.GGO_ID, AllFields=True)

    Asset = AllAssets[0]
    keyList = [x for x in Asset]
    # print (keyList)

    postgresBridge.CreateTable('asset', keyList)

    

