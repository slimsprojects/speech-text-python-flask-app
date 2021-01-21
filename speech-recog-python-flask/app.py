# create flask app where user uploads a .wav file and gets a text transcript using speech recognition module

from flask import Flask, render_template, request, redirect
import speech_recognition as sr


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    transcript = ''

    if request.method == "POST":
        print("FORM DATA RECEIVED")


        # if file does not exist  or file name is blank return back to homepage
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)

        # take the file user uploaded
        # create audio file object speech recognization module can understand
        # opening up audio file and reading it in through the recognizer
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)

            transcript = recognizer.recognize_google(data, key=None)
            #print(text)

    return render_template('index.html', transcript=transcript)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

