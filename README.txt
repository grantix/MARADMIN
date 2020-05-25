MARADMIN Command Search
A program by 1stLt Grant Guttschow, USMC
Published November 2019

The United States Marine Corps utilizes a single database for posting updates to the entire operating force.
Marine Administrative Messages (MARADMINS) are centrally located at the following URL:
https://www.marines.mil/News/Messages/MARADMINS

For a website of such importance, the filtering and search options are severely limited.  Currently the filters
include 'Year', 'Active/Cancelled', or the 'Key Word' search option which will return any document containing
the word.

Maradmin.py is a tool intended to be used by Marine Corps unit commanders in order to quickly and efficiently
scan thousands of MARADMINS for updates and notifications regarding Marines within the command.  The program
can be run as frequently or infrequently as desired, and the results will be displayed in the command shell
as the program executes.

This program utilizes a web crawler/scraper functionality aided by BeautifulSoup and Selenium imports.

In order to run this program, simply navigate to the created folder in a command shell and type:

python3 maradmin.py
