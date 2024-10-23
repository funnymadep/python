import serial
import time
from datetime import datetime
import threading
import os
import sys
# import signal

running = True
received_data = []  # 存储接收到的数据

# 接收数据的函数
def receive_data(ser):
    with open('recv1.log', 'a') as log_file:
        while running:
            try:
                data = ser.readline()
                data = data.decode('utf-8')
                print(f"Received: {data}")
                received_data.append(data)  # 将接收到的数据添加到列表中
                log_file.write(data)
                log_file.flush()  # 确保数据被写入
            except Exception as e:
                print(f"Receive Error: {e}")

# 发送数据的函数
def send_data(ser):
    counter = 0
    # with open('send.log', 'a') as log_file:
    while running:
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            data = f"Send1: {counter}, Time: {current_time}, Time: {current_time}\n"
            ser.write(data.encode('utf-8'))
            # print(data)
                # log_file.write(data + '\n')
                # log_file.flush()  # 确保数据被写入
            counter += 1  # 递增计数
            time.sleep(0.1)  # 每秒发送一次
        except Exception as e:
            print(f"Send1 Error: {e}")


# def signal_handler(sig, frame):
#     print('You pressed Ctrl+C!')
#     sys.exit(0)


# 主函数
if __name__ == "__main__":

    # signal.signal(signal.SIGINT, signal_handler)

    ser = serial.Serial('COM7', 9600)  # 打开COM7，波特率9600

    # 创建线程来接收数据
    receive_thread = threading.Thread(target=receive_data, args=(ser,))
    receive_thread.daemon = True  # 将线程设为守护线程
    receive_thread.start()

    # send_data(ser)
    try:
    # 直接在主线程中发送数据
        send_data(ser)
    except KeyboardInterrupt:
        print("Exiting program...")
        running = False

        with open('recv1.log', 'w') as log_file:
            for line in received_data:
                if 'Send1' not in line:  # 如果不包含'send1'
                    log_file.write(line + '\n')  # 写入保留的数据
            sys.exit(0)

    receive_thread.join()
