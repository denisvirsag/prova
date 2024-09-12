from flask import Flask, jsonify, request

app = Flask(__name__)

# Simuliamo alcuni dati che potremmo recuperare
url_data = {
    "example": {
        "title": "Example Domain",
        "description": "This domain is established to be used for illustrative examples in documents."
    },
    "test": {
        "title": "Test Site",
        "description": "A test site for demonstrating purposes."
    }
}

@app.route('/')
def h():
    print('hello world!')

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    url = request.args.get('url')
    if url in url_data:
        return jsonify(url_data[url])
    else:
        return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
