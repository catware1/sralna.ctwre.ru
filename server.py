
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from flask_cors import CORS
from time import ctime

app = Flask(__name__)
CORS(app)

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

@app.route('/') # <input type="text" size="40">
def hello_world():
    return f'''<h1>Welcome to sralna.ctwre.ru.</h1><h3>Серверное время - {ctime()}</h3><h3>А давай ты загрузишь свой высер, А?</h3><form name="username" method="get" action="upload">
  <p><b>Ваше имя:</b><br>

   <textarea name="username" cols="40" rows="3"></textarea>
  </p>
  <p>Текст для щит(а)<Br>
   <textarea name="text" cols="40" rows="3"></textarea></p>
  <p><input type="submit" value="Отправить"></p>
 </form><h3>Txt файл с высерами:</h3><pre>{readff("sex.txt")}'''

@app.route("/upload", methods=['GET'])
def upl():
    username = str(request.args.get("username"))
    text = str(request.args.get("text"))
    pluswrite(f"Пользователь: {username}, время: {ctime()}, текст ======\n{text}\n=============================================\n\n", "sex.txt")
    return """<head>
<meta http-equiv="refresh" content="1;URL=http://sralnactwreru.pythonanywhere.com" />
</head><body><h1>Запись успешно загружена. Редиректинг...........!!!</h1></body>"""
