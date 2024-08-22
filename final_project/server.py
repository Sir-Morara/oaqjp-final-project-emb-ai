from flask import Flask, render_template, send_from_directory, request, jsonify
from emotion_detection import emotion_detector  # Import the updated emotion_detector function

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files."""
    return send_from_directory(app.static_folder, filename)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handle emotion detection requests."""
    data = request.json
    statement = data.get('statement', '')
    
    results = emotion_detector(statement)
    
    if results['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400
    
    response_message = (
        f"For the given statement, the system response is 'anger': {results['anger']}, "
        f"'disgust': {results['disgust']}, 'fear': {results['fear']}, 'joy': {results['joy']} "
        f"and 'sadness': {results['sadness']}. The dominant emotion is {results['dominant_emotion']}."
    )
    
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
