
import requests
from bs4 import BeautifulSoup

class WikiScrapper():
  def __init__(self,keyword,url=None):
    self.keyword=keyword
    if url is None:
      self.url = f"https://en.wikipedia.org/wiki/{self.keyword}"

  def scrape(self):
    response=requests.get(self.url)
    if response.status_code==200:
      soup=BeautifulSoup(response.text,"html.parser")
      main_content = soup.find('div', class_='mw-parser-output')
      if main_content:
        return main_content.get_text()
      else:
        return "No main content found"
    else:
      return "Error: Unable to fetch the page"
    
    
  
  
