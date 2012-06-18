# from medialib.medialib import MediaPlayer
from medialib.plex import PlexMediaLibrary

PlexServer = "http://192.168.1.9:32400"
MovieSection = "1"
TVSection = "2"

if __name__ == '__main__':
    mediaplayer = PlexMediaLibrary(PlexServer,MovieSection, TVSection)
    mediaplayer.info()
    #===========================================================================
    # mediaplayer.getLatestTVShows(5)
    # mediaplayer.getLatestMovies(5)
    # mediaplayer.getLatestMusic(5)
    #===========================================================================
    
    #recentlyAddedMovies = mediaplayer.recentlyAddedMovies ()
    #recentlyAddedTV = mediaplayer.recentlyAddedTV()
    recentlyAiredTV = mediaplayer.recentlyAiredTV()
    
    #for movie in recentlyAddedMovies:
    #    print movie.movie, ' |', movie.summary
    #===========================================================================
    for episode in recentlyAiredTV:
        print episode.showtitle.encode('ascii', 'ignore'), '|', episode.synopsis.encode('ascii','ignore'), 
        '|', episode.title.encode('ascii','ignore'), '|', episode.summary.encode('ascii','ignore'), '|', episode.season, 
        'x', episode.episode
    #===========================================================================
    
    #===========================================================================
    # clients = mediaplayer.clients()
    # for client in clients:
    #    print client.name, '|', client.host, '|', client.address, '|', client.port
    #===========================================================================

