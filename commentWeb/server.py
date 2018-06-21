from flask import Flask, request, send_from_directory, send_file, jsonify
from utils import  db

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'])
def index():
    return send_file('static/index.html')

@app.route('/static/<path:path>', methods=['GET'])
def send_static(path):
    return send_from_directory('static', path)

@app.route('/comment/<int:begin_id>/<int:offset>', methods=['GET'])
def get_comment(begin_id, offset):
    fields = ['id','game_name','user_name','comment_time','content','score','type','emotion']
    return jsonify(db.get_comment(fields, begin_id, offset))

@app.route('/last_comment/<int:end_id>/<int:offset>', methods=['GET'])
def last_comment(end_id, offset):
    fields = ['id','game_name','user_name','comment_time','content','score','type','emotion']
    return jsonify(db.last_comment(fields, end_id, offset))

@app.route('/comment', methods=['POST'])
def update_comment():
    j = request.get_json()
    if 'emotion' in j:
        field = 'emotion'
        value = j['emotion']
    elif 'type' in j:
        field = 'type'
        value = j['type']
    else:
        return jsonify({'res':'error', 'paras':j})
    if db.update_comment(j['id'], field, value):
        return jsonify({'res': 'ok'})   
    else:
        return jsonify({'res':'error', 'paras':j})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
