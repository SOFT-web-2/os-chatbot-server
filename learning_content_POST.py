from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/post',methode = ['POST'])
def post():
    content = request.data.decode('utf-8')
    lines = content.split('\n')

    if len(lines) >= 4:
        title = lines[-4].split(':')[1].strip()
        files = int(lines[-3].split(':')[1].strip())
        author = lines[-2].split(':')[1].strip()
        passcode = lines[-1].split(":")[1].strip()

        if title and files and author and passcode:
            print("title:",title)
            print("files:",files)
            print("author:",author)
            print("passcode:",passcode)

            response = {'message': '게시 성공'}
            return jsonify(response), 201
        else:
            response = {'message': '마지막 3줄에 title, files, author가 존재하지 않음'}
            return jsonify(response), 400
    else:
        response = {'error': '서버 오류'}
        return jsonify(response), 500
