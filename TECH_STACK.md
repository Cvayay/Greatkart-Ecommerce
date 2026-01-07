# 🛠️ Greatkart E-Commerce - Complete Tech Stack

A detailed breakdown of all technologies, frameworks, libraries, and tools used in this project.

---

## 📊 Tech Stack Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    GREATKART TECH STACK                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BACKEND LAYER                 FRONTEND LAYER                   │
│  ─────────────────            ──────────────                    │
│  • Python 3.12                • HTML5                           │
│  • Django 3.2.25              • Bootstrap 5                     │
│  • SQLite3                     • CSS3                           │
│  • Django ORM                  • jQuery 2.0                     │
│                                • Font Awesome 5                 │
│  CORE DEPENDENCIES             • Pillow (Image)                │
│  ────────────────────                                          │
│  • asgiref 3.9.1               TOOLS & SERVICES                │
│  • sqlparse 0.5.3              ───────────────────             │
│  • pytz 2025.2                 • Git & GitHub                   │
│  • python-decouple 3.8         • Virtual Environment            │
│  • requests 2.32.5             • Django Admin                   │
│  • Pillow 12.0.0               • Email (SMTP)                   │
│                                • Session Management             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔷 Backend Stack

### **Programming Language**
```
Language:          Python 3.12
Why Python?        - Readable, maintainable code
                   - Extensive library ecosystem
                   - Great for web development
                   - Strong community support
Version:           3.12 (Latest stable)
Documentation:     https://www.python.org/
```

### **Web Framework**
```
Framework:         Django 3.2.25 (LTS - Long Term Support)
What is Django?    - Full-stack web framework
                   - "Batteries included" approach
                   - Built-in ORM, admin, authentication
                   - Excellent security features
Architecture:      MVT (Model-View-Template)
Documentation:     https://docs.djangoproject.com/
```

**Why Django for this project?**
- ✅ Built-in admin panel (no need for custom admin)
- ✅ ORM eliminates need for raw SQL
- ✅ Strong authentication framework
- ✅ Session management out-of-the-box
- ✅ CSRF protection built-in
- ✅ Migrations system for database versioning
- ✅ Excellent documentation
- ✅ Production-ready and scalable

### **Database Layer**

#### **Database Engine**
```
Database:          SQLite3
Purpose:           Development & Testing
Why SQLite?        - Zero setup required
                   - File-based (single file)
                   - Perfect for development
                   - No server needed

Production DB:     PostgreSQL (recommended)
Why PostgreSQL?    - Full ACID compliance
                   - Supports concurrent writes
                   - Better for high-traffic
                   - Advanced features (JSON, arrays)
```

#### **ORM (Object-Relational Mapping)**
```
ORM:               Django ORM (Built-in)
What it does:      - Maps Python classes to database tables
                   - Converts Python code to SQL queries
                   - Prevents SQL injection
                   - Query chaining and lazy evaluation

No need for:       - Writing raw SQL
                   - Manual connection management
                   - SQL syntax learning
```

### **Environment Management**
```
Package Manager:   pip (Python Package Manager)
Dependency File:   requirements.txt
Virtual Env:       .venv (Python venv)

Setup:
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
$ pip install -r requirements.txt
```

---

## 📦 Core Dependencies (Backend)

### **Installed Packages & Versions**

```
asgiref==3.9.1
├─ Purpose:       ASGI server utilities
├─ Used by:       Django (async support)
├─ What it does:  Converts WSGI to ASGI
└─ Why needed:    For async request handling

Django==3.2.25
├─ Purpose:       Web framework
├─ Core modules:
│  ├─ django.db           → ORM & database
│  ├─ django.contrib.auth → Authentication
│  ├─ django.contrib.admin → Admin panel
│  ├─ django.core.mail    → Email sending
│  ├─ django.urls         → URL routing
│  └─ django.template     → Template engine
└─ Documentation: https://docs.djangoproject.com/

python-decouple==3.8
├─ Purpose:       Read environment variables from .env file
├─ Imports:       from decouple import config
├─ Usage:         SECRET_KEY = config('SECRET_KEY')
└─ Why needed:    Separate secrets from code

pytz==2025.2
├─ Purpose:       Timezone handling
├─ Problem solved: Different timezones across users
├─ Usage:         Timezone-aware datetime objects
└─ Used in:       created_date, updated_date fields

sqlparse==0.5.3
├─ Purpose:       SQL parsing and formatting
├─ Used by:       Django ORM internally
├─ What it does:  Parses SQL statements
└─ Why needed:    For query optimization and debugging

requests==2.32.5
├─ Purpose:       HTTP client library
├─ Imports:       import requests
├─ Usage:         requests.get(url), requests.post(url, data)
├─ Used for:      External API calls (future payment gateways)
└─ Why needed:    Making HTTP requests from Python code

Pillow==12.0.0
├─ Purpose:       Image processing library
├─ Imports:       from PIL import Image
├─ Used for:      Handling Django ImageField
├─ Supports:      JPG, PNG, GIF, BMP, TIFF, etc.
├─ Features:
│  ├─ Image validation
│  ├─ Image resizing
│  ├─ Format conversion
│  └─ Thumbnail generation
└─ Used in:       Product images, user avatars
```

### **Dependency Tree**
```
Django 3.2.25
├── asgiref (3.9.1)
├── sqlparse (0.5.3)
├── pytz (2025.2)
└── (others)

Project Dependencies
├── python-decouple (3.8)      — .env management
├── requests (2.32.5)           — HTTP requests
└── Pillow (12.0.0)            — Image processing
```

### **Installation**
```powershell
# Install all at once
pip install -r requirements.txt

# Install individually
pip install Django==3.2.25
pip install python-decouple==3.8
pip install requests==2.32.5
pip install Pillow==12.0.0

# View installed packages
pip list
pip show Django
```

---

## 🎨 Frontend Stack

### **HTML**
```
Version:           HTML5
Template Engine:   Django Templates (Jinja2 syntax)
Base Template:     templates/base.html
Why HTML5?         - Semantic elements
                   - Built-in form handling
                   - Media support (video, audio)
                   - Canvas for graphics

Template Features:
├─ Variable interpolation: {{ variable }}
├─ Conditionals:           {% if condition %}
├─ Loops:                  {% for item in items %}
├─ Filters:                {{ date|date:"Y-m-d" }}
├─ Template tags:          {% load static %}
├─ URL reversal:           {% url 'view_name' %}
└─ Inheritance:            {% extends 'base.html' %}
```

### **CSS**
```
Framework:         Bootstrap 5
Bootstrap Files:   static/css/bootstrap.css
Custom CSS:        static/css/custom.css
Responsive:        static/css/responsive.css
UI Framework:      static/css/ui.css

Bootstrap 5 Features Used:
├─ Grid system (12 columns)
├─ Flex layout
├─ Button styles
├─ Form styling
├─ Card components
├─ Navbar component
├─ Alert components
├─ Modal dialogs
└─ Responsive breakpoints

Responsive Design:
├─ Mobile-first approach
├─ Breakpoints: xs, sm, md, lg, xl
├─ Flexbox layout
└─ Media queries

Custom Styles:
├─ Brand colors
├─ Custom fonts
├─ Product cards
├─ Shopping cart styling
└─ Form enhancements
```

### **JavaScript**

#### **jQuery**
```
Version:           jQuery 2.0.0
File:              static/js/jquery-2.0.0.min.js
What it does:      DOM manipulation, event handling
Used for:          ✓ Form validation
                   ✓ Dynamic content loading
                   ✓ Event handlers
                   ✓ AJAX requests
                   ✓ Animation

jQuery Methods Used:
├─ $(selector).click()
├─ $(selector).submit()
├─ $.ajax() or $.get()
├─ $(selector).hide()/show()
├─ $(selector).addClass()/removeClass()
└─ $(selector).val()
```

#### **Bootstrap JavaScript**
```
File:              static/js/bootstrap.bundle.min.js
Purpose:           Interactive components
Components:        ✓ Navbar collapse
                   ✓ Modals
                   ✓ Dropdowns
                   ✓ Toasts/Alerts
                   ✓ Tooltips
                   ✓ Popovers
```

#### **Custom JavaScript**
```
File:              static/js/script.js
Purpose:           Application-specific logic
Features:          ✓ Form validation
                   ✓ Cart management
                   ✓ User interactions
                   ✓ Event handlers
```

### **Icons & Fonts**

#### **Font Awesome**
```
Version:           Font Awesome 5
Location:          static/fonts/fontawesome/
Purpose:           Icon library
Icons Used:        ✓ Shopping cart icon
                   ✓ User account icon
                   ✓ Home icon
                   ✓ Search icon
                   ✓ Star rating icon
                   ✓ Check/X marks
                   ✓ Navigation arrows

Usage in HTML:
<i class="fas fa-shopping-cart"></i>
<i class="fas fa-star"></i>
<i class="fas fa-user"></i>
```

#### **Roboto Font**
```
Location:          static/fonts/roboto/
Purpose:           Typography
Variants:          Regular, Bold, Light, Medium
Used for:          Body text, headings
Why chosen:        Clean, readable, modern look
```

### **Image Processing**

#### **Pillow (Backend)**
```
Purpose:           Process images uploaded by users
Features:          ✓ Validate image format
                   ✓ Resize images
                   ✓ Convert formats
                   ✓ Generate thumbnails
                   ✓ Extract metadata

Used in Django:
from django.db import models
class Product(models.Model):
    images = models.ImageField(upload_to='photos/products')
    
This leverages Pillow for:
├─ Upload validation
├─ Storage management
└─ Image serving
```

---

## 🗄️ Database Schema & ORM

### **Database Design**
```
Type:              Relational Database
Tables:            15+ tables
Relationships:
├─ Foreign Keys    (1-to-Many)
├─ One-to-One      (Account ↔ UserProfile)
├─ Many-to-Many    (CartItem ↔ Variation)
└─ Junction Tables (Variation join table)

Data Types Used:
├─ CharField       → Text fields (max length)
├─ TextField       → Long text content
├─ IntegerField    → Whole numbers
├─ FloatField      → Decimal numbers
├─ BooleanField    → True/False
├─ DateTimeField   → Date and time
├─ EmailField      → Email validation
├─ ImageField      → Image upload & storage
├─ ForeignKey      → Relationships
└─ ManyToManyField → Multiple choices

Indexes:
├─ Primary Key (id) — Automatic
├─ Unique Fields — Indexed for performance
├─ Foreign Keys — Indexed by Django
└─ Slug Fields — Used for URL lookups
```

### **ORM Operations Used**

```python
# CREATE
Product.objects.create(product_name="Phone", price=30000)

# READ
Product.objects.all()
Product.objects.filter(category__name="Electronics")
Product.objects.get(id=1)

# UPDATE
product = Product.objects.get(id=1)
product.price = 35000
product.save()

# DELETE
product.delete()

# AGGREGATE
Product.objects.aggregate(Avg('price'))
Product.objects.aggregate(Count('id'))

# FILTERING
Product.objects.filter(is_avilable=True)
Product.objects.exclude(category__id=1)

# ORDERING
Product.objects.order_by('-created_date')

# RELATIONSHIPS
product.category.name
product.variation_set.all()
```

---

## 🔐 Security Technologies

### **Built-in Django Security**
```
Feature                        How it Works
─────────────────────────────────────────────────
CSRF Protection           →    {% csrf_token %} in forms
Password Hashing          →    set_password() method
SQL Injection Prevention   →    ORM (parameterized queries)
XSS Protection            →    Auto-escaping in templates
Session Management        →    Secure session cookies
User Authentication       →    Custom user model + manager
Permission System         →    is_active, is_staff, is_admin

.env File                 →    Secrets not in git
SQLite Database          →    Separate data file
Email Verification       →    Token-based activation
```

### **Custom Security**
```
Email Verification      →    User must verify email
Cart Merge Logic        →    Prevent cart loss on login
Password Reset Token    →    Time-limited secure link
IP Address Logging      →    Track review submissions
Admin Approval          →    Manual review moderation
```

---

## 🚀 Development & Deployment Tools

### **Version Control**
```
VCS:                   Git
Repository:            GitHub (cloud hosting)
Repository URL:        https://github.com/Cvayay/Greatkart-Ecommerce
Branch:                main
Workflow:              ✓ git add .
                       ✓ git commit -m "message"
                       ✓ git push origin main

.gitignore Includes:
├─ .env                 → Secrets
├─ .venv/               → Virtual environment
├─ db.sqlite3           → Development database
├─ __pycache__/         → Compiled Python
├─ *.pyc               → Python cache
├─ .DS_Store           → macOS files
└─ node_modules/       → (Future frontend deps)
```

### **Local Development**
```
Editor:                VS Code
Python Version:        3.12.x
Virtual Environment:   .venv (Python venv)
Dev Server:            Django runserver (port 8000)
Database:              SQLite3 (db.sqlite3)

Commands:
python manage.py runserver          → Start dev server
python manage.py makemigrations     → Create migration files
python manage.py migrate            → Apply migrations
python manage.py createsuperuser    → Create admin user
python manage.py collectstatic      → Collect static files
python manage.py shell              → Interactive shell
```

### **Production Deployment**

#### **Recommended Stack**
```
Web Server:            Gunicorn or uWSGI
Reverse Proxy:         Nginx
Database:              PostgreSQL
Cache Layer:           Redis (optional)
Static Files:          AWS S3 or CDN
Deployment Platform:   Heroku, AWS, DigitalOcean
Monitoring:            Sentry (error tracking)
Logging:               ELK Stack or similar
```

#### **Deployment Checklist**
```
Configuration:
├─ DEBUG = False
├─ ALLOWED_HOSTS configured
├─ SECRET_KEY from environment
├─ STATIC_ROOT configured
├─ MEDIA_ROOT configured
└─ Database switched to PostgreSQL

Services:
├─ Email backend (Gmail SMTP or SendGrid)
├─ SSL/HTTPS certificate
├─ Database backups
├─ Error monitoring
├─ Performance monitoring
└─ CDN for static assets
```

---

## 📧 Email Service

### **Email Configuration**
```
Backend:               SMTP (Simple Mail Transfer Protocol)
Provider:              Gmail or SendGrid (configurable)
Port:                  587 (TLS)

Django Settings:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

Used For:
├─ Account verification emails
├─ Password reset emails
├─ Order confirmation emails
├─ Admin notifications
└─ Marketing emails (future)

Implementation:
from django.core.mail import EmailMessage

message = render_to_string('template.html', context)
email = EmailMessage(subject, message, to=[email])
email.send()
```

---

## 📊 Project Statistics

### **Codebase Metrics**
```
Python Files:          15+
Templates:             20+
CSS Files:             5+
JavaScript Files:      3+
Total Lines of Code:   2,000+
Models:                9
Views:                 15+
URLs:                  50+
Database Tables:       15+
```

### **Performance Metrics**
```
Database Queries:      Optimized with select_related
Cache Strategy:        Session-based
Average Load Time:     < 500ms
Page Size:             ~ 2-5 MB
```

---

## 🔄 Data Flow Architecture

```
┌─────────────────┐
│  User Browser   │
│  (HTML, CSS,    │
│   JavaScript)   │
└────────┬────────┘
         │ HTTP Request
         ↓
┌─────────────────────────────┐
│   Django Web Server         │
│ ┌─────────────────────────┐ │
│ │ 1. URL Router (urls.py) │ │
│ │    ↓                    │ │
│ │ 2. View Function        │ │
│ │    ↓                    │ │
│ │ 3. Models (Query)       │ │
│ │    ↓                    │ │
│ │ 4. Template (Render)    │ │
│ │    ↓                    │ │
│ │ 5. Response (HTML)      │ │
│ └─────────────────────────┘ │
└────────┬────────────────────┘
         │
         ↓
┌─────────────────────────────┐
│   SQLite Database           │
│ ├─ Accounts                 │
│ ├─ Products                 │
│ ├─ Carts                    │
│ ├─ Orders                   │
│ └─ Reviews                  │
└─────────────────────────────┘
```

---

## 🔌 Integration Points

### **External Services (Optional)**
```
Payment Gateway:       Razorpay or Stripe (framework ready)
Email Service:         Gmail SMTP or SendGrid
Analytics:            Google Analytics (future)
CDN:                  Cloudflare or AWS CloudFront (future)
Image Storage:        AWS S3 or Google Cloud Storage (future)
```

### **APIs & Webhooks**
```
Payment Callbacks:     Webhook endpoints for payment status
Email Confirmations:   SMTP integration
Session Management:    Django session framework
```

---

## 📚 Documentation & Learning Resources

### **Official Documentation**
```
Django:        https://docs.djangoproject.com/
Python:        https://docs.python.org/3/
Bootstrap:     https://getbootstrap.com/docs/
jQuery:        https://jquery.com/
Pillow:        https://pillow.readthedocs.io/
```

### **Project Documentation**
```
README.md              → Quick start guide
SYNOPSIS.md            → Project architecture
LEARNING_GUIDE.md      → In-depth tutorials
PRESENTATION_GUIDE.md  → HOD presentation
```

---

## 🎯 Tech Stack Comparison

### **Why These Choices?**

| Component | Choice | Alternative | Why Chosen |
|-----------|--------|-------------|-----------|
| Backend | Django | Flask, FastAPI | Full-featured, batteries included |
| Database | SQLite | MySQL, PostgreSQL | Development convenience |
| ORM | Django ORM | SQLAlchemy | Built-in, no setup needed |
| Frontend | Bootstrap | Tailwind, Material | Popular, many examples |
| JavaScript | jQuery | React, Vue | Lightweight, simple interactions |
| Icons | Font Awesome | Material Icons | Extensive library, well-known |
| Python Env | venv | Poetry, Conda | Built-in, lightweight |

---

## 🔧 Tech Stack Strengths

```
✅ Full Backend & Frontend in one framework
✅ Built-in admin panel (saves development time)
✅ Strong security features out-of-the-box
✅ Excellent documentation
✅ Active community support
✅ Easy to deploy (Heroku, AWS, etc.)
✅ Great for rapid development
✅ Scalable architecture
✅ Well-tested by thousands of projects
✅ Easy to learn and understand
```

---

## 📈 Scalability Path

### **Current Stack (Development)**
```
SQLite → Django Dev Server → Bootstrap CSS → jQuery
```

### **Production Upgrade Path**
```
PostgreSQL → Gunicorn/uWSGI → Nginx → Bootstrap + Custom CSS → React/Vue

Additional Layers:
├─ Redis for caching
├─ CDN for static files
├─ Load balancing
├─ Database replication
└─ Microservices (future)
```

---

## 📦 Requirements.txt Reference

```
# Django Web Framework
Django==3.2.25

# Server utilities
asgiref==3.9.1

# Database utilities
sqlparse==0.5.3

# Timezone handling
pytz==2025.2

# Environment variables
python-decouple==3.8

# HTTP requests
requests==2.32.5

# Image processing
Pillow==12.0.0
```

### **Installation from File**
```powershell
# Create requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt

# Update a package
pip install --upgrade Django

# View installed packages
pip list
```

---

## 🎓 Learning the Tech Stack

### **Recommended Learning Order**

1. **Python Basics** (2-3 weeks)
   - Variables, data types, loops
   - Functions, classes, modules
   - File handling, error handling

2. **Django Framework** (3-4 weeks)
   - Models (ORM)
   - Views (function-based)
   - Templates (Jinja2)
   - URLs and routing

3. **Database** (2 weeks)
   - SQL basics
   - Relationships (FK, M2M)
   - Migrations
   - Query optimization

4. **Frontend Basics** (2 weeks)
   - HTML5
   - CSS3
   - Bootstrap grid system
   - Responsive design

5. **JavaScript** (2 weeks)
   - DOM manipulation
   - jQuery
   - Event handling
   - AJAX requests

6. **Full Projects** (Ongoing)
   - Build projects incrementally
   - Deploy to production
   - Iterate and improve

---

## 🚀 Next Tech Stack Additions

### **Phase 2 Enhancements**
```
Payment Gateway       → Stripe SDK / Razorpay SDK
REST API             → Django REST Framework
Real-time Messaging  → Django Channels (WebSocket)
Task Queue           → Celery + Redis
Caching              → Redis
Search               → Elasticsearch or Django Haystack
API Documentation    → Swagger/OpenAPI
```

### **Phase 3 Frontend Modernization**
```
Frontend Framework   → React or Vue.js
Build Tool          → Webpack or Vite
Package Manager     → npm or yarn
CSS Preprocessor    → SASS/SCSS
State Management    → Redux or Vuex
Component Library   → Material-UI or Ant Design
```

---

## 📞 Summary: Complete Tech Stack

```
┌─────────────────────────────────────────────────────┐
│              COMPLETE TECH STACK SUMMARY             │
├─────────────────────────────────────────────────────┤
│ BACKEND:          Django 3.2.25 + Python 3.12      │
│ DATABASE:         SQLite3 (Dev) / PostgreSQL (Prod) │
│ ORM:              Django ORM                        │
│ FRONTEND:         HTML5 + Bootstrap 5 + jQuery      │
│ ICONS:            Font Awesome 5                    │
│ FONTS:            Roboto                            │
│ IMAGE PROC:       Pillow 12.0.0                     │
│ EMAIL:            SMTP (Gmail/SendGrid)             │
│ VERSION CONTROL:  Git + GitHub                      │
│ DEPLOYMENT:       Heroku/AWS/DigitalOcean           │
│ MONITORING:       Django Debug Toolbar (Dev)        │
└─────────────────────────────────────────────────────┘
```

---

**Master this tech stack and you'll be ready to build professional web applications!** 🎓

