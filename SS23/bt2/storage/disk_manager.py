import math

def calculate_disk_blocks(size_bytes, block_size=4096):
    """Tính số khối phân vùng ổ đĩa bằng cách chia rồi làm tròn lên."""
    return math.ceil(size_bytes / block_size)