import requests
import json
import time


myBaseUrl = "http://qunanan.win:8080"
tempPublicKey = 'w0BGBwQWwZSk1QQbGZoaSQge0kE'
tempPrivateKey = 'On5e5j07jYIvPZZ8RnwLF0LzmGg'
tempDeleteKey = 'owVrV07W0lFwAZZoaPJXuyEe1L2'

humiPublicKey = 'kBgQVO2lB6U3mYYb9GNQSWVpBe4'
humiPrivateKey = 'pjPQrO6ljNSM5LLlW9j0cyG3ZOK'
humiDeleteKey = 'vLwJX3DYLWCQOppqE7Lehn2G71q'


requests.packages.urllib3.disable_warnings()

def pushTemp (data):
    url = myBaseUrl + '/input/' + tempPublicKey + '?private_key=' + tempPrivateKey + '&temp=' + str(data)
    req = requests.get(url)
    if req.status_code == 200:
        print 'push data: temperatrue -- ' + str(data)
    else:
        print req.content
        
def pushHumi (data):
    url = myBaseUrl + '/input/' + humiPublicKey + '?private_key=' + humiPrivateKey + '&humi=' + str(data)
    req = requests.get(url)
    if req.status_code == 200:
        print 'push data: humidity -- ' + str(data)
    else:
        print req.content
        
token = "1862ed6ca6bbd9f904b0e35fd299195e"        
humiURL = "https://cn.iot.seeed.cc/v1/node/GroveTempHumProD0/humidity?access_token=" + token
tempURL = "https://cn.iot.seeed.cc/v1/node/GroveTempHumProD0/temperature?access_token=" + token
sleepURL = "https://cn.iot.seeed.cc/v1/node/pm/sleep/100?access_token=" + token

while True:
    try:
        temp_req = requests.get(tempURL,timeout=10)
        humi_req = requests.get(humiURL,timeout=10)
        if temp_req.status_code == 200:
            temp = json.loads(temp_req.content)['celsius_degree']
            pushTemp(temp)
            print "Temperature = " + str(temp)
        else :
            print temp_req.content
        if humi_req.status_code == 200:
            humi = json.loads(humi_req.content)['humidity']
            pushHumi(humi)
            print "Humidity = " + str(humi)
        else :
            print humi_req.content
        sleeep = requests.post(sleepURL,timeout=10)
        if sleeep.status_code != 200:
            print "sleep error!"
        time.sleep(120)
    except:
        print("got an error")
        time.sleep(60)
