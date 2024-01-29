To run this mIPU Project we need two raspberry pi 4's

Let's give names to boards 
1. RPI-1
2. RPI-2

RPI-1 is for runnig Speech to text models and send it to RPI-2
RPI-2 will receive text input and Runs ChatGPT-2 Model locally and generates text based output

After cloning lab518 we need to set environment to run this project 

1. Setting RPI-1 Environment 
Since RPI-1 runs Speech to text based models we need all the required speech to text libraries to be installed
Dowloand virtual envirinment from https://drive.google.com/file/d/1sx0C3tFfCeYUyMCyhwGSY3FN_vyFWfT4/view?usp=drive_link
This gives venv32.tar tar file unzip it using `$ tar -xvf venv32.tar` command 
Activate virtual environment using `$ source <path to venv32>/bin/activate`
Now goto path `lab518/mIPU/rownak/speech_chatgpt_query_app/speech_text`
Run `$ python SpeechToText.py -f <audio_file_path>`
eg : `$ python SpeechToText.py -f ./audios/output.wav`



2. Setting RPI-2 Environment 
Since RPI-2 runs chat GPT model we need all the libraries required for GPT to be installed
NOTE: RPI-2 should be running a 64 bit RPI OS
Download venv64 from Google Drive https://drive.google.com/file/d/1tUQU7X67-YOLw85DYdE9G3fgY4Nq7Ag2/view?usp=drive_link
This gives venv64.tar file unzip it using `$ tar -xvf venv64.tar` command 
Download models from Google Drive https://drive.google.com/file/d/1uM5mzV32A6hH27BL4JqNHK-3Jb-fy536/view?usp=drive_link
This gives MODELS.tar file unzip it using `$ tar -xvf MODELS.tar` command
Place this MODELS folder into `mIPU/rownak/speech_chatgpt_query_app/chat_gpt/Code` folder 
Activate virtual environment using `$ source <path to venv364>/bin/activate`
NOTE: MQTT (Mosquitto Library should be install and Mosquitto broker should be running before performing next steps)
Follow https://www.arubacloud.com/tutorial/how-to-install-and-secure-mosquitto-on-ubuntu-20-04.aspx for installing and running mosquitto broker 
Helpful steps : `sudo apt update -y && sudo apt install mosquitto mosquitto-clients -y`
Helpful steps : `sudo systemctl status mosquitto`
If Mosquitto broker is active, verify the IP address in the code both `SpeechToText.py` and `GPT2MQTTIntr.py` should have the IP address
of RPI-2 which is runnig the broker, and both RPI 1 & 2 should be present in same network 
Now Run `$ python GPT2MQTTIntr.py` command


Other Helpful steps:
To record audio files with compatible `$ rec -c 1 -b 16 -r 48000 ./audios/output.wav`
Audio file Specifications to give as input to model
Channels       : 1
Sample Rate    : 48000
Precision      : 16-bit
Duration       : 00:00:03.33 = 159757 samples ~ 249.62 CDDA sectors
File Size      : 320k
Bit Rate       : 768k
Sample Encoding: 16-bit Signed Integer PCM


