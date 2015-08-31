#*-*coding:utf8*-*
import base64
from django.shortcuts import render
from django.http import HttpResponse

import rsa
pub_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCePb1GuZ8BZQLQQKNYEukK9dIN\
 bJXimpU8EKzNOqtnknAnOJgQfrJsohUiI+665Jqcs+CZy7MDOZAs2bOhnmIYzfKG\
 oEND/6TxN4pqgMRQw8qPLjCax1TXxqxfrjTlfBqA/Tn5E7sTfzLIRzFZ/OJkIHu0\
 bgwTXjCGbdaNTpkLuwIDAQAB"
private_key = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAJ49vUa5nwFlAtBA\
o1gS6Qr10g1sleKalTwQrM06q2eScCc4mBB+smyiFSIj7rrkmpyz4JnLswM5kCzZ\
s6GeYhjN8oagQ0P/pPE3imqAxFDDyo8uMJrHVNfGrF+uNOV8GoD9OfkTuxN/MshH\
MVn84mQge7RuDBNeMIZt1o1OmQu7AgMBAAECgYBI95cr4bQcZIOjm+q2ViH319qA\
Li3/S+C8zcOg7wjSvYfRzhrwoDuOND8iewc+TuOslpVe1bs6JXUB+XEHeY0pwUbP\
amVVgjcEVe7xce8QoTKYkC7oAwUBmX8zk/ZVIhME/In8BuY91kYx93fGq+cfquO8\
meD6/k0cojJY+zTeoQJBAM0MN5BcLJ+U5amI9VxiBZGEvi1m8Myjh8N1L/THj61o\
P3A2WDq2miMntbd3qFg8vkshdUCA/dziBeE7FQM5viUCQQDFj/+O3OSNQrcbCl/j\
jtShjp66coKwv00/Jqzm6xKTkOMvbtXNYDGwUIjOMbrUI26VhL4hd4ZqXZ+x/azW\
LsxfAkAQlENN3dYR1SU4rwU/wgE3Qedqnl8r/LD2gdwty5D3cW1nsk0x+h++ZfCQ\
dBFdiRPN2Ve0rnlYScI18uQBDcMtAkEAl8yRHIB1zGSatNg/3WV907T2GWSrLouP\
Gxrod3XgDCqjpWqQNQHYrBT1SRnE6ANhkNkyDhz81vWhIu47w0aqGQJAfJ18bcHu\
3QWNDO+aDFBxyyt3EZXXcCdSP1eCmUE2AgHBVZdNmWfFlko8j1xbu2scg9shSGpA\
g9HbsmC/bj4yGA=="

# Create your views here.
def index(request):
	return render(request,'index.html',{})

def get(request):
	(pub_key,private_key) = rsa.newkeys(1024)
	message = '{"username":"zhxhdean","password":"123456","address":"上海市"}'
	print len(message)
	#公钥加密
	crypto = rsa.encrypt(message,pub_key)
	print len(crypto)
	#私钥加签
	signature = rsa.sign(crypto,private_key,'SHA-1')
	#公钥验签
	if rsa.verify(crypto,signature,pub_key):
		#私钥解密
		decrypt = rsa.decrypt(crypto,private_key)
		print decrypt 
		return HttpResponse("You're at the openapi get .<br /> encrypt:"+crypto+"<br /> decrypt:"+decrypt)
	else:
		return HttpResponse("invilate") 
