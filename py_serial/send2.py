import serial
import time
from datetime import datetime
import threading
import os
import sys
# import lock
# import signal

running = True
received_data = []  # 存储接收到的数据
lock = threading.RLock()
# 接收数据的函数
def receive_data(ser):
    with open('recv2.log', 'a') as log_file:
        while running:
            # start_time = time.time()  # 记录开始时间
            # while time.time() - start_time < 0.1:  # 发送100ms
                try:
                    # lock.acquire()
                    # ser.reset_input_buffer()
                    data = ser.readline().decode()
                    # data = ser.read_all()
                    # lock.release();
                    # data = data.decode('utf-8')
                    # if 'Send1' not in data:
                    #     continue
                    print(f"Received: {data}")
                    received_data.append(data)  # 将接收到的数据添加到列表中
                    log_file.write(data)
                    log_file.flush()  # 确保数据被写入
                except Exception as e:
                    print(f"Receive Error: {e}")
                time.sleep(0.1)

# 发送数据的函数
def send_data(ser):
    counter = 0
    ser.reset_input_buffer()
    # with open('send.log', 'a') as log_file:
    while running:
        # start_time = time.time()  # 记录开始时间
        # while time.time() - start_time < 0.1:  # 发送100ms
            try:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                data = f"Send2: {counter}, Time: {current_time}, Time: {current_time}\n"
                # lock.acquire()
                ser.write(data.encode('utf-8'))
                # ser.reset_input_buffer()
                # lock.release()
                # print(data)
                    # log_file.write(data + '\n')
                    # log_file.flush()  # 确保数据被写入
                counter += 1  # 递增计数
                time.sleep(0.1)  # 每秒发送一次
            except Exception as e:
                print(f"Send2 Error: {e}")


# def signal_handler(sig, frame):
#     print('You pressed Ctrl+C!')
#     sys.exit(0)


# 主函数
if __name__ == "__main__":

    # signal.signal(signal.SIGINT, signal_handler)

    ser = serial.Serial('COM8', 9600)  # 打开COM7，波特率9600

    # 创建线程来接收数据
    receive_thread = threading.Thread(target=receive_data, args=(ser,))
    receive_thread.daemon = True  # 将线程设为守护线程
    receive_thread.start()

    # send_data(ser)
    # time.sleep(0.1)
    try:
    # 直接在主线程中发送数据
        send_data(ser)
    except KeyboardInterrupt:
        print("Exiting program...")
        running = False

        with open('recv2.log', 'w') as log_file:
            for line in received_data:
                if 'Send2' not in line:  # 如果不包含'send1'
                    log_file.write(line + '\n')  # 写入保留的数据
            sys.exit(0)

    receive_thread.join()
