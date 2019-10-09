'''
Demo program showing how we can save an online image locally
Call urlretrieve method passing the URL of the image and the file name with which you want to save locally
'''

import urllib.request

urllib.request.urlretrieve("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png","../output/onlineimage.jpg")