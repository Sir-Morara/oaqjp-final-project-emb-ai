import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        response_dict = response.json() 

        # Extract emotions from the nested JSON structure
        if 'emotionPredictions' in response_dict and len(response_dict['emotionPredictions']) > 0:
            emotions = response_dict['emotionPredictions'][0]['emotion']
            
            # Print debug information
            print("Response JSON:", response_dict) 
            print("Emotions Dictionary:", emotions)

            # Determine the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)
            
            return {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }
        else:
            return {"error": "No emotion predictions found in the response"}
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
