
# 📦 PureShopper
**Smart Sales & Inventory Management System**

PureShopper is a powerful all-in-one e-commerce solution designed for small to medium-sized businesses. It seamlessly integrates real-time inventory tracking with streamlined sales management, helping you optimize stock levels, automate reordering, and uncover insights that drive efficiency and growth. Whether managing storefronts, warehouses, or online channels, PureShopper empowers your business to operate smarter and scale faster.

---

### 🔹 **Core E-commerce Features**

- **Real-Time Inventory Tracking**  
  **Monitor stock levels** across multiple warehouses and online sales channels with live updates.

- **Integrated Sales Management**  
  **Manage online orders, POS transactions, and marketplace sales from a single dashboard.**

- **Automated Reordering**  
  **Set stock thresholds to trigger restock alerts or automatic supplier orders.**

- **Multi-Location Support**  
  **Track inventory and sales across online stores, retail locations, and marketplaces like Amazon, eBay, and Etsy.**

- **Product Catalog Management**  
  **Create and organize product listings with categories, variants, images, pricing, SKUs, and SEO-friendly descriptions.**

- **Supplier & Purchase Order Management**  
  **Manage vendor relationships, automate purchase orders, and track inbound inventory shipments.**


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
git clone https://github.com/edwin-niwaha/pure_shopper
cd pure_shopper
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

For questions or demo requests, contact us at **support@pure_shopper.io**
