import requests
import json
import numpy as np
import string
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import facebook
import json
import nltk 
from nltk.corpus import stopwords   
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#allMessages = pd.read_csv("C:/Users/faith/facebookpython/fb.csv",index_col=0)
#print (allMessages)
#stopwords = set(STOPWORDS)

token = 'EAAFJkdFc6GEBAFZC2DiOlSgs2ZC0u0gKcspOx9MG130sQZC8pYGIKP2bgWxderZCfZCLd5oNaqYChCqIDFhQsg2bZAQv5vzoaPErODHanw8oRGHJEGL81Sj1aZAHBk6jBouakXQiBK4FpiAZB4cmZCQgbDr9qItRLlvF9LrQyQmdhwK7quGLkLOrWNTcs5cISEx4ZD'

graph = facebook.GraphAPI(access_token= token, version ="3.1")

posts = graph.get_object(id='108843817704467/conversations', fields='messages{message}')

allMessages = []

while(True):
    try:
            #get conversations
        conversations = posts["data"]
                
            #loop conversations
        for conversation in conversations:
            convo = conversation["messages"]
                    
            while(True):
                try:
                        #get messages
                    messages = convo["data"]
                        #Loop messages
                    for message in messages:
                        allMessages.append(message["message"])
                            
                        #get message next page
                    nextmessages = convo["paging"]["next"]
                    convo = requests.get(nextmessages).json()
                        
                except KeyError:
                     break
            #get conversation next page
        conversation_next = posts["paging"]["next"]
        posts = requests.get(conversation_next).json()
    except KeyError:
        break
'''
wc = WordCloud(max_font_size=75, max_words=100,width=500, height=400,collocations=False,
                background_color='white',scale=1,relative_scaling=0.5).generate(str(allMessages))
plt.imshow(wc,interpolation='bilinear')
plt.axis("off")
#plt.savefig('C:/Users/faith/facebookpython/static/wordcloud_photo/wordcloud3.png')
#plt.show()
'''


analyse = SentimentIntensityAnalyzer()
        #nltk.downloader.download('vader_lexicon')
            
summary = {"positive":0,"neutral":0,"negative":0}
for x in allMessages: 
    ss = analyse.polarity_scores(x)
    if ss["compound"] == 0.0: 
        summary["neutral"] +=1
    elif ss["compound"] > 0.0:
        summary["positive"] +=1
    else:
        summary["negative"] +=1
#print(summary)

lists = sorted(summary.items()) # sorted by key, return a list of tuples
#x= sentiments
#y= polarity scores
x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.bar(x, y)
plt.savefig('C:/Users/faith/facebookpython/static/wordcloud_photo/chart.png')
plt.show()




