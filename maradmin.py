# necessary imports for project
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# create a webdriver object and set options for headless browsing
options = Options()
options.headless = True
browser = webdriver.Chrome('./chromedriver', options=options)

# Additional outside variables and lists
mainurl = "https://www.marines.mil/News/Messages/MARADMINS/?Page="
maradmin_links = []
namelist = []
pagecheck = ""

# generate a list of names to search for from user input
def main(namelist):
    print ('-'*20, 'Welcome to the MARADMIN name check tool!', '-'*20)
    print("""
        Please input a last name you would like to scan for.
        Press enter after each name.

        OR

        Copy and paste a list of names formatted as:
        Lastname;Lastname;Lastname

        Type "done" when finished inputting names. """)

    while True:
        inputted = input()
        if inputted == ("done"):
            if len(namelist) == 0:
                print("No names inputted.  Goodbye")
                return None

            else:
                print("The names being checked for are:")
                for i in namelist:
                    print (i)
            break
        else:
            if ";" in inputted:
                namelist = inputted.split(";")
            else:
                namelist.append(inputted)

    print ("""
    Now input how many pages you would like to scan for these names.
    type a number between 1 and 420 and press enter:
    """)
    pagecheck = input()

    # if there are names inputted, run the scrape and check functions
    scrape_mainpage(maradmin_links, mainurl, browser, pagecheck)
    check_message(maradmin_links, browser, namelist)

# uses webdriver object to execute javascript code and get dynamically loaded webcontent
def get_js_soup(mainurl, browser):
    browser.get(mainurl)
    res_html = browser.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html, 'html.parser')  # beautiful soup object to be used for parsing html content
    return soup

# extracts all message urls from the maradmin page range
def scrape_mainpage(maradmin_links, mainurl, browser, pagecheck):
    print ('-'*20, 'Scraping MARADMIN pages 1 -', pagecheck, '-'*20)
    for page in range(1,int(pagecheck) + 1):
        newurl = mainurl + str(page)
        soup = get_js_soup(newurl, browser)
        for link_holder in soup.find_all('div', attrs={'class': 'msg-title msg-col'}):
            rel_link = link_holder.find('a')['href']
            maradmin_links.append(rel_link)
    print ('-'*20, 'Found {} MARADMIN messages'.format(len(maradmin_links)), '-'*20)
    return maradmin_links

# checks the namelist against all maradmin links collected and outputs matches
def check_message(maradmin_links,browser, namelist):
    flag = 0
    for url in maradmin_links:
        soup = get_js_soup(url, browser)
        title = soup.find('div', class_='msg-title msg-title-animate').get_text()
        body = soup.find('div', class_='body-text').get_text()
        # scans the body for any references to namelist
        for i in namelist:
            if body.find(i) > 0:
                flag = 1
                print(i + " has been found in MARADMIN: " + '\n' + title)
    if flag == 0:
        print ("No MARADMINS include the names you submitted")
    print("Done scraping MARADMIN Pages")


# run main program
main(namelist)
