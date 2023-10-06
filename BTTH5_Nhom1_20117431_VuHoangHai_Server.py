# Viết ứng dụng truyền thông Client – Server (TCP) theo mô tả sau:
# Server:
# -  Cung cấp danh sách các dịch vụ:
# 1.     Đảo ngược chuỗi đồng thời in hoa ký tự đầu của mỗi từ
# 2.     Đếm số lần xuất hiện của một từ bất kỳ trong chuỗi
# 3.     Thoát
# -       Server có thể xử lý đồng thời yêu cầu từ nhiều client. (chưa cần làm)
# -       Kiểm tra ngắt kết nối.

# Client:
# -       Kết nối tới server qua địa chỉ IP và port được cung cấp
# -       Nhập chuỗi, sau đó chọn dịch vụ. Nhập từ cần đếm (hoặc Chọn dịch vụ, sau đó nhập chuỗi và nhập từ cần đếm)
# -       Hiển thị ra màn hình kết quả xử lý của server.
# -       Kiểm tra ngắt kết nối.
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


def reverseAndUppercase(s):
    str = ""
    for i in range(0, len(s)):
        if s[i-1] == " ":
            str = s[i].upper() + str
        else:
            str = s[i].lower() + str
    return str


def countWord(str, word):
    # Sử dụng phương thức count() để đếm số lần xuất hiện của từ trong chuỗi
    count = str.lower().count(word.lower())
    return count


while True:
    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode()
    option_str = f"1.     Đảo ngược chuỗi đồng thời in hoa ký tự đầu của mỗi từ\n" + \
        f"2.     Đếm số lần xuất hiện của một từ bất kỳ trong chuỗi\n" + f"3.     Thoát\n"
    client_socket.send(option_str.upper().encode())
    option = client_socket.recv(1024).decode()
    if option == "3":
        break
    elif option == "1":
        client_socket.send(reverseAndUppercase(data).encode())
    elif option == "2":
        word = client_socket.recv(1024).decode()
        client_socket.send(str(countWord(data, word)).encode())

# Đóng kết nối
client_socket.close()
server_socket.close()
