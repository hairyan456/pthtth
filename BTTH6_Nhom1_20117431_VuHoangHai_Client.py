import socket
import os

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Đặt địa chỉ và cổng của máy chủ
host = socket.gethostname()  # Địa chỉ IP của máy chủ
port = 12345       # Cổng của máy chủ
server_address = (host, port)

# Kết nối đến máy chủ
client_socket.connect(server_address)

while True:
    file_name = (str(input(f"\nNhập tên file: ")))
    while not os.path.exists(file_name):
        file_name = (
            str(input(f"File không tồn tại! Mời nhập lại: ")))
    client_socket.send(file_name.encode())
    option_str = client_socket.recv(1024).decode()
    print(option_str)
    option = (str(input(f"Mời chọn từ 1-3: ")))
    while (option not in ["1", "2", "3"]):
        option = (str(input(f"Vui lòng chỉ nhập từ 1-3: ")))
    client_socket.send(option.encode())
    if option == "3":
        break
    elif option == "1":
        print(client_socket.recv(1024).decode())
    elif option == "2":
        print(client_socket.recv(1024).decode())
# Đóng kết nối
client_socket.close()
