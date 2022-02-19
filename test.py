import pandas as pd
import webbrowser
import os
import datetime
import pyttsx3
import wikipedia
from wikipedia import exceptions

def speak (audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voices',voices[1].id)
    # print(voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def order(qery):
    csv_path='responce.csv'
    index=['qery','execution']
    path=pd.read_csv(csv_path,names=index,header=None)
    # print(path)
    query=qery
    query=query.replace('love you','love_you')
    query=query.replace('play music','play_music')

    print(query)
    # print(query)
    r=0
    for i in range(len(path)): 
        if 'exit' in query:
            r+=1       
                  
        if path.loc[i,'qery'] in query :
            r+=1
            if '\n' in  path.loc[i,'execution']:
                p=path.loc[i,'execution'] 
                sp=[]
                sp.extend((p.split('\r\n')))
                #    print(sp[:])
                for j in range(len(sp)):
                    exec(sp[j])
                break    
            else: 
                exec(path.loc[i,'execution'])
                break
    # if r==0:
    #   try:
    #     query=query.replace("wikipedia","")
    #     results= wikipedia.summary(query,sentences=1)
    #     speak("According to Google")
    #     print(results)
    #     speak(results)
    #   except exceptions as e:
    #     p='sorry sir...i don\'t have any idea'
    #     print(p)
    #     speak(p)
        
      
if __name__ == "__main__" :
    qery='what the day'
    order(qery)
            
        

