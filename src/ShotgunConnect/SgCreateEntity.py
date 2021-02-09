class SgCreateEntity(object):
       
    @staticmethod
    def CreateVersion(Connection , Project, VersionCode):
        pass
    
    @staticmethod
    def CreateAsset(Connection, ItemData):
        """[Creates an asset from the imput data]

        Args:
            Connection ([object, sg instance]): [the connection instance to shotgun site api]
            ItemData (dictionary): [requeres a dictionary containing at lists 2 keys:
            {'project': {type: 'Project', 'id': intProjectId}, 'code': 'AssetName'} ]
            
        return: 
            if succes, returns the dictionary from created asset.
        """
        
        return Connection.create('Asset', ItemData)
        