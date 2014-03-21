# coding:utf-8

from pykakao import kakaotalk
from PIL import Image
import random
import os
from google_image import image_search

img_cnt = 0
kakao = kakaotalk("b92b9df63e1b40c78dccdd5347e5e1eef8dd336202194690a3574e1ad2e1e98a", "1", 4507713)

if kakao.login()["body"]["status"] == 0:
    while True:
        packet = kakao.translate_response()

	if packet["command"] == "MSG":
	    message = packet["body"]["chatLog"]["message"].encode("utf-8")
	    groupid = packet["body"]["chatLog"]["chatId"]
	    uid = packet["body"]["chatLog"]["authorId"]
	
	    if message[0] == '>':
	        kakao.write(groupid, os.popen(packet["body"]["chatLog"]["message"][1:]).read())

	    if message[:7] == "@검색":
	        print "equal"
	        kakao.write(groupid, "https://www.google.co.kr/#newwindow=1&q=" + packet["body"]["chatLog"]["message"][4:])

	    if message[:7] == "@구글":
	        kakao.write(groupid, "http://lmgtfy.com/?q=" + packet["body"]["chatLog"]["message"][4:])

	    if message[:10] == "@이미지":
	        print "image" + packet["body"]["chatLog"]["message"], img_cnt
		#kakao.write_image(groupid, "a.jpg", 1920, 1080)

		if len(message) < 11:
		    kakao.write(groupid, "image load fail")
		    continue
		if not image_search(message[11:], '', img_cnt):
		    kakao.write(groupid, "image load fail")
		    continue

		img = Image.open("images/" + str(img_cnt) + ".jpg")
		if img == False:
		    kakao.write(groupid, "image load fail")
		    continue
		url = kakao.upload_image("images/" + str(img_cnt) + ".jpg")
		w, h = img.size
		kakao.write_image(groupid, url, w, h)
		img_cnt += 1

	    if message[:7] == "@랜덤":
	        kakao.write(groupid, str(random.randint(0, 99)) + "가 나왔습니다 (0~99)")

else:
    print "login failed"
