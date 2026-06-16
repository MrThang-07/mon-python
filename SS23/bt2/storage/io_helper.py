import os

def safe_create_dir(path):
    """Tạo thư mục lồng nhau an toàn, nếu có rồi thì bỏ qua."""
    os.makedirs(path, exist_ok=True)