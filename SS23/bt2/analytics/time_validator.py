import datetime

def parse_and_inspect_date(date_str):
    """Bẫy lỗi ngày tháng không hợp lệ bằng try-except."""
    try:
        valid_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return valid_date
    except ValueError:
        return None