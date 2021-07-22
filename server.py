# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, abort, current_app
from flask_cors import CORS
from time import time
import textwrap

app = Flask(__name__)
CORS(app)

ALLOWED_CHARS=list(" ёЁйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()!\"№;%:?*()-_=+}{:\"?></.,;'][")
ALLOWED_CHARS.append("\\n")

Suspic = [
    {
    "IP": "none",
    "LastPost": time(),
    "Trys": 0
    }
    ]
Suspic_IPS = []

FontsStyle="""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500&d..');
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@500&display=swap');
* { font-family: 'Inter', sans-serif; }
pre, code {
	font-family: 'Roboto Mono', monospace;
}
</style>"""

Scripts = {
"AutoUpdate":
    """
let xhr = new XMLHttpRequest();
while(true){
xhr.open('GET', '/getfile');
xhr.send();
let responseObj = xhr.response;
  document.getElementById("kek").innerHTML = responseObj.message;
}
    """
    }

def writeto(text, target):
    file = open(str(target), 'w', encoding='utf-8')
    file.write(str(text))
    file.close()

def readff(file): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except:
        return None

def pluswrite(text, target):
    file = open(str(target), 'a', encoding='utf-8')
    file.write(str(text))
    file.close()

ip_ban_list = readff("/home/sralnactwreru/Blocked_IPS.txt").split(",")

@app.route('/') # <input type="text" size="40">
def hello_world():
    ip_ban_list = readff("/home/sralnactwreru/Blocked_IPS.txt").split(",")
    ip = str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    if ip not in ip_ban_list:
        return f'''<meta charset="UTF-8">{FontsStyle}
<title>сральня сереги</title>
<center>
    <h1>СРАЛЬНЯ ЮРЫ (СОВМЕСТНО С АРТЕМОМ) НАХУЙ</h1>
    <h3>Предупреждение - 1 пост менее чем за 15 секунд карается предупреждением. Максимальное кол-во предупреждений - 5.</h3>
    <h3>Максимальный размер текста - 1000 символов. Если он больше, то он обрежется до 1000 символов.</h3>
</center>
</head>
<body>
<center>
<p id="form-1">
<form action="upload" method="get">
      <h6>кто вы:</h6>
      <input type="text" name="username">
    <h6>ваш высер:</h6>
    <textarea name="text"></textarea>
    <br>
    <br>
    <button type="submit">Высрать</button>
</form></p><h3>Txt файл с высерами:</h3><pre id="kek">{readff("serega.txt")}</pre></center></body>'''
    else:
        return f'''<meta charset="UTF-8">{FontsStyle}
<title>сральня сереги</title>
<center>
<br><br><br><br><br><br>
    <h1>СРАЛЬНЯ ЮРЫ (СОВМЕСТНО С АРТЕМОМ) НАХУЙ</h1>
    <h3>Предупреждение - 1 пост менее чем за 15 секунд карается предупреждением. Максимальное кол-во предупреждений - 5.</h3>
    <h3>Максимальный размер текста - 1000 символов. Если он больше, то он обрежется до 1000 символов.</h3>
</center>
</head>
<body>
<center>
<p id="form-1"
ВЫ ЗАБАНЕНЫ НАХУЙ ПО ПРИЧИНЕ ПИДОРАС БЛЯДЬ<br><br><b>Если вы считаете, что произошла ошибка: напишите vk.com/catweird следующее письмо: <br>Здравствуй. Меня забанили на Сральне Юрия и Артемия. Прошу разбань. Мой IP - {ip}.</b></p><h3>Txt файл с высерами:</h3><pre id="kek">{readff("serega.txt")}</pre></center></body>'''
@app.route("/upload", methods=['GET'])
def upl():
    ip_ban_list = readff("/home/sralnactwreru/Blocked_IPS.txt").split(",")
    ip = str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))

    #
    # Catware Suspicious Users Detection System
    #

    if ip not in Suspic_IPS:
        Suspic_IPS.append(ip)
        Suspic.append({"IP": ip, "Trys": 0, "LastPost": time()})

    for x in Suspic:
        if x["IP"] == ip:
            if "python" in str(request.headers.get('User-Agent')):
                x["Trys"] += 1
            if time() - x["LastPost"] < 15:
                x["Trys"] += 1
                if x['Trys'] == 5:
                    ip_ban_list.append(ip)
                    writeto(",".join(ip_ban_list), "/home/sralnactwreru/Blocked_IPS.txt")
                    pluswrite(f"------------------------------\nCSUDS:\n Catware Suspicious Users Detection System забанила IP: {ip}\n------------------------------\n\n", "serega.txt")

    if ip not in ip_ban_list and "python" not in str(request.headers.get('User-Agent')).lower():
        username = str(request.args.get("username"))
        text = str(request.args.get("text")).replace("<", "&lt;").replace(">", "&gt;")[:1000]
        nb = ""
        for x in text:
            if x in ALLOWED_CHARS:
                nb += x
        text = nb
        for x in range(len(text)):
            if text.startswith(" "):
                text = text[1:]
            if text.endswith(" "):
                text = text[:-1]
        text = textwrap.fill(text, width=25)
        #pluswrite(f"------------------------------\n{username}:\n {text}\n------------------------------\n\n", "serega.txt")
        pluswrite(f""" ═╣ {username} ╠══════════════════════════════
 {text}
 ═════════════════════════════════════════════
""", "serega.txt")
        return f"""<head>{FontsStyle}
<meta http-equiv="refresh" content="1;URL=http://sralnactwreru.pythonanywhere.com" />
</head><body><h1>взлом казино 777...</h1></body>"""
    else:
        return f"""<head>{FontsStyle}
<meta http-equiv="refresh" content="1;URL=http://sralnactwreru.pythonanywhere.com" />
</head><body><h1>Сука иди нахуй я тебе запретил срать!!!!</h1></body>"""

@app.route("/get-my-ip")
def gmi():
    return f"<h1>{str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))}</h1>"

@app.route("/getfile")
def gf():
    return readff("serega.txt")

@app.route("/is-banned")
def isb():
    ip = str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    if ip not in ip_ban_list:
        return "false"
    else:
        return "true"
