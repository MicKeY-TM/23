import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import wikipedia
from wikipedia import exceptions
import webbrowser
import os
import test

# import smtplib


def speak (audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voices',voices[1].id)
    # print(voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      
      r.pause_threshold= 1
      audio=r.listen(source)
    try:
      print("Rcognizing...")
      query= r.recognize_google(audio,language='en-in')
      print(f"User said:{query}\n ")
      

    except Exception as e:
      #print(e)
      a='Sorry sir i can\'t recognize..Say that again please....'
      print(a)
      speak(a)
      return 'None'
    return query

#we need to first allow less secure apps in gmail
# def sendEmail(to,content):
#   server=smtplib.SMTP('smtp.gmail.com',587)
#   server.ehlo()
#   server.starttls()
#   server.login('your_gmail','your_password')
#   server.sendmail('you_gmail',to, content)
#   server.close()
 
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
      speak("Good Morning Sir..")
    elif hour >=12 and hour<18:
      speak("Good Afternoon Sir..")
    else:
      speak("Good Evening Sir..")
    speak("I am Mickey. sir, Please tell me how may help you?..")

if __name__ == "__main__":
  wishMe()

  while True:
    query=takeCommand().lower()
    
# logic for executing task based on quary
    if 'wikipedia' in query:
      speak('Searching wikipedia..')
      try:
        query=query.replace("wikipedia","")
        results= wikipedia.summary(query,sentences=1)
        speak("According to wikipedia")
        print(results)
        speak(results)
      except exceptions as e:
        p='i don\'t have any wikipedia'
        print(p)
        speak(p)
    else:
      
      test.order(query)
    
    # # elif 'email to mickey' in query:
    #   try:
    #     speak("what should i say")
    #     content=takeCommand()
    #     to= 'www.tanmoymaity2016@gmail.com'
    #     sendEmail(to,content)
    #     speak("Email has been send")
    #   except exceptions as e:
    #       speak("Sorry my friend Tanmoy bhai  i am not able to send email")

    if 'exit' in query:
        test.speak('okey sir.. exit')
        break

