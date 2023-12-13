Flashing Procedure into Arduino Due
stty -f /dev/cu.usbmodem1401 1200
/Users/sai/Library/Arduino15/packages/arduino/tools/bossac/1.6.1-arduino/bossac -e -w -v --port=cu.usbmodem1401 -b /tmp/temp/Blink.ino.bin

ADC to Volatge Conversion formula 

Voltage = (ADC Reading * Full Scale Voltage) / (2^(Resolution) * PGA)

PGA - programmable gain amplifier 
Full Scale Voltage depends on PGA
Resolution depends on number of bits 16 bits.

 [PGA]  [ Full Scale Volatge ]
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V



[ Steps to setup  RPI ] 
sudo raspi-config # enable i2c
sudo i2cdetect -y 1