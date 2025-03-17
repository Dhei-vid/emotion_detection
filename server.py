from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze: 
        return "Invalid input! Try again."

    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion_score = response['dominant_emotion']
    
    return (f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, "
        f"'joy': {joy_score} and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion_score}.")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)