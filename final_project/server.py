from flask import Flask, render_template, send_from_directory, request, jsonify
from emotion_detection import EmotionDetection  # Ensure this import matches your module

app = Flask(__name__, static_folder='static', template_folder='templates')

# Initialize your emotion detector
emotion_detector = EmotionDetection()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    # Get the statement from the POST request
    data = request.json
    statement = data.get('statement', '')
    
    # Process the statement using the emotion detector
    results = emotion_detector.detect_emotion(statement)
    
    # Determine the dominant emotion
    dominant_emotion = max(results, key=results.get)
    
    # Prepare the response in the desired format
    response = {
        "anger": results.get("anger", 0),
        "disgust": results.get("disgust", 0),
        "fear": results.get("fear", 0),
        "joy": results.get("joy", 0),
        "sadness": results.get("sadness", 0),
        "dominant_emotion": dominant_emotion
    }
    
    # Format the response message
    response_message = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    
    return jsonify(response_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
