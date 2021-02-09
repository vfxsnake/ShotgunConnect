


class SgPlayListMakerConnection(object):

    def __init__(self):
        ''' Conects to Huevocartoon@shotgun usnign the playlist Maker script key'''

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
        

