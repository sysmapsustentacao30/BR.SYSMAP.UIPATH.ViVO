import sys
import os
import requests
from slackclient import SlackClient


# function to send messages to Slack
def sendMessage(text,channel):
      
    # get the api key from the environment variables
    token = "xoxb-465708053495-463929998784-7YFPTVirkcqNpSeLl7j34ZkI"
    
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

    # get the api key from the environment variables
    token = "xoxb-465708053495-463929998784-7YFPTVirkcqNpSeLl7j34ZkI"  

    # Attachment file
    attachments = [{"color": color, "text":text}]

    # connect to the api and create client
    sc = SlackClient(token)
    
    # send a message to a specific channel
    sc.api_call(
                 "chat.postMessage",
                  channel= "uipath_release",
                  attachments=attachments,
                  as_user= True,
                  username="yoda_nero"
                 )
           
# function to send messages to Slack
def sendImage(text, titleImage, img, channel):
    
    # get the api key from the environment variables
    token = "xoxb-465708053495-463929998784-7YFPTVirkcqNpSeLl7j34ZkI"

    # Attachment file
    attachments = [{"title": titleImage, "image_url": img}]

    # connect to the api and create client
    sc = SlackClient(token)

    # send a message to a specific channel
    sc.api_call(
                 "chat.postMessage",
                  channel= "uipath_release",
                  text = text,
                  attachments=attachments,
                  as_user= True,
                  username="yoda_nero"
                )


# function to send file to Slack
def sendFile(file,typeFile,fileName):

    # get the api key from the environment variables
    token = "xoxb-465708053495-463929998784-7YFPTVirkcqNpSeLl7j34ZkI"
    
    #Abrir Arquivo
    my_file = {'file' : (file, open(file, 'rb'), typeFile)}

    #Parametros
    payload={
              "filename":fileName, 
              "token":token, 
              "channels":['uipath_release']
            }
 
    requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)

