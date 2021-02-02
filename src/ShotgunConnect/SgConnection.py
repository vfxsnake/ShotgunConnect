
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

    def __del__(self):
        '''
        when the class is destroyed, 
        closes the contenctionto shotgun
        '''
        print (' Removing SgPlayListMakerConnection')
        self.sg._close_connection()

class SGQuery():

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
    
    def __del__(self):
        self.Connection.sg._close_connection()
        
        print ("Removing SgQuery")


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
        
        Tasks = self.Connection.sg.find("Task", Filters, Fields)
        if Tasks:
            return Tasks

    def GetAllAsstes(self, Project, Filters=None, Fields=None):
        '''
            returns a list of Assets from the spesified project, filters and fields.
            if no filter return all Assets from the project
            if no fields return the basic data  id, code, step, content
            Filter and Fields are  list, containing the filters or fields coma separated.
        '''
        if not Filters:
            Filters = [SgFilter.ProjectIs(Project)]
        else:
            Filters.append(SgFilter.ProjectIs(Project))

        if not Fields:
            Fields = ['id', 'code', 'step', 'sg_asset_type']

        Assets = self.Connection.sg.find('Asset', Filters, Fields)
        return Assets

    def GetAllDigitalMedia(self, Project, Filters=None, Fields=None):
        '''
            return a list of all digital media (Versions) from the project and fields specified
            if no Filter or fields spesified, defaut parameteres are set in place.
        '''
        if not Filters:
            Filters = [SgFilter.ProjectIs(Project)]
        
        else:
            Filters.append(SgFilter.ProjectIs(Project))

        
        if not Fields:
            Fields = ['id', 'code', 'entity', 'sg_task', 'sg_status_list']

        
        DM = self.Connection.sg.find('Version', Filters, Fields)
        return DM

class SgTransferFiles():
    def __init__(self):
        self.Connection = SgPlayListMakerConnection()
        
    def GetVersion(self, VerisionQuery):
        pass
    
    def UploadToVersion(self, VersionQuery, FileToUpload):
        pass
        


class SgCreateEntity():
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def CreateVersion(Project, VersionCode):
        pass

class UpdateStatuses():
    def __init__(self) -> None:
        pass
    
    @staticmethod    
    def UpdateStatus(self, args):
        pass
    
    @staticmethod
    def Register(self, args):
        pass

if __name__ == '__main__':
    # test examples for debugin porposes porposes
    # and examples of usages 
    
    print ('loading SgQuery')
    Sg = SGQuery()

    tempFilters = [SgFilter.EntityIs("Asset", 2400), SgFilter.OperatorIfAnyOf([SgFilter.SgStatusIs('apr'), SgFilter.SgStatusIs('fin')]) ]
    
    print('make query')
    Elements = Sg.GetAllDigitalMedia(Sg.GGO_ID)

    print (len(Elements))

    # for x,element in enumerate(Elements):
    #     print (x, element)

    # Published Files , published file dependicies para hacer el registro