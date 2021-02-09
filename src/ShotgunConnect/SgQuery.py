from SgFilterBuilder import SgFilterBuilder as SgFilter
from SgConnection import SgPlayListMakerConnection

class SGQuery(object):
    
    def __init__(self):
        '''This module has all the functions to queri thrue shotgun python api 3
            is a collection of functions to retrive imformation from entities in shotgun
            uses the imports the filter module to facilitate the filtering typing

        '''
        self.Connection = SgPlayListMakerConnection()
    
        self.UGC_ID = 159
        self.HEF_ID = 106
        self.GGO_ID = 161 #old version of gungo
        self.GNG_ID = 359 #gungo new project
        self.SandBox_ID = 227
    
    def __del__(self):
        self.Connection.sg._close_connection()
        
        print ("Removing SgQuery")

    def GetAllProjects(self):
        """Return the list of all projects in the shotgun site
           defualt field: 'id', 'name', 

        Returns:
            [type]: [description]
        """
        return self.Connection.sg.find('Project', [], ['name'])

    def GetAllTask(self, Project,Filters=None, Fields=None):
        """[Returns a list of all tasks matching the filters ]

        Args:
            Project ([int]): [Id of the project in shotgun]
            Filters ([list], optional): [list of filters, for simplicity use the SGFilterBuilder to create this list]. Defaults to None.
            Fields ([list], optional): [specify contennts of the query, adds aditional keys to the returning didctionaries]. Defaults to None.
                default fieds are 'id', 'code', 'step', 'content', 'task_assignees'
        Returns:
            [list of dictionaries]: [list of found Tansks in a form of dictionaries.]
        """

        if not Filters:
            Filters = [SgFilter.ProjectIs(Project)]
        
        if not Fields:
            Fields = ['id', 'code', 'step', 'content', 'task_assignees']
        
        Tasks = self.Connection.sg.find("Task", Filters, Fields)
        if Tasks:
            return Tasks

    def GetAllAsstes(self, Project, Filters=None, Fields=None):
        """[Return list of all assets matching the specify query]

        Args:
            Project (int): [shot id from the project]
            Filters ([list], optional): [list of filters created by SgFilterBuilder]. Defaults to None.
            Fields ([list], optional): [list of keys to be returned as part of the dictionaries from the query]. Defaults to None.
                default fields are 'id', 'code', 'step', 'sg_asset_type'
        Returns:
            [list]: [List of dictionaries of all assets queried if match]
        """
        if not Filters:
            Filters = [SgFilter.ProjectIs(Project)]
        else:
            Filters.append(SgFilter.ProjectIs(Project))

        if not Fields:
            Fields = ['id', 'code', 'step', 'sg_asset_type', 'project']

        Assets = self.Connection.sg.find('Asset', Filters, Fields)
        return Assets

    def GetAllDigitalMedia(self, Project, Filters=None, Fields=None):
        """[query all digital medira from the project specified]

        Args:
            Project (int): [shotgun Id from the project]
            Filters ([list], optional): [list of filters to be applied.]. Defaults to None.
            Fields ([list], optional): [list of key desired as part of the dictionary queries]. Defaults to None.
                default fields are 'id', 'code', 'entity', 'sg_task', 'sg_status_list'

        Returns:
            [lit]: [list of dictionaries matching the query]
        """
        if not Filters:
            Filters = [SgFilter.ProjectIs(Project)]
        
        else:
            Filters.append(SgFilter.ProjectIs(Project))

        
        if not Fields:
            Fields = ['id', 'code', 'entity', 'sg_task', 'sg_status_list']

        
        DM = self.Connection.sg.find('Version', Filters, Fields)
        return DM

    def GetAllUsers(self):
        pass

    def FindAssetByName(self, ProjectId, AssetName):
        data = [SgFilter.CodeIs(AssetName), SgFilter.ProjectIs(ProjectId)]
        return self.Connection.sg.find_one('Asset', data, [])


if __name__ == '__main__':
    # test examples for debugin porposes porposes
    # and examples of usages 
    
    print ('loading SgQuery')
    Sg = SGQuery()
    # print (Sg.GetAllProjects())
    test  = Sg.GetAllAsstes(Sg.SandBox_ID)
    # print (test[0])
    
    print (Sg.FindAssetByName(Sg.SandBox_ID, 'apicreatedAsset01') )


    # SgCreateEntity.CreateAsset(Sg.Connection.GetSgConnection(), data )


    # tempFilters = [SgFilter.EntityIs("Asset", 2400), SgFilter.OperatorIfAnyOf([SgFilter.SgStatusIs('apr'), SgFilter.SgStatusIs('fin')]) ]
    
    # print('make query')
    # Elements = Sg.GetAllProjects()

    # for x,element in enumerate(Elements):
    #     print (x, element)