import requests
import json

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

        print("Response JSON:", response_dict) 
        
        emotions = {
            'anger': response_dict.get('anger', 0),
            'disgust': response_dict.get('disgust', 0),
            'fear': response_dict.get('fear', 0),
            'joy': response_dict.get('joy', 0),
            'sadness': response_dict.get('sadness', 0),
        }
        
        print("Emotions Dictionary:", emotions)

        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
