from flask import Flask, render_template
import requests
import json
print('================================================first task==========================================================================================')
# Создайте Flask-сервер, добавьте в него роутер '/nbu', который отправит запрос на апи НБУ,
# получит и обработает ответ, и отдаст данные по курсам. Используйте формат данных для ответа из ДЗ 11
#Код опубликуйте на gitlab или github, на проверку - ссылку на репозиторий#


app = Flask(__name__)

@app.route("/")
def main():
    try:
        response = requests.get("http://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json//")
        if response.status_code == 200:
            res = response.text
        return render_template('home_task.html', res=res)
    except:
        raise EOFError

if __name__ == "__main__":
   app.run(debug=True)