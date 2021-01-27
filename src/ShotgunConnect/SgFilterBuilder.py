class SgFilterBuilder(object):
    ''' return the desire filter in the correct sintax an format for shotgun Queries'''
    
    @staticmethod
    def ProjectIs(ProjectID):
        '''returns the project filter for queri
            accepts only ints for project ID
        '''
        return ['project', 'is', {'type': 'Project', 'id': ProjectID}]

    @staticmethod
    def StepIs(stepName, stepId):
        '''return the step filter correctly formated
            accepts stepNmaes "ART, MODELING, RIG, PREVIZ", etc 
        '''
        return ['step', 'is',  {'id': stepId, 'name': stepName, 'type': 'Step'}]

    @staticmethod
    def EntityIs(EntityType, EntityId):
        '''returns Entity filter correcty formated for filtering entyti
            Entity is the linked to column and Can Be "ASSET", "SHOT", etc
        '''
        return ['entity', 'is',  {'type': EntityType, 'id':EntityId}]  
    @staticmethod
    def ShotgunAssetTypeIs(ShotgunAssetType):
        ''' acepts "CHARACTER", "ENVIRONMENT", "PROP"
            return the filter to shotgun asset Type
        '''
        return ['sg_asset_type', 'is', ShotgunAssetType]

    @staticmethod
    def SgStatusIs(Status):
        ''' 
            return the correct format filter for sg_status _list
            accepts "rdy, ip, app, rtk,, apr, dlvr, omt, rev, fin, opn" etc
        '''
        return ['sg_status_list', 'is', Status]

    @staticmethod
    def OperatorIfAnyOf(FilterListToApply):
        return {'filter_operator': 'any', 'filters': FilterListToApply }
