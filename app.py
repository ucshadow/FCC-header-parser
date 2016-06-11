from flask import Flask
from flask import request
from flask import jsonify
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'kittens')

@app.route("/", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr,
                    'language': request.headers.get('Accept-language'),
                    'User-Agent': request.headers.get('User-Agent')}), 200

if __name__ == "__main__":
    app.run()
