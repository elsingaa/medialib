#medialib

* **Author**: [A.J. Elsinga](https://github.com/elsingaa]

##What is medialib?

medialib is a unifying solution for accessing media libraries like Plex and XMBC. medialib was born out of irritation for the lack of Plex support in various tools.


##What features does it have?
* plexgetxml (internal only)
* recentlyAddedTV
* recentlyAiredTV
* recentlyAddedMovies
* clients


##Timeline/priority

1. generic object model (Python)
2. Plex implementation (Python)
3. XBMC implementation (Python)
4. other implementations (Python)

The first priority will be to set up a working library for integration in Maraschino, a front-end for HTPCs.

##Demo program
A simple demo program is available to demonstrate various functions in the library. Start it with python demo.py and enter your configuration settings.
The library ID's can be found with a web browser pointing to http://<yourplexserver>:<port>/library/sections, look up the correct library (title)
and use the values mentioned with key=
 