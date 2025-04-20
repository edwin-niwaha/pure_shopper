
# 📦 StockTrack
**Smart Sales & Inventory Management System**

StockTrack is a powerful system for small to medium-sized businesses, combining real-time inventory tracking with seamless sales management. Optimize stock levels, automate reordering, and gain insights to boost efficiency and growth—across storefronts, warehouses, or online channels.


---

## 🚀 Features

### 🔹 **Core Features**

- **Real-Time Inventory Tracking**  
  **Monitor stock levels** across multiple locations with live updates.

- **Sales Management**  
  **Record and manage sales transactions** with integrated POS or online order syncing.

- **Automated Reordering**  
  **Set stock thresholds** to trigger automatic restock alerts or orders.

- **Multi-Location Support**  
  **Track inventory and sales** across stores, warehouses, and sales channels.

- **Product Catalog Management**  
  **Organize products** by categories, variants, pricing, and SKUs.

- **Supplier & Purchase Order Management**  
  **Manage vendors**, create purchase orders, and track inbound stock.

---

### 📊 **Analytics & Insights**

- **Sales & Inventory Reports**  
  **Gain insights** into best-selling products, stock turnover, and profit margins.

- **Demand Forecasting**  
  **Predict stock needs** based on sales trends and seasonality.

- **Inventory Valuation**  
  **Track inventory value** using FIFO, LIFO, or average cost methods.

---

### 🔐 **Additional Features**

- **User Roles & Permissions**  
  **Control access levels** for different team members.

- **Low Stock Alerts**  
  **Get notified** before you run out of critical items.

- **Barcode Scanning**  
  **Speed up operations** with barcode integration for inventory and sales.

---

## 📋 Requirements

- **Operating System:**  
  - Linux, macOS, or Windows
- **Programming Language:**  
  - Python 3.8 or higher
- **Database:**  
  - PostgreSQL (recommended) or MySQL
- **Web Framework:**  
  - Django 3.2 or higher
- **Additional Tools:**
  - Node.js (for front-end build tools)
  - Redis (optional for caching)
- **Libraries/Dependencies:**  
  - `Django REST framework`
  - `django-cors-headers`
  - `psycopg2` (for PostgreSQL)
  - `celery` (for background tasks)
  - `Pillow` (for image handling)
  - `django-environ` (for environment variables)
  - `django-debug-toolbar` (for debugging)

---

## 📈 Benefits

- Reduce stockouts and overstocks
- Streamline sales and inventory operations
- Make data-driven business decisions
- Scale effortlessly across locations

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/edwin-niwaha/stock-track
cd stock-track
```

### 2. Set Up Python Environment
Create a virtual environment:
```bash
python -m venv .venv

```
### Activate the virtual environment:

- Windows:
```bash
source .venv/Scripts/activate
  # Powershell
    deactivate
    .venv\Scripts\Activate
```


### 3. Install Required Python Packages
```bash
pip install -r requirements.txt
pip freeze > requirements.txt
```

### 4. Set Up Database
- Create a new database in PostgreSQL/MySQL.
- Update your database settings in settings.py.

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 7. Seed Initial Data (if applicable)
```bash
python manage.py loaddata <fixture-file>
```

### 9. Run the Django Development Server
```bash
python manage.py runserver
```
### 10. Access the Application
-Open your browser and go to:
http://127.0.0.1:8000

---

## 🧪 Contributing

Want to contribute? Fork the repo and submit a pull request!

---

## 📄 License

MIT License

---

## 📬 Contact

For questions or demo requests, contact us at **support@stocktrack.io**
