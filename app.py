from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/reverse', methods=['POST'])
def reverse_word():
    data = request.get_json()
    if not data or 'word' not in data:
        return jsonify({'error': 'Missing "word" parameter'}), 400
    
    reversed_word = data['word'][::-1]
    return jsonify({'reversed': reversed_word})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
