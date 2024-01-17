import serial
import time

# connect to arduino via serial ( COM port may vary )
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

# give 2 seconds to settle up the connection
time.sleep(2)      

def led_on():
    arduino.write(bytes('H', 'utf-8'))

def led_off():
    arduino.write(bytes('L', 'utf-8'))

try:
    while True:
        led_on()
        time.sleep(1)   # led is on for 1 second
        led_off()
        time.sleep(1)   # led is off for 1 second
except KeyboardInterrupt:
    print("Program Terminated!")
finally:
    arduino.close()   # close the serial communication