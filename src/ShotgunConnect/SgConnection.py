
from SgFilterBuilder import SgFilterBuilder as SgFilter

class SgPlayListMakerConnection(object):

    def __init__(self):
        ''' Conects to Nuevocarotin @ shotgun usnign the playlist Maker script key'''

        from shotgun_api3 import shotgun
        SERVER_PATH = "https://hcpstudio.shotgunstudio.com"
        SCRIPT_NAME = 'PlayListMaker'
        SCRIPT_KEY = 'fqvnvll~s0jnzondjiTfnqkns'

        self.sg = shotgun.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    def GetSgConnection(self,):
        return self.sg

class SGQuery():

    def __init__(self):
        '''This module has all the functions to queri thrue shotgun python api 3
            is a collection of functions to retrive imformation from entities in shotgun
            uses the imports the filter module to facilitate the filtering typing

        '''
        ShotgunConnection = SgPlayListMakerConnection()
        self.sg = ShotgunConnection.GetSgConnection()

        self.UGC_ID = 159
        self.HEF_ID = 106
        self.GGO_ID = 161 #old version of gungo
        self.GNG_ID = 359 #gungo new project
    
    

    def GetAllTask(self, Project,Filters=None, Fields=None):
        ''' returns a list of tasks  spisify by project, filters and fields
            if no filter return all task from the project
            if no fields return the basic data  id, code, step, content
            Filter and Fields are  list, containing the filters or fields coma separated.
        '''

        if not Filters:
            Filters = [SgFilter.ProjectIs(Project)]
        
        if not Fields:
            Fields = ['id', 'code', 'step', 'content', 'task_assignees']
        
        Tasks = self.sg.find("Task", Filters, Fields)
        if Tasks:
            return Tasks

    def GetAllAsstes(self, Porject, Filters=None, Fields=None):
        '''
            returns a list of Assets from the spesified project, filters and fields.
            if no filter return all Assets from the project
            if no fields return the basic data  id, code, step, content
            Filter and Fields are  list, containing the filters or fields coma separated.
        '''
        if not Filters:
            Filters = [SgFilter.ProjectIs(Porject)]

        if not Fields:
            Fields = ['id', 'code', 'step', 'sg_asset_type']

        Assets = self.sg.find('Asset', Filters, Fields)
        return Assets

    

if __name__ == '__main__':
    # test examples for debugin porposes porposes
    # and examples of usages 
    Sg = SGQuery()
    Elements = Sg.GetAllAsstes(Sg.GGO_ID)


    for x,element in enumerate(Elements, 1):
        if x > 50:
            break
        taskFilter = [SgFilter.ProjectIs(Sg.GGO_ID), SgFilter.EntityIs(element['type'], element['id']), SgFilter.StepIs('ART', 13),
                     SgFilter.OperatorIfAnyOf([SgFilter.SgStatusIs('apr'), SgFilter.SgStatusIs('fin')])]
        tasks = Sg.GetAllTask(Sg.GGO_ID, taskFilter)
        print (element)
        if tasks:
            for item in tasks:
                print (item)



