from flask import Flask, request, jsonify, send_file, render_template, send_from_directory
# from gtts import gTTS
import os
import pyttsx3

app = Flask(__name__)

# Function to speak out the given text and save the audio file
def speak(text):
    # tts = gTTS(text=text, lang='en')
    # tts.save("static/output.mp3")
    
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def process_command(command, selectedOption):
    print("Received command:", command)
    command_lower = command.lower()
    #print("Lowercased command:", command_lower)
    #print("Selected option @@@", selectedOption)

    if 'Fans' in selectedOption:
        if 'turn-on' in command_lower:
            response = "Turning on the Fans..."
        elif 'turn-off' in command_lower:
            response = "Turning off the Fans..."
        else:
            response = "Controlling Fans..."

    elif 'Lights' in selectedOption:
        if 'turn-on' in command_lower:
            response = "Turning on the lights..."
        elif 'turn-off' in command_lower:
            response = "Turning off the lights..."
        else:
            response = "Controlling lights..."

    elif 'AC' in selectedOption:
        if 'on' in command_lower:
            response = "Turning on the air conditioner..."
        elif 'off' in command_lower:
            response = "Turning off the air conditioner..."
        else:
            response = "Controlling air conditioner..."
            
    elif 'Temperature' in selectedOption:
        response = "Adjusting temperature..."
    elif 'Doors' in selectedOption:
        response = "Controlling doors..."
    elif 'Music' in selectedOption:
        response = "Playing music..."
    elif 'Sound' in selectedOption:
        response = "Controlling sound systems..."
    elif 'Others' in selectedOption:
        response = "Controlling other devices..."
    else:
        response = "Sorry, I couldn't understand that command."
        
    print("Response:", response)
    return response

# Route to serve the HTML page
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e), 500  # Return the error message and 500 status code

# Route to handle voice commands
@app.route('/voice-command', methods=['POST'])
def voice_command():
    try:
        data = request.get_json()
        #print("data value@@",data)
        command = data['command']
        selectedOption =data['selectedOption']
        print(command)
        if command:
            response = process_command(command, selectedOption)
            print("output", response)
            speak(response)
            return jsonify({'response': response})
        else:
            return jsonify({'response': "No command received."}), 400
    except Exception as e:
        return str(e), 500  # Return the error message and 500 status code

# Route to serve the audio file
# @app.route('/audio')
# def play_audio():
#     try:
#         return send_file('static/output.mp3', as_attachment=True)
#     except Exception as e:
#         return str(e), 500  # Return the error message and 500 status code

if __name__ == '__main__':
    app.run(debug=True)

