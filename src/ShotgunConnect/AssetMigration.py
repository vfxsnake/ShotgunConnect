from SgQuery import *
from SgFilterBuilder import *

class AssetMigration():
    
    def __init__(self):
        self.Query = SGQuery()

    def MigrateAllAssets(self, skipOmit=True):
        Filters = []
        if skipOmit:
            Filters = [SgFilter.SgStatusIsNot('omt'), 
            SgFilter.OperatorIfAnyOf([SgFilter.ShotgunAssetTypeIs('CHARACTER'), SgFilter.ShotgunAssetTypeIs('ENVIRONMENT')])]

        allAssets = self.Query.GetAllAsstes(self.Query.GGO_ID, Filters)
        
        return allAssets    

if __name__ == '__main__':

    test = AssetMigration()

    AssetsData = test.MigrateAllAssets()
    for element in AssetsData:
        print (element)
        