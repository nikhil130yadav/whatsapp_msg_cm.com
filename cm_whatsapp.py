#from abc import ABC,abstractmethod 
import requests
import json
import os
os.getcwd()



class MessagingClient():
    global_endpoint = "https://gw.cmtelecom.com/v1.0/message"
    def __init__(self,product_token,name_space):
        self._product_token = product_token
        self._name_space =  name_space
        
        
    def sendMessage(self,template_name,message=[],to_numbers =[]):
        '''
        Method to send template msg wihtout any rich media on whatsapp routing through cm.com.
        Parameters:
        Template_name - name of element of template, Please visit cm.com account 
        messasge - list of key-value of variables to send
        to_numbers -list of numbers to send whatsapp message
        
        Returns - json data from cm.com
        '''
        
        headers = {'host': 'gw.cmtelecom.com','accept': 'application/json','content-type': 'application/json ; charset=utf-8'}
        
        send_to_numbers = [{"number":number} for number in to_numbers ]
        media_auth = {
                            "messages": {
                                "authentication": {
                                    "producttoken": self._product_token
                                },
                                "msg": [{
                                    "from": "0013053959986",

                                    "to": send_to_numbers,
                                    "body": {
                                        "type": "auto",
                                        "content": "This is a WhatsApp message"
                                    },
                                    "allowedChannels": ["WhatsApp"],
                                    "richContent": {
                                        "conversation":
                                        [{
                                            "template": {
                                                "whatsapp": {

                                                      "namespace": self._name_space,
                                                    "element_name": template_name,
                                                    "language": {
                                                        "policy": "deterministic",
                                                        "code": "en_US"
                                                    },
                                                    "components": [

                                                        {
                                                            "type": "body",
                                                            "parameters": 
                                                            message
                                                        },
                                                           {
                                                            "type": "footer",
                                                            "parameters": [
                                                                {
                                                                    "type": "text",
                                                                "text": """Thank You For Shipping With Us !

                                                                        Email- TRACK@EZZYSHIP.COM"""
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            }
                                        }]
                                    }
                                }]
                            }
                        }
        auth = json.dumps(media_auth)
        print(auth)
        #print(send_to_numbers,"\n",self.product_token)
        #print(json.dumps(auth))
        return requests.post(url=self.global_endpoint,data=auth,headers=headers)
        

    def send_chatbot_response(self,message="Hello World",to_numbers =[]):
        '''
        Method to send normal Text msg on whatsapp routing through cm.com account
        Parameters:
        Template_name - is name of element of template, see in cm.com
        messasge - list of key-value of variables to send,check format on cm.com
        to_numbers -list of numbers to send whatsapp message
        
        Returns - json data from cm.com
        '''        
        
        headers = {'host': 'gw.cmtelecom.com','accept': 'application/json','content-type': 'application/json ; charset=utf-8'}
        
        
        print("tooo numbers",to_numbers)
        send_to_numbers = [{"number":number} for number in to_numbers ]
        print(send_to_numbers)
        media_auth = {
            "messages": {
                "authentication": {
                    "productToken": self._product_token
                },
                "msg": [{
                    "body": {
                        "type": "auto",
                        "content": message
                    },
                    "to": send_to_numbers,
                    "from": "0013053959986",
                    "allowedChannels": ["WhatsApp"]
                }]
            }
        }
        auth = json.dumps(media_auth)
        return requests.post(url=self.global_endpoint,data=auth,headers=headers)