import socket

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Đặt địa chỉ và cổng của máy chủ
host = socket.gethostname()  # Địa chỉ IP của máy chủ
port = 12345       # Cổng của máy chủ
server_address = (host, port)

# Kết nối đến máy chủ
client_socket.connect(server_address)

while True:
    message = input(f"Nhập chuỗi: ")

    # Gửi dữ liệu đến máy chủ
    client_socket.send(message.encode())
    option_str = client_socket.recv(1024).decode()
    print(option_str)
    option = (str(input(f"Mời chọn từ 1-3: ")))
    if option not in ["1", "2", "3"]:
        while (option not in ["1", "2", "3"]):
            option = (str(input(f"Vui lòng chỉ nhập từ 1-3: ")))
    client_socket.send(option.encode())
    if option == "3":
        break
    elif option == "1":
        print(client_socket.recv(1024).decode())
    elif option == "2":
        word = (str(input(f"Nhập từ muốn đếm trong chuỗi: ")))
        client_socket.send(word.encode())
        print("Số lần xuất hiện của từ {0} trong chuỗi là: {1}".format(
            word, client_socket.recv(1024).decode()))
# Đóng kết nối
client_socket.close()
