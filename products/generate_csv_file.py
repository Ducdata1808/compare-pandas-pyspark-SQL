import pandas as pd
import random
import uuid 
from datetime import datetime, timedelta

number_of_products = 100

order_id = [f"pro_{str(uuid.uuid1())[:8]}" for _ in range(number_of_products)]
print(order_id[: 10])

surname = ["Nguyen", "Le", "Do", "Tran", "Pham", "Dang", "Vo", "Ly"]
middle_name = ["Van", "Thi", "Hoang", "Duc", "Trong", "Trung", "Gia", "Xuan", "Ba"]
name = ["Duc", "Hoang", "Phu", "Viet", "Tuan", "Uy", "Huy", "Khoa", "Dung", "Vinh", "Thanh", "Phat", "Khang", "Bao", "Thu", "Giang", "Mai", "Hoa", "Lieu", "Truc", "Ly", "Y", "Huong", "Binh", "Tran", "Phong", "Vien", "Huyen", "Dat", "An", "Anh", "Minh", "Thuy", "Tai", "Nghia", "Khanh", "Trang", "Quynh", "Dung", "Hanh"]
customer = [(random.choice(surname) + " " + random.choice(middle_name) + " " + random.choice(name)) for _ in range(number_of_products)]
print(customer[: 10])

products_name = ["Bag", "Pencil", "Table", "Chair", "Lamp", "Mirror", "Fan", "Shoes", "Mouse", "Book", "Gun", "Bomb", "Key", "Soap", "bed", "power outlet", "lock", "keyboard", "pipe", "cover", "comb", "glass", "bowl"]
price_per_unit = [150000, 10000, 300000, 240000, 120000, 80000, 280000, 150000, 135000, 12000, 400000, 700000, 35000, 30000, 500000, 165000, 80000, 210000, 240000, 18000, 21000, 38000, 27000]

product = [" " for _ in range(number_of_products)]
price = [0 for _ in range(number_of_products)]
for i in range(number_of_products):
    index = random.randint(0, len(products_name) - 1)
    product[i] = products_name[index]
    price[i] = price_per_unit[index]
quantity = [random.randint(1, 10) for _ in range(number_of_products)]
print(product[:10])
print(price[:10])
print(quantity[:10])

def generate_random_dates(start_date, end_date, n):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = end - start

    random_dates = [
        (start + timedelta(days=random.randint(0, delta.days))).date()
        for _ in range(n)
    ]
    return random_dates
order_date = generate_random_dates("2025-01-01", "2025-02-01", 100)
print(order_date[: 10])

df = pd.DataFrame({
    "order_id": order_id,
    "customer": customer,
    "product": product,
    "quantity": quantity,
    "price": price,
    "order_date": order_date
})
print(df.head())

df.to_csv("orders.csv", index = False, header = True, mode = "w")