from flask import Flask,Blueprint, render_template
from urllib.parse import quote
from urllib.request import urlopen
import json
import requests
import os
news = Blueprint('news', __name__)


OPEN_NEW_URL = "http://api.mediastack.com/v1/news?access_key={}&keywords=currency"

OPEN_NEW_KEY = os.environ.get('API_NEWS')

@news.route('/news')
def news1():  
    url = OPEN_NEW_URL.format(OPEN_NEW_KEY)
    data = requests.get(url).json()
    mydict = data['data']
    return render_template('news.html', new=mydict)

# def get_newz(news,OPEN_NEW_KEY):

#     query = quote(news)

#     url = OPEN_NEW_URL.format(news,OPEN_NEW_KEY) 

#     data = urlopen(url).read() #ยิง request ไป ตอบกลับมาเป็น json xml

#     parsed = json.loads(data)

#     news = None
#     Arr = []
#     if parsed.get('articles'):

#         for x in parsed['articles']:
#             title = x['title']
#             description = x['description']
#             url = x['url']
            
            

#             news = { 'title': title,  
#                      'description': description,
#                      'url': url
#                    }
#             Arr.append(news)
                   
#     return Arr

    #return Arr,render_template('news.html')