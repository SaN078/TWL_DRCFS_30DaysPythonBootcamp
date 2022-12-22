from bs4 import BeautifulSoup
import requests

url = "https://www.hamropatro.com/"

def get_content(url:str) ->str:
    content_ = requests.get(url)
    #parsing
    sooop = BeautifulSoup(content_.content,'html.parser')
    date =  sooop.find("span").text
    print(date)
    return date




























if __name__ == "__main__":
    get_content(url)