from webbot import Browser
import time

f = open("pass.txt","r")
data = f.read()
email = data.split(';')[0]
pwd = data.split(';')[1]

url = 'https://web.simple-mmo.com/travel'
web = Browser()

def fight():
    try:
        isNPC = web.find_elements(text=' Attack')
        if len(isNPC)==1: #NPC fight
            web.click(text=' Attack')
            while not web.exists(text='Close'):
                time.sleep(1)
                web.click(text='Attack')
            time.sleep(1)
            web.click(text='Close')
        time.sleep(1)
    except:
        pass

def changeStep():
    try:
        while web.find_elements(id='travelBarContainer')[-1].get_attribute('style')=='':
            time.sleep(0.5)
        web.click(id='primaryStepButton')
        time.sleep(1)
    except:
        pass

def verify():
    try:
        isVerify = web.find_elements(text='Press here to verify')
        if len(isVerify)==1:
            web.click(text='Press here to verify')
            # develop AI to recognize image
        time.sleep(1)
    except:
        pass

def play():
    try:
        while True:
            time.sleep(1)
            fight()
            verify()
            if web.get_current_url()==url:
                changeStep()
    except KeyboardInterrupt:
        import sys
        sys.exit()

def connect():
    web.go_to("https://web.simple-mmo.com/login")
    web.type(email,id="email")
    web.type(pwd,id="password")
    web.click(text='Sign in')
    web.go_to(url)
    web.click(id='primaryStepButton')
    play()

connect()
