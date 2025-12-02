# Greatkart E-Commerce Project — Complete Synopsis

## 📋 Project Overview

**Greatkart** is a full-featured Django-based e-commerce web application designed to demonstrate a complete online shopping platform. It allows users to browse products, manage shopping carts, place orders, and provides administrators with tools to manage inventory, categories, and user accounts.

**Repository:** https://github.com/Cvayay/Greatkart-Ecommerce  
**Author:** Shivaji Sahani  
**Technology Stack:** Django 3.2, Python 3.12, SQLite3  
**Status:** Development/Demo

---

## 🎯 Project Goals

1. Build a functional e-commerce platform from scratch.
2. Implement core shopping features: product catalog, cart, checkout, and orders.
3. Provide admin panel for product and order management.
4. Demonstrate Django best practices (models, views, forms, templates).
5. Enable user registration, authentication, and profile management.

---

## 🏗️ Architecture & Core Components

### **1. Project Structure**

```
greatkart-django/
├── greatkart/              # Main project settings
│   ├── settings.py         # Django configuration
│   ├── urls.py             # Root URL routing
│   ├── views.py            # Home page view
│   ├── wsgi.py             # WSGI app entry
│   └── static/             # Global static files
├── accounts/               # User authentication & profiles
├── store/                  # Products catalog
├── carts/                  # Shopping cart management
├── orders/                 # Orders & payments
├── category/               # Product categories
├── templates/              # HTML templates
├── media/                  # User uploads (product images)
├── static/                 # CSS, JS, images
├── manage.py               # Django CLI
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not committed)
```

### **2. Django Apps**

#### **Accounts App**
- **Purpose:** User registration, authentication, profile management
- **Models:**
  - `Account` — Custom user model with extended fields
  - `UserProfile` — User profile (address, phone, avatar)
- **Features:**
  - User signup/login
  - Email verification
  - Password reset
  - User dashboard
  - Edit profile & change password

#### **Store App**
- **Purpose:** Product catalog and review management
- **Models:**
  - `Product` — Product details (name, price, description, image)
  - `Variation` — Product variants (size, color)
  - `ReviewRating` — User reviews and ratings
  - `ProductGallery` — Multiple product images
- **Features:**
  - Product filtering by category
  - Product detail view
  - User reviews & ratings
  - Product search

#### **Carts App**
- **Purpose:** Shopping cart management
- **Models:**
  - `Cart` — Shopping cart per user
  - `CartItem` — Individual items in cart
- **Features:**
  - Add/remove products from cart
  - Update quantities
  - Cart summary display
  - Cart context processor (available in all templates)

#### **Orders App**
- **Purpose:** Order management and payment
- **Models:**
  - `Order` — Order details (date, status, total)
  - `OrderProduct` — Products in an order
  - `Payment` — Payment information
- **Features:**
  - Place orders from cart
  - Order history & tracking
  - Payment processing (Razorpay/PayPal integration)
  - Order status updates

#### **Category App**
- **Purpose:** Product categorization
- **Models:**
  - `Category` — Product categories
- **Features:**
  - Category list/detail views
  - Context processor for navbar menu

---

## 💾 Database Design (SQLite3)

### **Key Models & Relationships**

```
Account (Custom User)
  ├── id (BigAutoField)
  ├── username, email, password
  ├── first_name, last_name
  ├── phone_number, is_active, created_date
  └── [One-to-One] UserProfile

UserProfile
  ├── user (FK → Account)
  ├── profile_picture, address, country, state, city
  └── zip_code

Category
  ├── id, category_name, slug
  ├── description, cat_image
  └── created_date

Product
  ├── id, product_name, slug, price
  ├── description, images
  ├── stock, category (FK → Category)
  ├── is_available, created_date
  └── [One-to-Many] Variation, ReviewRating, ProductGallery

Variation
  ├── product (FK → Product)
  ├── variation_category, variation_value
  └── is_active

ReviewRating
  ├── product (FK → Product), user (FK → Account)
  ├── subject, review, rating, status
  └── created_date

Cart
  ├── cart_id, date_added
  └── [One-to-Many] CartItem

CartItem
  ├── cart (FK → Cart), product (FK → Product)
  ├── quantity, is_active
  └── created_date

Order
  ├── order_number, user (FK → Account)
  ├── first_name, email, phone
  ├── address, city, state, country, zip
  ├── order_total, tax, status, created_date
  └── [One-to-Many] OrderProduct

OrderProduct
  ├── order (FK → Order)
  ├── product_name, product_id, price
  ├── quantity, created_date

Payment
  ├── order (FK → Order)
  ├── payment_id, payment_method, amount_paid
  ├── status, created_date
```

---

## 🔧 Technology Stack

### **Backend**
- **Framework:** Django 3.2.25
- **Language:** Python 3.12
- **Database:** SQLite3 (development)
- **ORM:** Django ORM

### **Frontend**
- **Template Engine:** Django Templates (HTML + Jinja2 syntax)
- **CSS Framework:** Bootstrap 5
- **JavaScript:** jQuery, custom scripts
- **Icons:** Font Awesome
- **Images:** Pillow (image processing)

### **Key Dependencies**
| Package | Version | Purpose |
|---------|---------|---------|
| asgiref | 3.9.1 | ASGI utilities |
| Django | 3.2.25 | Web framework |
| python-decouple | 3.8 | Environment variables |
| pytz | 2025.2 | Timezone handling |
| sqlparse | 0.5.3 | SQL parsing |
| requests | 2.32.5 | HTTP requests |
| Pillow | 12.0.0 | Image processing |

---

## 🚀 Setup & Installation

### **Prerequisites**
- Python 3.12+
- pip (package manager)
- Git

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/Cvayay/Greatkart-Ecommerce.git
cd Greatkart-Ecommerce
```

### **Step 2: Create Virtual Environment**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### **Step 3: Install Dependencies**
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### **Step 4: Configure Environment**
Create a `.env` file in the project root:
```
SECRET_KEY=your-django-secret-key-here
DEBUG=True
```

### **Step 5: Database Setup**
```powershell
python manage.py migrate
python manage.py createsuperuser
```

### **Step 6: Collect Static Files**
```powershell
python manage.py collectstatic --noinput
```

### **Step 7: Run Development Server**
```powershell
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 📱 User-Facing Features

### **Customers**
1. **Browse Products**
   - View all products or filter by category
   - See product details, images, variations
   - Read reviews and ratings

2. **Shopping Cart**
   - Add/remove products
   - Adjust quantities
   - View cart total

3. **Checkout & Orders**
   - Enter shipping address
   - Choose payment method
   - Place and track orders
   - View order history

4. **User Account**
   - Register and login
   - Manage profile (address, avatar)
   - Change password
   - View order history with details
   - Leave reviews and ratings

### **Admin/Staff**
1. **Product Management**
   - Add/edit/delete products
   - Manage variations and galleries
   - Set pricing and stock

2. **Category Management**
   - Create and manage categories
   - Assign products to categories

3. **Order Management**
   - View all orders
   - Update order status
   - Track payments

4. **User Management**
   - View registered users
   - Manage user accounts

---

## 🔑 Key Features Implemented

✅ **User Authentication & Authorization**
- Custom user model
- Email verification (optional)
- Password reset via email
- Profile management

✅ **Product Catalog**
- Multiple product images
- Product variations (size, color, etc.)
- Product filtering & search
- Stock management

✅ **Shopping Cart**
- Persistent cart per user
- Add/remove/update items
- Real-time cart counter

✅ **Orders & Checkout**
- Multi-step checkout
- Shipping address collection
- Order confirmation emails
- Order history & tracking

✅ **Reviews & Ratings**
- User product reviews
- 5-star rating system
- Review moderation (admin approval)

✅ **Admin Panel**
- Django admin interface
- Product/order management
- Category management
- User account administration

---

## 🔐 Security Features

- Secret key stored in `.env` (not committed)
- CSRF protection enabled
- Password hashing (Django default)
- SQL injection prevention (Django ORM)
- User authentication required for cart/orders
- Admin-only access to sensitive operations

---

## 📊 Database Migrations

The project includes 5+ migration files per app to evolve the schema:
- Initial models creation
- Field additions (UserProfile, ReviewRating, etc.)
- Updates to existing models

**Run migrations:**
```powershell
python manage.py migrate
```

---

## 🎨 Frontend Pages (Templates)

| Page | Template | Purpose |
|------|----------|---------|
| Home | `home.html` | Landing page with popular products |
| Products List | `store/store.html` | All products with filtering |
| Product Detail | `store/product_detail.html` | Single product view |
| Cart | `store/cart.html` | Shopping cart view |
| Checkout | `store/checkout.html` | Order placement |
| Order Confirmation | `orders/order_complete.html` | Post-order summary |
| User Dashboard | `accounts/dashboard.html` | User home |
| Login | `accounts/login.html` | User login |
| Register | `accounts/register.html` | New account signup |
| Profile | `accounts/edit_profile.html` | Edit user profile |
| Order History | `accounts/my_orders.html` | User's past orders |
| Order Detail | `accounts/order_detail.html` | Single order view |

---

## 🛠️ Development & Testing

### **Run Tests** (if available)
```powershell
python manage.py test
```

### **Code Quality Checks**
```powershell
python manage.py check
```

### **Create Superuser**
```powershell
python manage.py createsuperuser
```

### **Access Admin Panel**
Navigate to: http://127.0.0.1:8000/admin/

---

## 🚧 Known Issues & Improvements

1. **Admin Thumbnails**
   - Currently uses a local stub (`admin_thumbnails.py`)
   - Future: Implement proper image preview in admin

2. **Payment Integration**
   - Razorpay/PayPal integration prepared but requires API keys
   - Future: Full payment gateway integration

3. **Email Notifications**
   - Configured in settings but requires SMTP setup
   - Current: Gmail credentials in settings (should use `.env`)

4. **Scalability**
   - SQLite3 suitable for development only
   - Production: Switch to PostgreSQL or MySQL

---

## 📝 Deployment Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Use production-grade database (PostgreSQL)
- [ ] Configure allowed hosts: `ALLOWED_HOSTS = ['yourdomain.com']`
- [ ] Use environment variables for all secrets
- [ ] Set up HTTPS/SSL certificate
- [ ] Configure email backend for notifications
- [ ] Run `python manage.py collectstatic`
- [ ] Set up Gunicorn/uWSGI web server
- [ ] Use Nginx/Apache as reverse proxy
- [ ] Configure database backups

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -m "Add feature"`
4. Push to branch: `git push origin feature/my-feature`
5. Open a Pull Request

See `CONTRIBUTING.md` for details.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

## 👤 Author

**Shivaji Sahani**  
Email: shivajisahani01@gmail.com  
GitHub: [@Cvayay](https://github.com/Cvayay)

---

## 📞 Support & Questions

For questions or issues:
- Open an issue on GitHub
- Check the README for setup instructions
- Refer to Django documentation: https://docs.djangoproject.com/

---

## 🎓 Learning Resources

This project demonstrates:
- Django MVT architecture
- Database design & ORM
- User authentication & authorization
- Form handling & validation
- Template rendering & context processors
- Static files & media management
- Admin customization
- URL routing & view functions
- Model relationships (FK, M2M, 1-to-1)

---

**Last Updated:** December 1, 2025  
**Version:** 1.0.0
