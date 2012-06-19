# from medialib.medialib import MediaPlayer
import os
from medialib.plex import PlexMediaLibrary

PlexServer=""
PlexPort=""
TVSection=""
MovieSection=""
NumOfItems=3
mediaplayer=object


def clear_screen():
    os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
    
def print_menu():
    clear_screen()
    print "Test Medialibrary"
    print "================="
    print
    print
    print_current_config()
    print
    print "1. Set connection info"
    
    if hasattr(mediaplayer,'info'):
        print "2. print info"
        print "3. Show recently added movies"
        print "4. Show recently added episodes"
        print "5. Show recently aired episodes"
    print 
    print "q. quit"
    print 
 
def print_current_config():
    print "Current config:"
    print " - Plex server: ", PlexServer
    print " - Plex Port: ", PlexPort
    print " - Movies Library ID: ", MovieSection
    print " - Series Library ID: ", TVSection  
    print " - show num of items: ", NumOfItems
    
def get_connection_info():
    global PlexServer
    global PlexPort
    global TVSection
    global MovieSection
    global actions
    global NumOfItems
    
    print 
    print "Enter configuration info"
    print "========================"
    PlexServer=raw_input("Enter Plex Server (name or IP address):")
    PlexPort=raw_input("enter port: ")
    MovieSection=raw_input ("Enter the library ID for your movies: ")
    TVSection=raw_input ("Enter the library ID for your series: ")
    NumOfItems=str2num(raw_input("Enter number of items to show: "))
    create_connection_object()
    actions = {"1": get_connection_info, "2": print_connection_info, "3": showrecentlyaddedmovies, "4": showrecentlyaddedseries, 
               "5": showrecentlyairedseries}
    
def str2num (string):
    try:
        i = int(string)
    except ValueError:
        i = 0
    return i
    
def create_connection_object():
    global mediaplayer
    plexconnectionstring="http://"+PlexServer+":"+PlexPort
    mediaplayer = PlexMediaLibrary(plexconnectionstring,MovieSection, TVSection)

def no_such_action():
    print "Chosen option invalid. Please try again"

def wait_for_enter():
    raw_input("Press Enter to continue...")
        
def print_connection_info():
    mediaplayer.info()
    wait_for_enter()
    
def maxnum (item,itemstoshow):
    if len(item)<itemstoshow:
        x=len(item)
    else:
        x=NumOfItems
    return x

def showrecentlyaddedmovies():
    AllMovies=mediaplayer.recentlyAddedMovies()
    for x in range (0,maxnum(AllMovies,NumOfItems)):
        showmovie(AllMovies[x])
    wait_for_enter()

def showrecentlyaddedseries():
    AllSeries=mediaplayer.recentlyAddedTV()
    for x in range (0,maxnum(AllSeries,NumOfItems)):
        showseries(AllSeries[x])
    wait_for_enter() 
    
def showrecentlyairedseries():
    AllSeries=mediaplayer.recentlyAiredTV()
    for x in range (0,maxnum(AllSeries,NumOfItems)):
        showseries(AllSeries[x])
    wait_for_enter()        

def buildmenu():
    global actions
    while True:
        print_menu()
        selection = raw_input("Your selection: ")
        if "q" == selection:
            return
        toDo = actions.get(selection, no_such_action)
        toDo()
        
def asciiprint (item):
    print item.encode('ascii','ignore')
            
def showmovie(movie):
    asciiprint ("Movie title: " + movie.title)
    print "Summary:"
    asciiprint (movie.summary)
    print ('-' * 80)

def showseries(series):
    asciiprint ("Series title: " + series.showtitle)
    print "Summary:"
    asciiprint (series.synopsis)
    asciiprint ("episode: " + str(series.season) + "x" + str(series.episode) + " " +series.title)
    print "Episode summary:"
    asciiprint (series.summary)
    print ('-' * 80)

if __name__ == '__main__':
    actions={"1": get_connection_info}
    buildmenu()    
    
   
    #    episode.season, 
    #    'x', episode.episode
    #===========================================================================
    
    #===========================================================================
    # clients = mediaplayer.clients()
    # for client in clients:
    #    print client.name, '|', client.host, '|', client.address, '|', client.port
    #===========================================================================

