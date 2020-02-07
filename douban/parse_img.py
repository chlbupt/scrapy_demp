# encoding:utf-8
import urllib
from urllib import request
from base64 import b64encode
import requests

appcode = '06cd6b081afa457899cdbddbb953462f'
apiurl = 'http://codevirify.market.alicloudapi.com/icredit_ai_image/verify_code/v1'
# imgurl = 'https://accounts.douban.com/j/captcha/show?vid=login:captcha:YwZ3E56cO9INTqHMfz3vtXgM&size=small'
imgurl = 'https://icredit-api-market.oss-cn-hangzhou.aliyuncs.com/%E9%AA%8C%E8%AF%81%E7%A0%81.jpg'
request.urlretrieve(imgurl, 'captcha.png')

formdata = {}
with open('captcha.png', 'rb') as fp:
    data = fp.read()
    pic = b64encode(data)
    formdata['IMAGE'] = pic
    formdata['IMAGE_TYPE'] = '0'

headers = {
    'Authorization': 'APPCODE ' + appcode,
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}

print(formdata)
response = requests.post(apiurl, data=formdata, headers=headers)
print(response.json())