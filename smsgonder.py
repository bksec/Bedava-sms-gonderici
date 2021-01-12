import os ,proxy ,time ,json ,requests
from renkler import *

def sil():
    sistem = os.name

    if os.name == 'nt':
        sil = os.system('cls')
    else:
        sil = os.system('clear')
    sil
sil()
print("""{}
                          .--.
                          |  |
                          |  |
                          |  |
                          |  |
         _.-----------._  |  |          
      .-'     ___       `-.  |     
    .'      .'   `.        `.|
   ;        :     :          ;      {}Ucretsiz sms gonderici{}    
   |        `.___.'          |         
   |                         |      {}yazar = Berkay Kucuk{}         
   |  ASELSAN         1919   |             
   | .---------------------. |      {}versiyon = 0.1{} 
   | |                     | |
   | |{}  github.com/bksec{}   | |      
   | |    {}  ,_, {}           | |
   | |    {} (O,O){}           | |
   | |    {} (   ) {}          | |
   | |    {} -"-"- {}          | |
   | |                     | |
   | `---------------------' |
   |                         |
   |                __       |
   |  ________  .-~~__~~-.   |
   | |___C___/ /  .'  `.  \  |
   |  ______  ;   : OK :   ; |
   | |__A___| |  _`.__.'_  | |
   |  _______ ; \< |  | >/ ; |
   | [_=

""".format(yesil,siyah,yesil,siyah,yesil,siyah,yesil,siyah,yesil,gri,yesil,gri,yesil,gri,yesil,gri,yesil)
)
time.sleep(4)
def bekleme():
    bar = [
    " [=     ]",
    " [ =    ]",
    " [  =   ]",
    " [   =  ]",
    " [    = ]",
    " [     =]",
    " [    = ]",
    " [   =  ]",
    " [  =   ]",
    " [ =    ]",
]
    i = 0

    while i<45:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2)
        i += 1    

sil()
while True:
    kabul = str(input(f"{kirmizi}Bu toolu saka ve eglence amacli yapilmistir yapilan hicbir seyden sorumluluk kabul etmiyorum . Bu amac dogrultusunda kullancagina soz veriyor musun {siyah}[e/h]? "))
   
    if kabul.lower().startswith("e"):
        print(yesil,"*Bir numaraya gunde 1 mesaj atma hakkin var\n *Mesajda link atmak yasak ")
        time.sleep(3)
        break
    elif kabul.lower().startswith("h"):
        print(siyah,f"{kirmizi}Uzgunum,Lutfen bidaha dusun")
        exit()
    else:
        print(kirmizi,f"{kirmizi}Anliyamadim") 
         
           
sil()
telefon_no = str(input(f"{mor}ulke koduyla telefon numarasini giriniz{pembe} or(+905xxxxxxxxx)\n"))


onay = True

while onay:


    mesaj = str(input(f"{siyah}Gondermek istedginiz mesaji giriniz\n"))
    sil()
    cevap = str(input(f"{mavi}==>{mesaj}\n{siyah}Mesajinizi onayliyor musunuz ? {kirmizi}[e/h] "))
    sil()

    if cevap.lower().startswith("e"):
        print(f"{kirmizi}Proxy aliniyor")
        bekleme()
        onay = False
    elif cevap.lower().startswith("h"):
        print(siyah,f"{kirmizi}Tekrardan mesajiniz giriniz")
        
    else:
        print(kirmizi,f"{kirmizi}Anliyamadim")




istek_gitti = True
while istek_gitti:

    proxy = proxy.Proxy()
    http = 'socks5://'+proxy
    https = 'socks5://'+proxy

    
    mesajurl = 'https://textbelt.com/text'

    
    istek = requests.get(mesajurl,{
    'phone': telefon_no,
    'message': mesaj,
    'key': 'textbelt',
    },proxies={'http':http,'https':https},headers={'Content-Type': 'application/json'})


    
    istekcevap = istek.json()
    mesaj_gitti = istekcevap['success']
    

    if istek.status_code == 200:
        break

    else:
        istek_gitti = True

if mesaj_gitti == True:
    
    print(f"{yesil}  Mesajiniz basariyla iletildi\n")
    print("""
 
        .@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
        @@ @@@,                @@@  @@   
        @@   ,@@@           ,@@     @@
        @@       @@@      @@#       @@
        @@      @@@,@@&@@@ @@       @@
        @@   ,@@             @@     @@
        @@  @@                 @@   @@
        @@@@                     @@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@

{}"""
.format(sifirla))


elif mesaj_gitti ==False:
    hata = str(istekcevap['error'])
    print(f"{kirmizi}Bir Hatayla karsilasildi. Hata : {hata}{sifirla}")
