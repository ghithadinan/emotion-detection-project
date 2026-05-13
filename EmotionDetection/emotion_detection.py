"""Emotion detection module using IBM Watson NLP API."""

import requests


API_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores and dominant emotion."""

    headers = {
        "grpc-metadata-mm-model-id": MODEL_ID
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(
            API_URL,
            json=payload,
            headers=headers,
            timeout=10
        )
    except requests.exceptions.RequestException:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Task 7: Handle invalid input (HTTP 400 Bad Request)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions