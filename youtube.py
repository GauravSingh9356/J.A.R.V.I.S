from urllib.request import urlopen
import urllib.parse
import re
from bs4 import BeautifulSoup
import webbrowser
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register(
    'chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def you(textToSearch):
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.get('chrome').open_new_tab(url)
    #response = urlopen(url)
    #html = response.read()
    #soup = BeautifulSoup(html, "lxml")
    #flag = 0
    #search_results=re.findall('href=\"\\/watch\\?v=(.{11})', html.decode())
    #print(search_results)
    #webbrowser.get('chrome').open_new_tab('http://youtube.com/watch?v=' + search_results[0])
    


if __name__ == '__main__':
    print(you('lahore'))
