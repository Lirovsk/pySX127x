import serial


ser = serial.serial('/dev/serial10', 115200)

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode().rstrip()
        print("Received data: ", data)
# envio de data para o ESP32
ser.write(b"Hello, ESP32!/n")