import sys
import os
import requests
from slackclient import SlackClient

# get the api key from the environment variables
token = "xoxb-465708053495-463929998784-7f7QOOcxGuXqMtJ0rUGo6Mfr"


# function to send messages to Slack
def sendMessage(text,channel):
      
    # connect to the api and create client
    sc =SlackClient(token)

    # send a message to a specific channel
    sc.api_call(
                  "chat.postMessage",
                  channel=channel,
                  text=text,
                  as_user= True,
                  username="yoda_nero"
               )


# function to send edited messages to Slack
def sendTextAttachments(text, channel, color):

    # Attachment file
    attachments = [{"color": color, "text":text}]

    # connect to the api and create client
    sc = SlackClient(token)
    
    # send a message to a specific channel
    sc.api_call(
                 "chat.postMessage",
                  channel= channel,
                  attachments=attachments,
                  as_user= True,
                  username="yoda_nero"
                 )
           
# function to send messages to Slack
def sendImage(text, titleImage, img, channel):

    # Attachment file
    attachments = [{"title": titleImage, "image_url": img}]

    # connect to the api and create client
    sc = SlackClient(token)

    # send a message to a specific channel
    sc.api_call(
                 "chat.postMessage",
                  channel= channel,
                  text = text,
                  attachments=attachments,
                  as_user= True,
                  username="yoda_nero"
                )


# function to send file to Slack
def sendFile(pathfile,filename,file_type):
    

    #Abrir Arquivo
    my_file = {'file' : (pathfile, open(pathfile, 'rb'), file_type)}

    #Parametros
    payload={
              "filename":filename, 
              "token":token, 
              "channels":['uipath']
            }
    
    requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)