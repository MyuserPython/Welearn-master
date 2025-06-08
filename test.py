import requests
import re
from time import sleep
from random import randint

session = requests.Session()

username = '13194440018'
password = 'lfx2983928331'

response = requests.get(
    'https://welearn.sflep.com/user/prelogin.aspx?loginret=http%3a%2f%2fwelearn.sflep.com%2fuser%2floginredirect.aspx',
    allow_redirects=False)
rturl = response.headers['Location'].replace('https://sso.sflep.com/idsvr', '')

data = {
    'rturl': rturl,
    'account': username,
    'pwd': password,
}

rs = session.post('https://sso.sflep.com/idsvr/account/login', data=data)

url = 'https://sso.sflep.com/idsvr'+rturl

res = session.get(url)

url = "https://welearn.sflep.com/ajax/authCourse.aspx?action=gmc"
response = session.get(
    url, headers={"Referer": "https://welearn.sflep.com/student/index.aspx"})

print(response.text)