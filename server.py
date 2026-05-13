"""Flask server for Emotion Detection application."""

from flask import Flask, request, render_template_string

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main page."""
    with open("static/index.html", "r", encoding="utf-8") as file:
        return render_template_string(file.read())


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze text and return formatted emotion response."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}</b>."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)