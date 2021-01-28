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
        '''
            Entity is the column 'Link' in shotgun web, could be "ASSET", "SHOT",etc
            Accepts all entity types, the Entity id is requiered
        '''
        return ['entity', 'is',  {'type': EntityType, 'id':EntityId}]  

    @staticmethod
    def SgTaskIs(TaskId):
        '''
            accepts only Task ids, because this field
            is restricted to task by shotgun.
            returs the query correctly formated
            
        '''
        return ['sg_task', 'is', {'type':'Task', 'id': TaskId}]
        
        

    @staticmethod
    def ShotgunAssetTypeIs(ShotgunAssetType):
        ''' 
            acepts "CHARACTER", "ENVIRONMENT", "PROP"

        '''
        return ['sg_asset_type', 'is', ShotgunAssetType]

    @staticmethod
    def SgStatusIs(Status):
        ''' 
            accepts "rdy, ip, app, rtk,, apr, dlvr, omt, rev, fin, opn" etc
            
        '''
        return ['sg_status_list', 'is', Status]

    @staticmethod
    def OperatorIfAnyOf(FilterListToApply):
        '''
            returns a dictionary containing the filter operator any, helps to include
            two or more filters of the sem tipe, ex:
            OperatorIfAnyof(sgFiltarBuilder.SgStatusIs('Apr'), sgFiltarBuilder.SgStatusIs('ip'), sgFiltarBuilder.SgStatusIs('sub'))
            this filter operartor helps to find statuse in this 3 stages.
        '''
        return {'filter_operator': 'any', 'filters': FilterListToApply }
