'''
Created on Jun 6, 2012

@author: Anne Jan Elsinga
'''

from collections import namedtuple

class MediaLibrary:
    TVitem = namedtuple("TVitem", 'showtitle synopsis title summary duration season episode viewcount')
    MovieItem = namedtuple ("MovieItem", 'title summary')
    ClientItem = namedtuple ("ClientItem", 'name host address port')
    mediaplayer=""
    mediaplayerprotocol=""
    # duration in sec
    def __init__ (self):
        self.mediaplayer="Reference player"
        self.mediaplayerprotocl = "reference"
    
    def connect (self, servername):

        print "Connect to server " + servername
        ## acties om te connecten met een mediaplayer
        
    def info (self):
        print "Current player object: " + self.mediaplayer
        print "Current player protocol: " + self.mediaplayerprotocol
 
        # medialibrary related
    def getLatestMovies (self, numofitems, unwatched):
        print "latest movies"
        return "empty list"
    
    def getLatestTVShows (self,numofitems, unwatched):
        print "latest tv shows"
        return "empty list"
    
    def getLatestMusic (self,numofitems, unlistened):
        print "latest music"
        return "empty list"

