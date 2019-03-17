from flask import Flask, request
from nlp_service import NlpService
import random
app = Flask(__name__)


@app.route("/post", methods=['POST'])
def post():
    res_answer = request.form['answer']
    num = random.randint(0, 100)
    response_answer = NlpService(res_answer)
    print(num)
    if num > 30:
        return response_answer.get_analized_answer()
    else:
        return response_answer.get_response_answer()

if __name__ == '__main__':
    # http://localhost:5000/ でアクセスできるよう起動
    app.run(host='localhost', port=5000)
