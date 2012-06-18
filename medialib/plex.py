'''
Created on Jun 6, 2012

@author: Anne Jan Elsinga
'''


from medialib import MediaLibrary
from elementtree import ElementTree
from urllib import urlopen
 
#TODO: Implement capabilities function 

class PlexMediaLibrary(MediaLibrary):
    
    '''
    classdocs
    ''' 
    server=""
    def __init__(self, servername, moviesLibID, seriesLibID):
        '''
        Constructor
        '''
        self.server=servername
        self.movieLibID = moviesLibID
        self.seriesLibID = seriesLibID
        self.mediaplayer = "PLEX media player"
        self.mediaplayerprotocol = "PLEX"

#===============================================================================
# Functions that are in beta testing
#===============================================================================
 
    def plexgetxml (self, location):
        '''
        plexgetxml returns the root for an XML for Plex
        '''
        tree = ElementTree.parse(urlopen(self.server+location))
        root=tree.getroot()
        return root
    
    def recentlyAddedTV (self):
        '''
        recentlyAddedTV returns the recently added TV episodes from the library
        '''
        TVItems=[]
        root = self.plexgetxml("/library/sections/"+self.seriesLibID+"/recentlyAdded")
        for node in root:
            root2 = self.plexgetxml(node.get('grandparentKey'))
            for extrainfo in root2:
                TVItems.append(self.TVitem(node.get('grandparentTitle'),extrainfo.get("summary"), 
                                          node.get("title"), node.get("summary"), 
                                          node.get("duration"),
                                          int(node.get ('parentIndex')),
                                          int(node.get ('index')),
                                          int(node.get ('viewCount'))))
        return TVItems
    
    def recentlyAddedMovies(self):
        '''
        recentlyAddedMovies returns the most recently added movies
        '''
        MovieItems=[]
        root = self.plexgetxml("/library/sections/"+self.movieLibID+"/recentlyAdded")
        for node in root:
            MovieItems.append(self.MovieItem(node.get('title'), 
                                             node.get('summary')))
        return MovieItems 
    
    def connect(self):
        '''
            connects to server. for Plex this doesn't do anything (yet)
        '''
        pass
        
    def clients (self):
        '''
            Returns the clients from the library server
        '''
        root=self.plexgetxml("/clients")
        Clients=[]
        for node in root:
            Clients.append (self.ClientItem(node.get('name'), 
                                              node.get('host'),
                                              node.get('address'),
                                              node.get('port')
                                              ))
        return Clients
        
    def recentlyAiredTV (self):
        '''
        recentlyAddedTV returns the recently added TV episodes from the library
        '''
        TVItems=[]
        root = self.plexgetxml ("/library/sections/"+self.seriesLibID+"/newest")
        for node in root:
            root2 = self.plexgetxml (node.get('grandparentKey'))
            for extrainfo in root2:
                TVItems.append (self.TVitem(node.get('grandparentTitle'),extrainfo.get("summary"), 
                                            node.get("title"), node.get("summary"), 
                                            node.get("duration"),
                                            int(node.get ('parentIndex')),
                                            int(node.get ('index')),
                                            node.get ('viewCount')))
        return TVItems
#===============================================================================
# Functions that are pre-alpha and alpha        
#===============================================================================
    
    def getMovieLibrary (self):
        root=self.plexgetxml("/library/sections/"+self.seriesLibID+"/recentlyAdded")
        return root
    
    
    def getLatestMovies (self, numofitems):
        print "latest movies from " + self.__mediaplayerprotocol
        return "empty list"
    
    def getLatestTVShows (self,numofitems):
        print "latest tv shows from " + self.__mediaplayerprotocol
        return "empty list"
    
    def getLatestMusic (self,numofitems):
        print "latest music from " + self.__mediaplayerprotocol
        return "empty list"
    
    def unwatchedTV(self, libID):
        root=self.plexgetxml("/library/sections/"+self.seriesLibID+"/unwatched")
        return root
    