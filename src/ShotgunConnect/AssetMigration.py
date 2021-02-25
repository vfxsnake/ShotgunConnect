from SgQuery import *

class AssetMigration():
    
    def __init__(self):
        self.Query = SGQuery()

    def MigrateAllAssets(self, SourceProjectId, DestinationProjectId,skipOmit=True):
        Filters = []
        if skipOmit:
            Filters = [SgFilter.SgStatusIsNot('omt'), 
            SgFilter.OperatorIfAnyOf([SgFilter.ShotgunAssetTypeIs('CHARACTER'), SgFilter.ShotgunAssetTypeIs('ENVIRONMENT')])]

        allAssets = self.Query.GetAllAsstes(SourceProjectId, Filters)        
        return allAssets    
    
    def switchName(self):
        data = self.readCsv()
        for element in data:
            pair = element.split(',')
            # print (pair)
            originalAsset =  self.Query.FindAssetByName(self.Query.GNG_ID, pair[0])
            originalAsset['code'] = pair[1]
            # print(originalAsset['code'], 'new name')
            # originalAsset['code'] = pair[1]
            # print(originalAsset['code'], 'new name')
            name = {'code':originalAsset['code']}
            updatedAsset = self.Query.Connection.sg.update('Asset', originalAsset['id'], name)
            print (updatedAsset)

    def readCsv(self):
        import csv
        data = []
        with open('src\ShotgunConnect\CambiosNombres.csv') as csv_file:
            for line in csv_file:
                data.append(line.rstrip('\n'))
        if data:
            return data


if __name__ == '__main__':

    test = AssetMigration()
    test.switchName()
    # AssetsData = test.MigrateAllAssets(test.Query.GGO_ID, test.Query.GNG_ID)
    # for element in AssetsData:
    #     newProject = {'id': 359, 'type': 'Project'}
        
    #     data = {'project': newProject, 'code': element['code'], 'sg_old_id': element['id'], 'task_template': element['task_template'], 'sg_asset_type': element['sg_asset_type']}
    #     print(data)

    #     assetExists = test.Query.FindAssetByName(data['project']['id'], data['code']) 
    #     if not assetExists:
            
    #         currentAssetCreated = SgCreateEntity.CreateAsset(test.Query.Connection.GetSgConnection(), data )
    #         print (data['code'],"created")
        
    #     else:
    #         print("asset exists")