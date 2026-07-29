class Product:
    def __init__(self, p_id, name, price, quantity, discount):
        self.id = p_id
        self.name = name
        self.price = float(price)
        self.quantity_sold = int(quantity)
        self.discount = float(discount)
        self.total_revenue = 0.0
        self.revenue_type = ""
        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        # Tính doanh thu, nếu nhỏ hơn 0 thì gán bằng 0
        rev = (self.price * self.quantity_sold) - self.discount
        self.total_revenue = rev if rev > 0 else 0

    def classify_revenue(self):
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"