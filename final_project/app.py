from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def emotion():
    data = request.json
    text = data.get('raw_document', {}).get('text', '')
    # Here you would call the Watson service or process the text
    return jsonify({"response": f"Text received: {text}"})

if __name__ == '__main__':
    app.run(debug=True)
