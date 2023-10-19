# Sử dụng Socket TCP viết ứng dụng Client-Server theo mô tả:
#  *Server:
#     - Lưu trữ tập tin data5.txt với nội dung:
#         4 5 6 8 9 15
#         5 7 8 15 24 1
#         9 5 4 4 2 56
#     - Cung cấp 2 dịch vụ Tổng và Tích
#     - Tính Tổng & Tích từng hàng và trả về cho Client

# Client:
#   Kết nối tới Server
#   CHọn dịch vụ do Server cấp qua menu
#   Hiển thị kết quả Server trả về
import socket

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Đặt địa chỉ và cổng
host = socket.gethostname()  # Địa chỉ IP của máy chủ
port = 12345       # Cổng của máy chủ
server_address = (host, port)

# Liên kết (bind) socket với địa chỉ và cổng
server_socket.bind(server_address)

# Lắng nghe kết nối từ client
server_socket.listen(5)
print(f"Đang lắng nghe tại {host}:{port}...")

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()
print(f"Kết nối từ: {client_address}")


def calSum():
    s = ""
    import numpy as np
    with open('data5.txt') as f:
        for line in f:
            i = 1
            c = line.strip().split(' ')
            res = [eval(i) for i in c]
            array = np.array(res)
            s = s + \
                "- Tổng của hàng thứ {0} là:".format(
                    i) + (str)(np.sum(array)) + "\n"
            i = i + 1
    return s.strip()


def calMultiple():
    import numpy as np
    s = ""
    with open('data5.txt') as f:
        for line in f:
            i = 1
            c = line.strip().split(' ')
            res = [eval(i) for i in c]
            array = np.array(res)
            s = s + \
                "- Tích của hàng thứ {0} là:".format(
                    i) + (str)(np.prod(array)) + "\n"
            i = i + 1
    return s.strip()


while True:
    option_str = f"\n1.     Tổng\n" + \
        f"2.     Tích\n" + f"3.     Thoát\n"
    client_socket.send(option_str.upper().encode())
    option = client_socket.recv(1024).decode()
    if option == "3":
        break
    elif option == "1":
        client_socket.send(calSum().encode())
    elif option == "2":
        client_socket.send(calMultiple().encode())

# Đóng kết nối
client_socket.close()
server_socket.close()
