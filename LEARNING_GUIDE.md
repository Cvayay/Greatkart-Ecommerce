# 📚 Greatkart E-Commerce - Complete Learning Guide

A comprehensive guide to understanding every aspect of this Django e-commerce project. Learn Django through real-world application development.

---

## 📖 Table of Contents

1. [Django Fundamentals](#django-fundamentals)
2. [Project Architecture](#project-architecture)
3. [Models (Database Layer)](#models-database-layer)
4. [Views (Business Logic)](#views-business-logic)
5. [Forms & Validation](#forms--validation)
6. [Templates (Frontend)](#templates-frontend)
7. [URLs & Routing](#urls--routing)
8. [Authentication System](#authentication-system)
9. [Shopping Cart Logic](#shopping-cart-logic)
10. [Order Management](#order-management)
11. [Static Files & Media](#static-files--media)
12. [Context Processors](#context-processors)
13. [Admin Customization](#admin-customization)
14. [Best Practices](#best-practices)
15. [Common Patterns](#common-patterns)
16. [Troubleshooting](#troubleshooting)

---

## 🎓 Django Fundamentals

### What is Django?

Django is a **batteries-included** Python web framework that follows the **MVT (Model-View-Template)** architecture:

- **Model** — Database layer (ORM)
- **View** — Business logic and request handling
- **Template** — HTML rendering with dynamic data

### Key Concepts

#### **1. Models (ORM)**
Models define your database structure without writing SQL:

```python
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
```

#### **2. Views**
Functions that handle HTTP requests and return responses:

```python
from django.shortcuts import render
from .models import Product

def store(request):
    products = Product.objects.all()
    return render(request, 'store.html', {'products': products})
```

#### **3. Templates**
HTML files with dynamic content using Jinja2 syntax:

```html
<h1>Products</h1>
{% for product in products %}
    <h2>{{ product.product_name }}</h2>
    <p>Price: ₹{{ product.price }}</p>
{% endfor %}
```

#### **4. URLs**
Map URLs to views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.store, name='store'),
]
```

---

## 🏗️ Project Architecture

### Django Project Structure

```
greatkart-django/
│
├── greatkart/              # Project configuration (settings, URLs, WSGI)
│   ├── settings.py         # Database, installed apps, middleware, etc.
│   ├── urls.py             # Root URL configuration
│   └── views.py            # Home page view
│
├── accounts/               # User authentication app
├── store/                  # Products catalog app
├── carts/                  # Shopping cart app
├── orders/                 # Orders & payments app
├── category/               # Categories app
│
├── templates/              # Global HTML templates
├── static/                 # CSS, JS, images
├── media/                  # User-uploaded files
│
├── manage.py               # Django CLI tool
└── requirements.txt        # Python dependencies
```

### MVT Flow in Greatkart

```
User Request
    ↓
URL Router (urls.py) — finds matching view
    ↓
View Function (views.py) — fetches data from models
    ↓
Model Query (models.py) — retrieves from database
    ↓
View renders Template (templates/) with context
    ↓
HTML Response sent to browser
```

---

## 💾 Models (Database Layer)

Models are Python classes that map to database tables. Understanding models is **crucial** for Django development.

### **1. Custom User Model (Account)**

This project uses a custom user model instead of Django's default `User`:

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    """Manager for creating regular and superusers"""
    
    def create_user(self, first_name, last_name, username, email, password=None):
        """Create a regular user"""
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):
        """Create admin user with all permissions"""
        user = self.create_user(email, username, password, first_name, last_name)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    """Custom user model extending Django's AbstractBaseUser"""
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    
    # Authentication fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)  # Email verification
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'  # Login with email instead of username
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        """Check if user has permission"""
        return self.is_admin
```

**Why custom user model?**
- Login with email instead of username
- Add phone number and extra fields
- Flexible future customization
- Better for production apps

### **2. UserProfile (One-to-One Relationship)**

Extends the Account model with address information:

```python
class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    profile_picture = models.ImageField(blank=True, upload_to='user_profile/')
    city = models.CharField(blank=True, max_length=20)
    state = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    
    def __str__(self):
        return self.user.first_name
    
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
```

**One-to-One Relationship:**
- Each Account has exactly one UserProfile
- Each UserProfile belongs to exactly one Account
- `on_delete=models.CASCADE` — delete profile when user is deleted

**Usage:**
```python
# Access profile from user
user.userprofile.address_line_1

# Access user from profile
profile.user.email
```

### **3. Category Model**

Product categories:

```python
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)  # URL-friendly name
    description = models.CharField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
        """Generate URL for this category"""
        return reverse('products_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name
```

**Key Concepts:**
- `slug` — URL-friendly identifier (e.g., "electronics" instead of "Electronics & Gadgets")
- `get_url()` — Generates URL dynamically using reverse()
- `reverse()` — Converts URL name to actual URL path

### **4. Product Model (Many-to-One with Category)**

```python
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_avilable = models.BooleanField(default=True)  # Note: typo in field name
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        """Generate product URL"""
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def averageReview(self):
        """Calculate average rating"""
        reviews = ReviewRating.objects.filter(
            product=self, status=True
        ).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def countReview(self):
        """Count total reviews"""
        reviews = ReviewRating.objects.filter(
            product=self, status=True
        ).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
    
    def __str__(self):
        return self.product_name
```

**Key Concepts:**
- `ForeignKey` — Many products belong to one category
- `aggregate()` — Perform database calculations (sum, avg, count)
- `auto_now_add` — Set timestamp only on creation
- `auto_now` — Update timestamp on every save

### **5. Variation Model (Product Variants)**

Handle different sizes, colors, etc.:

```python
variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)

class VariationManager(models.Manager):
    """Custom manager for filtering variations"""
    
    def colors(self):
        return super(VariationManager, self).filter(
            variation_category='color', is_active=True
        )
    
    def sizes(self):
        return super(VariationManager, self).filter(
            variation_category='size', is_active=True
        )

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice
    )
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    
    objects = VariationManager()
    
    def __str__(self):
        return self.variation_value
```

**Custom Manager:**
```python
# Usage in views
colors = Variation.objects.colors()  # Get all active colors
sizes = Variation.objects.sizes()    # Get all active sizes
```

### **6. ReviewRating Model**

User reviews with ratings:

```python
class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)  # Admin approval
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
```

**Many-to-Many Relationship (implicit):**
- Many users can review many products
- Uses ForeignKey to achieve Many-to-Many

### **7. Cart & CartItem Models**

Shopping cart system:

```python
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)  # Session-based
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)  # Size, color chosen
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
```

**Key Concept: Dual Cart System**
- **Authenticated users:** Use user-based cart (persisted)
- **Anonymous users:** Use session-based cart (temporary)

### **8. Order & OrderProduct Models**

Order management:

```python
class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product.product_name
```

**Key Concept: Snapshot**
- OrderProduct stores a **snapshot** of product data
- Prevents price changes from affecting past orders
- `product_price` is copied from Product.price at order time

### **9. Payment Model**

```python
class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.payment_id
```

---

## 🎯 Views (Business Logic)

Views are Python functions that handle HTTP requests and return responses. They're the **brain** of your application.

### **View Anatomy**

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product

def product_detail(request, product_id):
    # 1. Get request data
    product_id = request.GET.get('id', 1)
    
    # 2. Query database
    product = get_object_or_404(Product, id=product_id)
    
    # 3. Process data
    is_in_stock = product.stock > 0
    
    # 4. Create context (data for template)
    context = {
        'product': product,
        'is_in_stock': is_in_stock,
    }
    
    # 5. Render template with context
    return render(request, 'product_detail.html', context)
```

### **1. Home View (greatkart/views.py)**

```python
def home(request):
    products = Product.objects.all().filter(is_avilable=True).order_by('created_date')
    
    # Collect reviews per product
    reviews = {}
    for product in products:
        reviews[product.id] = ReviewRating.objects.filter(
            product_id=product.id, status=True
        )
    
    context = {
        'products': products,
        'reviews': reviews,  # dict: product_id -> QuerySet of reviews
    }
    
    return render(request, 'home.html', context=context)
```

**Key Concepts:**
- `filter()` — Get matching records
- `order_by()` — Sort results
- `context` — Pass data to template as dictionary

### **2. Store View (List Products)**

```python
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        # Filter by category
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_avilable=True)
        paginator = Paginator(products, 3)
    else:
        # Show all products
        products = Product.objects.all().filter(is_avilable=True).order_by('id')
        paginator = Paginator(products, 6)
    
    # Pagination
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()
    
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
```

**Key Concepts:**
- **Pagination** — Split large result sets into pages
- **QuerySet methods:**
  - `filter()` — WHERE clause
  - `count()` — COUNT(*)
  - `order_by()` — ORDER BY
  - `get_object_or_404()` — Get one object or return 404 error

### **3. Product Detail View**

```python
def product_detail(request, category_slug, product_slug):
    # Get the product
    single_product = Product.objects.get(
        category__slug=category_slug,  # Filter by category
        slug=product_slug
    )
    
    # Check if in cart
    in_cart = CartItem.objects.filter(
        cart__cart_id=_cart_id(request),
        product=single_product
    ).exists()
    
    # Check if user bought it (for reviews)
    if request.user.is_authenticated:
        orderproduct = OrderProduct.objects.filter(
            user=request.user,
            product_id=single_product.id
        ).exists()
    else:
        orderproduct = None
    
    # Get reviews
    reviews = ReviewRating.objects.filter(
        product_id=single_product.id,
        status=True
    )
    
    # Get product gallery
    product_gallery = ProductGallery.objects.filter(
        product_id=single_product.id
    )
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery': product_gallery,
    }
    return render(request, 'store/product_detail.html', context)
```

**Key Concepts:**
- **Double underscore (`__`)** — Follow relationships (ForeignKey)
  - `category__slug` — Access Category.slug through Product.category
- **exists()** — Check if record exists without fetching
- **Request object** — Contains info about the request

### **4. Search View**

```python
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # Search by product name or description
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) |  # OR
                Q(product_name__icontains=keyword)
            )
            product_count = products.count()
    
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
```

**Key Concepts:**
- **Q objects** — Complex queries with AND/OR logic
  - `Q(field1__icontains=value) | Q(field2__icontains=value)` — OR
  - `Q(...) & Q(...)` — AND
- **icontains** — Case-insensitive search

### **5. Review Submission**

```python
def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')  # Get previous page
    
    if request.method == 'POST':
        try:
            # Check if user already reviewed
            reviews = ReviewRating.objects.get(
                user__id=request.user.id,
                product__id=product_id
            )
            # Update existing review
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Your review has been updated!')
            return redirect(url)
        
        except ReviewRating.DoesNotExist:
            # Create new review
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')  # IP address
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Your review has been submitted.')
                return redirect(url)
```

**Key Concepts:**
- **request.META** — Server/client information
  - `HTTP_REFERER` — Previous page URL
  - `REMOTE_ADDR` — Client IP address
- **messages framework** — Flash messages to show user feedback
- **Model instantiation** vs **form.save()** — Different patterns

---

## 🛒 Shopping Cart Logic

The cart system is **sophisticated** and handles both authenticated and anonymous users:

### **Cart ID Function**

```python
def _cart_id(request):
    """Get or create a cart ID based on session"""
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()  # Create session if doesn't exist
    return cart
```

**How it works:**
1. Django stores session ID in browser cookie
2. Each session is unique to a user
3. Temporary carts are linked to session

### **Add to Cart (Authenticated User)**

```python
def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)
    
    if current_user.is_authenticated:
        product_variation = []
        
        # Get selected variations from form (size, color)
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(
                        product=product,
                        variation_category__iexact=key,
                        variation_value__iexact=value
                    )
                    product_variation.append(variation)
                except:
                    pass
        
        # Check if product already in cart
        is_cart_item_exists = CartItem.objects.filter(
            product=product, user=current_user
        ).exists()
        
        if is_cart_item_exists:
            # Get existing cart items
            cart_item = CartItem.objects.filter(product=product, user=current_user)
            ex_var_list = []
            id = []
            
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            
            # Check if exact same variations exist
            if product_variation in ex_var_list:
                # Increase quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                # Create new cart item with different variations
                item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    user=current_user
                )
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            # Create new cart item
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                user=current_user,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        
        return redirect('cart')
```

**Key Concepts:**
- **Variation matching** — Same product with different sizes/colors = different cart items
- **Many-to-Many** — `variations.add(*product_variation)` adds multiple variations
- **Request.POST** — Form data from HTML form

### **Remove from Cart**

```python
def remove_cart(request, product_id, cart_item_id):
    """Decrease quantity or remove item"""
    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(
            product=product,
            user=request.user,
            id=cart_item_id
        )
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(
            product=product,
            cart=cart,
            id=cart_item_id
        )
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Remove if quantity becomes 0
    
    return redirect('cart')
```

### **View Cart**

```python
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        
        if request.user.is_authenticated:
            # User's cart
            cart_items = CartItem.objects.filter(
                user=request.user,
                is_active=True
            )
        else:
            # Session cart
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(
                cart=cart,
                is_active=True
            )
        
        # Calculate totals
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        
        tax = (2 * total) / 100  # 2% tax
        grand_total = total + tax
    
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)
```

**Key Concepts:**
- **Try-Except** — Handle cases where cart doesn't exist
- **ObjectDoesNotExist** — Django exception for missing objects
- **Calculation logic** — Totals, tax computed in view

---

## 📧 Authentication System

### **Custom User Registration**

```python
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]  # Generate username from email
            
            # Create user
            user = Account.objects.create_user(
                first_name=first_name,
                email=email,
                username=username,
                password=password
            )
            user.is_active = False  # Require email verification
            user.save()
            
            # Send verification email
            current_site = get_current_site(request)
            mail_subject = 'Please Activate your Account'
            message = render_to_string('accounts/account_varification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            return redirect('/accounts/login/?command=verification&email=' + email)
    else:
        form = RegistrationForm()
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
```

**Key Concepts:**
- **form.cleaned_data** — Validated form data
- **Email verification** — User must activate before login
- **Token generation** — Secure link for email verification
- **Base64 encoding** — Encode user ID for URL

### **Login with Cart Merge**

```python
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate user
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            # Merge anonymous cart to user cart
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                
                if is_cart_item_exists:
                    # Get items from session cart
                    cart_item = CartItem.objects.filter(cart=cart)
                    
                    # Extract variations from session cart
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))
                    
                    # Get user's existing cart items
                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)
                    
                    # Merge carts
                    for pr in product_variation:
                        if pr in ex_var_list:
                            # Increase quantity
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            # Add new item
                            cart_items = CartItem.objects.filter(cart=cart)
                            for cart_item in cart_items:
                                cart_item.user = user
                                cart_item.cart = None
                                cart_item.save()
            
            except:
                pass
            
            # Login user
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
```

**Key Concepts:**
- **Cart merge** — Anonymous cart items transferred to user account
- **Session management** — Authenticate and login user
- **Error messages** — Flash feedback to user

---

## 📋 Forms & Validation

Forms handle user input and validation. They're HTML + validation logic.

### **Registration Form**

```python
from django import forms
from .models import Account, UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
        # More field styling...
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("Password doesn't match!")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
```

**Key Concepts:**
- **ModelForm** — Automatically generates from model
- **clean()** — Custom validation logic
- **set_password()** — Hash password before saving
- **Widget** — HTML input element customization

---

## 🎨 Templates (Frontend)

Templates use Jinja2 syntax to render dynamic HTML.

### **Template Syntax**

```html
<!-- Variable interpolation -->
<h1>{{ product.product_name }}</h1>
<p>Price: ₹{{ product.price }}</p>

<!-- Conditional -->
{% if product.is_avilable %}
    <p>In Stock</p>
{% else %}
    <p>Out of Stock</p>
{% endif %}

<!-- Loops -->
{% for item in cart_items %}
    <tr>
        <td>{{ item.product.product_name }}</td>
        <td>{{ item.quantity }}</td>
        <td>₹{{ item.sub_total }}</td>
    </tr>
{% empty %}
    <tr><td>Cart is empty</td></tr>
{% endfor %}

<!-- URL reverse -->
<a href="{% url 'product_detail' product.category.slug product.slug %}">
    View Details
</a>

<!-- Static files -->
<img src="{% static 'images/logo.png' %}" alt="Logo">

<!-- Template inheritance -->
{% extends 'base.html' %}
{% block content %}
    <h1>Page content</h1>
{% endblock %}

<!-- Include other templates -->
{% include 'includes/navbar.html' %}

<!-- Context variable -->
{{ request.user.email }}
{{ request.user.is_authenticated }}
```

### **Base Template Structure**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Greatkart{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
</head>
<body>
    <!-- Navbar -->
    {% include 'includes/navbar.html' %}
    
    <!-- Messages -->
    {% include 'includes/alerts.html' %}
    
    <!-- Page content -->
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    
    <!-- Footer -->
    {% include 'includes/footer.html' %}
    
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### **Product Detail Template**

```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
<div class="container">
    <div class="row">
        <!-- Product Image -->
        <div class="col-md-6">
            <img src="{{ single_product.images.url }}" alt="{{ single_product.product_name }}">
        </div>
        
        <!-- Product Details -->
        <div class="col-md-6">
            <h1>{{ single_product.product_name }}</h1>
            
            <!-- Rating -->
            <div class="rating">
                ⭐ {{ single_product.averageReview }} / 5.0
                ({{ single_product.countReview }} reviews)
            </div>
            
            <!-- Price -->
            <h2>₹{{ single_product.price }}</h2>
            
            <!-- Stock -->
            {% if single_product.is_avilable %}
                <p class="text-success">In Stock</p>
            {% else %}
                <p class="text-danger">Out of Stock</p>
            {% endif %}
            
            <!-- Variations -->
            <form method="POST" action="{% url 'add_cart' single_product.id %}">
                {% csrf_token %}
                
                <!-- Color selection -->
                {% if single_product.variation_set.all %}
                    {% for variation in single_product.variation_set.all %}
                        {% if variation.variation_category == 'color' %}
                            <label>Color: 
                                <select name="color">
                                    <option value="{{ variation.variation_value }}">
                                        {{ variation.variation_value }}
                                    </option>
                                </select>
                            </label>
                        {% endif %}
                    {% endfor %}
                {% endif %}
                
                <button type="submit" class="btn btn-primary">Add to Cart</button>
            </form>
            
            <!-- Add to Wishlist -->
            {% if not in_cart %}
                <button class="btn btn-secondary">Add to Wishlist</button>
            {% endif %}
        </div>
    </div>
    
    <!-- Reviews Section -->
    <div class="row mt-5">
        <h3>Reviews</h3>
        {% for review in reviews %}
            <div class="review">
                <strong>{{ review.user.first_name }}</strong>
                <p>⭐ {{ review.rating }}/5</p>
                <p>{{ review.review }}</p>
            </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

**Key Concepts:**
- **{% static %}** — Reference static files
- **{{ model.method }}** — Call model methods in templates
- **{% csrf_token %}** — Security token for POST forms
- **Template inheritance** — Reduce HTML duplication
- **Context variables** — Pass data from view to template

---

## 🔗 URLs & Routing

URL routing maps URLs to views:

### **Root URLs (greatkart/urls.py)**

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('carts/', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### **App URLs (store/urls.py)**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]
```

**URL Patterns:**
- `<slug:category_slug>` — Capture slug parameter
- `<int:product_id>` — Capture integer parameter
- `name='product_detail'` — Reference URL by name (reverse lookup)

---

## 🔐 Context Processors

Context processors make data available to all templates:

### **Cart Context Processor**

```python
# carts/context_processors.py
from .models import Cart, CartItem
from .views import _cart_id

def cart_counter(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        except Cart.DoesNotExist:
            cart_items = []
    
    for cart_item in cart_items:
        cart_count += cart_item.quantity
    
    return dict(cart_count=cart_count)
```

**Register in settings.py:**
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                # ... default processors ...
                'carts.context_processors.cart_counter',
                'category.context_processors.menu_links',
            ],
        },
    },
]
```

**Usage in template:**
```html
<!-- cart_count is available in all templates -->
<span>Cart: {{ cart_count }} items</span>
```

### **Category Context Processor**

```python
# category/context_processors.py
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
```

**Usage in navbar template:**
```html
<nav>
    {% for category in links %}
        <a href="{{ category.get_url }}">{{ category.category_name }}</a>
    {% endfor %}
</nav>
```

---

## ⚙️ Settings & Configuration

### **Django Settings (greatkart/settings.py)**

```python
import os
from decouple import config

# Secret key (from .env file)
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for email
    'accounts',
    'store',
    'carts',
    'orders',
    'category',
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# User model
AUTH_USER_MODEL = 'accounts.Account'

# Custom field for new models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files (user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

---

## 🏪 Common Patterns

### **1. Get or 404**

```python
# Returns object or raises Http404
product = get_object_or_404(Product, slug=slug)
```

### **2. Filter or Empty**

```python
# Returns QuerySet (empty if no matches)
reviews = ReviewRating.objects.filter(product=product)
```

### **3. Create or Update**

```python
# Create
item = CartItem.objects.create(product=product, quantity=1, user=user)

# Update
item.quantity += 1
item.save()
```

### **4. Check Existence**

```python
# Fast check without fetching
exists = CartItem.objects.filter(product=product, user=user).exists()
```

### **5. Aggregate Calculations**

```python
from django.db.models import Avg, Count, Sum

avg_rating = Product.objects.aggregate(Avg('price'))['price__avg']
count = ReviewRating.objects.filter(product=product).aggregate(Count('id'))['id__count']
total_spent = OrderProduct.objects.aggregate(Sum('quantity'))['quantity__sum']
```

### **6. Queryset Methods**

```python
# Get all
all_products = Product.objects.all()

# Filter
available = Product.objects.filter(is_avilable=True)

# Exclude
not_electronics = Product.objects.exclude(category__name='Electronics')

# Order
sorted_by_price = Product.objects.order_by('-price')  # Descending

# Count
count = Product.objects.count()

# Distinct (remove duplicates)
unique_categories = Product.objects.values('category').distinct()

# First/Last
first = Product.objects.first()
last = Product.objects.last()

# Values/Values List (return dicts/tuples instead of objects)
names = Product.objects.values_list('product_name', flat=True)
```

---

## 🐛 Troubleshooting

### **Common Issues & Solutions**

#### **1. ModuleNotFoundError**

```
ModuleNotFoundError: No module named 'decouple'
```

**Solution:**
```powershell
python -m pip install python-decouple
```

#### **2. ImageField Errors**

```
ImportError: cannot import name 'Image' from 'PIL'
```

**Solution:**
```powershell
python -m pip install Pillow
```

#### **3. Database Not Found**

```
django.db.utils.OperationalError: no such table
```

**Solution:**
```powershell
python manage.py migrate
```

#### **4. Static Files Not Loading**

```powershell
python manage.py collectstatic --noinput
```

**Update settings:**
```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

#### **5. CSRF Token Missing**

Add to forms in templates:
```html
<form method="POST">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

#### **6. UnboundLocalError in Views**

**Problem:**
```python
def home(request):
    if products:
        reviews = ReviewRating.objects.filter(...)
    # Later...
    context = {'reviews': reviews}  # Error if products was empty
```

**Solution:**
```python
def home(request):
    reviews = {}  # Initialize before conditional
    if products:
        # Add to reviews
    context = {'reviews': reviews}
```

---

## 📚 Learning Resources & Next Steps

### **What You've Learned**

✅ Custom user models and authentication  
✅ Database relationships (FK, 1-to-1, M2M)  
✅ QuerySet methods and filtering  
✅ View functions and request handling  
✅ Forms and validation  
✅ Template rendering and inheritance  
✅ URL routing and reverse lookup  
✅ Context processors  
✅ Shopping cart logic  
✅ Order management  

### **Next Steps to Master Django**

1. **Class-Based Views (CBV)**
   - Replace function-based views with CBV
   - Learn Django's built-in generic views

2. **REST API**
   - Build API endpoints with Django REST Framework
   - Return JSON instead of HTML

3. **Testing**
   - Write unit tests for models and views
   - Use Django TestCase

4. **Deployment**
   - Deploy to Heroku, AWS, or DigitalOcean
   - Configure production database (PostgreSQL)
   - Set up CI/CD pipeline

5. **Advanced Features**
   - Celery for async tasks
   - Redis for caching
   - Elasticsearch for search
   - Payment integration (Stripe, Razorpay)

### **Debugging Tools**

```python
# Django shell - test code interactively
python manage.py shell
>>> from store.models import Product
>>> products = Product.objects.all()

# Print SQL queries
from django.db import connection
from django.test.utils import CaptureQueriesContext
with CaptureQueriesContext(connection) as queries:
    products = Product.objects.all()
print(queries)

# Django Debug Toolbar (optional)
pip install django-debug-toolbar
```

### **Django Documentation**

- Official docs: https://docs.djangoproject.com/
- Model API: https://docs.djangoproject.com/en/stable/ref/models/
- QuerySet API: https://docs.djangoproject.com/en/stable/ref/models/querysets/
- View decorators: https://docs.djangoproject.com/en/stable/topics/http/decorators/

---

## 🎯 Practice Exercises

### **Exercise 1: Add Wishlist Feature**

```python
# Create model
class Wishlist(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Create views for add/remove/view wishlist
```

### **Exercise 2: Product Search Improvement**

```python
# Add full-text search
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

results = Product.objects.annotate(
    search=SearchVector('product_name', 'description'),
).filter(
    search=SearchQuery(keyword)
).annotate(
    rank=SearchRank('search', SearchQuery(keyword))
).order_by('-rank')
```

### **Exercise 3: Admin Custom Actions**

```python
# Admin action to export orders
def export_orders(modeladmin, request, queryset):
    import csv
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    # Write CSV...
    return response
export_orders.short_description = "Export selected orders as CSV"

class OrderAdmin(admin.ModelAdmin):
    actions = [export_orders]
```

---

**Congratulations!** You now understand the complete Greatkart e-commerce project from database to frontend. 🎉

Keep practicing, build projects, and refer back to this guide anytime you need clarification.

Happy coding! 💻

