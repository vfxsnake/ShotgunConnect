import psycopg2 
import json

class ShotgunToPostgreConnection(object):
    def __init__(self):
        self.Connection = psycopg2.connect(host='localhost', database='sgtest',user ='shotgundb', password='Huevo1234#')
        # self.cursor = None
        self.cursor =  self.Connection.cursor()
        print("conection succes")

    def CloseConnection(self):
        self.Connection.close()
    
    def CreateTable(self, TableName):

        self.DropTableIfExists(TableName)
        NewTable = "CREATE TABLE {0} (id integer PRIMARY KEY)".format(TableName)
        table = self.cursor.execute(NewTable)
        self.Connection.commit()
        print ('New table commit', table)

    def AddColumnToTable(self,TableName, ColumnName, DataType):

        NewColumn = "ALTER TABLE {0} ADD COLUMN {1} {2}".format(TableName, ColumnName, DataType)
       
        try:
            self.cursor.execute(NewColumn)
            print (NewColumn)
            self.cursor.commit()
        except:
            pass

    def AddMultipleColumnsToTable(self, TableName, ColumnNameList, DataType):
        for element in ColumnNameList:
            self.AddColumnToTable(TableName, element, DataType)

    def InserDataToTable(self, assets, Datata):
        IsertData = None
        self.cursor()

    def DropDataBase(self):
        pass
    
    def DropTableIfExists(self, TableName):
        command = "DROP TABLE IF EXISTS {0}".format(TableName)
        self.cursor.execute(command) 
            

if __name__ == '__main__':

    from SgQuery import *

    query = SGQuery()
    postgresBridge = ShotgunToPostgreConnection()

    AllAssets = query.GetAllAsstes(query.GGO_ID, AllFields=True)

    Asset = AllAssets[0]
    keyList = [x for x in Asset]
    # print (keyList)

    postgresBridge.CreateTable('assets')
    postgresBridge.AddMultipleColumnsToTable('assets', keyList, "JSON")


    

