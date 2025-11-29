from django.shortcuts import render

from store.models import Product, ReviewRating

def home(request):

    products = Product.objects.all().filter(is_avilable=True).order_by('created_date')

    # Collect reviews per product to avoid UnboundLocalError when no products exist
    reviews = {}
    for product in products:
        reviews[product.id] = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,  # dict: product_id -> QuerySet of reviews
    }

    return render(request, 'home.html', context=context)