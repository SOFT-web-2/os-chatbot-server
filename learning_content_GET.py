from flask import Flask, request, jsonify

app = Flask(__name__)

posts = {}

@app.route('/<int:post_id>', methods=['GET', 'DELETE', 'PATCH'])
def manage_post(post_id):
    if request.method == 'GET':
        return get_post(post_id)
    elif request.method == 'DELETE':
        return delete_post(post_id)
    elif request.method == 'PATCH':
        return patch_post(post_id)

def get_post(post_id):
    post = posts.get(post_id)
    if post:
        return jsonify(post), 200
    else:
        return jsonify({'error': '게시글이 존재하지 않음'}), 404

def delete_post(post_id):
    passcode = request.json.get('passcode')
    if not passcode:
        return jsonify({'error': '본문에 passcode 키가 없음'}), 400

    post = posts.get(post_id)
    if post:
        if post['passcode'] == passcode:
            del posts[post_id]
            return jsonify({'message': '삭제 성공'}), 200
        else:
            return jsonify({'error': 'passcode가 틀림'}), 403
    else:
        return jsonify({'error': '게시글이 존재하지 않음'}), 404

def patch_post(post_id):
    passcode = request.json.get('passcode')
    if not passcode:
        return jsonify({'error': '본문에 passcode 키가 없음'}), 400

    operations = request.json.get('operations')
    if not operations:
        return jsonify({'error': '본문에 D, A, R 중 하나도 없음'}), 400

    post = posts.get(post_id)
    if post:
        if post['passcode'] == passcode:
            for op in operations:
                if op.startswith('D'):
                    line, col = map(int, op[2:].split(':'))
                    post['content'][line] = post['content'][line][:col]
                elif op.startswith('A'):
                    line, col = map(int, op[2:].split(':'))
                    text = op[5:]
                    post['content'][line] = post['content'][line][:col] + text + post['content'][line][col:]
                elif op.startswith('R'):
                    line, col = map(int, op[2:].split(':'))
                    text = op[5:]
                    post['content'][line] = post['content'][line][:col] + text
            return jsonify({'message': '수정 성공'}), 200
        else:
            return jsonify({'error': 'passcode가 틀림'}), 403
    else:
        return jsonify({'error': '게시글이 존재하지 않음'}), 404
