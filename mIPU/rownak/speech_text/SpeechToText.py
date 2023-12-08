import os
import wave
import json
import argparse
import paho.mqtt.client as mqtt
from vosk import Model, KaldiRecognizer

parser = argparse.ArgumentParser(description ='Provide some wav file')
 
parser.add_argument('-f', '--file', required=True)

args = parser.parse_args()

def get_text_from_voice(audio_file_path, model_path, output_file):
    print("Input file : ", audio_file_path)
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}")
        exit(1)

    wf = wave.open(audio_file_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        exit(1)

    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    text_lst = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            result = json.loads(rec.PartialResult())  # Parse the JSON
            text = result.get("partial", "")
            text_lst.append(text)
            print(text)

    if text_lst:
        txt_str = text_lst[-1]
    else:
        txt_str = ''
    
    client.publish("SPEECH_TO_TEXT", json.dumps(txt_str))

    with open(output_file, "w") as output:
        for text in text_lst:
            output.write(text + "\n")

    return text_lst

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe("none")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print("Received message Req: " + message)
    
if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("10.0.0.5", 1883, 60) 
    audio_file_path = r"/home/lab518/Rownak/project/audios/record.wav"
    model_path = r"/home/lab518/Rownak/project/vosk-model-small-en-us-0.15"
    output_file = r"/home/lab518/Rownak/project/Transcription.txt"
    result = get_text_from_voice(args.file, model_path, output_file)
    print("Transcription Result:", result)
