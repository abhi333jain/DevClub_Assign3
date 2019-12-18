import os
import requests
from bs4 import BeautifulSoup

input_file = open("inputfile.txt" , "r")
content = input_file.read().split()
months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
monthsinv = { 1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july', 8:'august', 9:'september', 10:'october', 11:'november', 12:'december'}
start_month = months[content[0].lower()]
start_year = int(content[1])
end_month = months[content[2].lower()]
end_year = int(content[3])
author_list = content[4:]


while(start_year<=end_year) :
    os.mkdir(str(start_year))
    os.chdir(str(start_year))
    if(start_year<end_year) :
        while(start_month<=12):
            os.mkdir(monthsinv[start_month])
            os.chdir(monthsinv[start_month])
            if(start_month<=9)
                source = requests.get("http://explosm.net/comics/archive/"+str(start_year)+"/0"+str(start_month))
            else
                source = requests.get("http://explosm.net/comics/archive/" + str(start_year) + "/" + str(start_month))
            soup = BeautifulSoup(source.content ,'html5lib')

            for comic_content in soup.find_all(id='comic-author'):
                date = comic_content.text.split()[0]
                author = comic_content.text.split()[2]
                if(author in author_list):
                    img_source =  requests.get("http://explosm.net" + comic_content.parent.a['href']).content
                    img_soup = BeautifulSoup(img_source , 'html5lib')
                    img_url = "http:" + img_soup.find(id='main-comic')['src']
                    img = requests.get(img_url).content
                    comic_name = "{}-{}.png".format(date,author)
                    fh= open(comic_name, 'wb')
                    fh.write(img)
                    fh.close()
            os.chdir("..")
            start_month+=1
        os.chdir("..")
        start_month=1
        start_year+=1

    else :

       while (start_month <= end_month):
           os.mkdir(monthsinv[start_month])
           os.chdir(monthsinv[start_month])
           if (start_month <= 9)
               source = requests.get("http://explosm.net/comics/archive/" + str(start_year) + "/0" + str(start_month))
           else
               source = requests.get("http://explosm.net/comics/archive/" + str(start_year) + "/" + str(start_month))
           soup = BeautifulSoup(source.content, 'html5lib')

           for comic_content in soup.find_all(id='comic-author'):
               date = comic_content.text.split()[0]
               author = comic_content.text.split()[2]
               if (author in author_list):
                   img_source = requests.get("http://explosm.net" + comic_content.parent.a['href']).content
                   img_soup = BeautifulSoup(img_source, 'html5lib')
                   img_url = "http:" + img_soup.find(id='main-comic')['src']
                   img = requests.get(img_url).content
                   comic_name = "{}-{}.png".format(date, author)
                   fh = open(comic_name, 'wb')
                   fh.write(img)
                   fh.close()
           os.chdir("..")
           start_month += 1

       start_year+=1


