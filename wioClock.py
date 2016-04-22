import requests
import time
import json
import datetime
import pytz

requests.packages.urllib3.disable_warnings()
token = "743b63e1c57e783a5a2eae8acaea9d80"

local_tz = pytz.timezone('Asia/Shanghai') # use your local timezone name here


def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt) # .normalize might be unnecessary
def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%H%M')
    
while True:
    try:
        dp_url = "https://cn.iot.seeed.cc/v1/node/Grove4DigitUART0/display_point/1?access_token=" + token
        requests.post(dp_url,timeout=10)
        now = aslocaltimestr(datetime.datetime.utcnow())
        print (now)
        time_url = "https://cn.iot.seeed.cc/v1/node/Grove4DigitUART0/display_digits/0/" + now +"?access_token=" + token
        requests.post(time_url,timeout=10)
        time.sleep(60)
    except:
        print("got an error")
        streamer.log("Status", "got an error")
        time.sleep(60)
