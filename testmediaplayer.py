# from medialib.medialib import MediaPlayer
from medialib.plex import PlexMediaLibrary



if __name__ == '__main__':
    PlexServer = "http://" + raw_input("Enter Plex Server (name or IP address): ")+":"+raw_input("enter port: ")
    MovieSection = raw_input ("Enter the library ID for your movies: ")
    TVSection = raw_input ("Enter the library ID for your series: ")

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

