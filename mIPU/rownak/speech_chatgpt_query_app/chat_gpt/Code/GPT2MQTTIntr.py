import paho.mqtt.client as mqtt
import json
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load and prepare GPT-2 model
model_name = "gpt2"
model_save_path = "./MODELS/GPT2"
model = GPT2LMHeadModel.from_pretrained(model_save_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_save_path)
model.eval()

def generate_text(prompt, max_length=50, temperature=0.7):
    input_ids = tokenizer.encode(prompt, return_tensors = "pt")
    output = model.generate(input_ids, max_length=max_length, temperature=temperature, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe("SPEECH_TO_TEXT")

def on_message(client, userdata, msg):
    message = json.loads(msg.payload)
    print("Received Message : ", message)
    generated_story = generate_text(message, max_length=50, temperature=0.7)
    print("Response:")
    print(generated_story)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT broker
    client.connect("10.0.0.7", 1883, 60)

    # Start the loop
    client.loop_forever()

if __name__ == "__main__":
    main()
