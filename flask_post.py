from flask import Flask, request
from nlp_service import NlpService
app = Flask(__name__)


@app.route("/post", methods=['POST'])
def post():
    hoge = request.form['answer']
    nlp_response = NlpService(hoge)
    return nlp_response.get_response_answer()


if __name__ == '__main__':
    # http://localhost:5000/ でアクセスできるよう起動
    app.run(host='localhost', port=5000)
