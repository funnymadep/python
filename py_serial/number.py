def check_log_file(filename):
    print(filename)
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        previous_number = -1
        non_continuous_numbers = []  # 用于存储不连续的数字

        for line in lines:
            if line.startswith("Send1:"):
                # 提取数字
                number = int(line.split(':')[1].split(',')[0].strip())
                # 检查是否连续
                if number != previous_number + 1:
                    non_continuous_numbers.append(number)
                previous_number = number

        # 输出所有不连续的数字
        if non_continuous_numbers:
            print("Non-continuous numbers found:")
            for number in non_continuous_numbers:
                print(number)
        else:
            print("All numbers are continuous.")

    except FileNotFoundError:
        print("recv.log file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file1 = "recv2_1.log"
    file2 = "recv2_2.log"
    check_log_file(file1)
    print('***************************************')
    check_log_file(file2)
