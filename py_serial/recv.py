import serial
import time

ser = serial.Serial('COM8', 9600)  # 打开COM7，波特率9600
with open('recv.log', 'a') as log_file:
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            print(data)
            log_file.write(data + '\n')
            log_file.flush()  # 确保数据被写入
        except Exception as e:
            print(f"Error: {e}")
