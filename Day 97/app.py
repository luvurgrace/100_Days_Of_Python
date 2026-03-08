"""
F1 Shop with Stripe Payment
"""

from flask import Flask, render_template, redirect, url_for, request, flash, session
import stripe
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# === STRIPE CONFIG ===
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')

# === PRODUCTS ===

PRODUCTS = [
    {
        'id': 1,
        'name': 'Red Bull Racing Cap',
        'team': 'Red Bull',
        'price': 35.00,
        'image': 'https://hatstore.imgix.net/196996568720_1.jpg'
    },
    {
        'id': 2,
        'name': 'Ferrari Team T-Shirt',
        'team': 'Ferrari',
        'price': 55.00,
        'image': 'https://fueler.store/cdn/shop/files/scuderia-ferrari-2025-team-t-shirt-fuelertm-701232809001802-fueler-store-92970.jpg?v=1759273166&width=3000'
    },
    {
        'id': 3,
        'name': 'Mercedes AMG Hoodie',
        'team': 'Mercedes',
        'price': 89.00,
        'image': 'https://i.sportisimo.com/products/images/2031/2031252/700x700/puma-mapf1-ess-hoodie_0.jpg'
    },
    {
        'id': 4,
        'name': 'McLaren Team Jacket',
        'team': 'McLaren',
        'price': 120.00,
        'image': 'https://fueler.store/cdn/shop/files/mclaren-f1-2025-softshell-team-jacket-fuelertm-tu9917-088-s-fueler-store-45331.jpg?v=1759276499&width=1080'
    },
    {
        'id': 5,
        'name': 'Aston Martin Polo',
        'team': 'Aston Martin',
        'price': 65.00,
        'image': 'https://gpshop.cdn.shoprenter.hu/custom/gpshop/image/data/product/AMF1_2025/aston-martin-polo-2025-701233031002-1.jpg.webp?lastmod=1740227478.1738324618'
    },
    {
        'id': 6,
        'name': 'Alpine Team Backpack',
        'team': 'Alpine',
        'price': 79.00,
        'image': 'https://www.oreca-store.com/media/catalog/product/s/a/sac-a-dos-bwt-alpine-f1-team-202420250106190645677c1bb5790ba.jpg'
    },
]


def get_product(id):
    for p in PRODUCTS:
        if p['id'] == id:
            return p
    return None


def get_cart_items():
    cart = session.get('cart', {})
    items = []
    total = 0
    for product_id, qty in cart.items():
        product = get_product(int(product_id))
        if product:
            subtotal = product['price'] * qty
            total += subtotal
            items.append({
                'product': product,
                'quantity': qty,
                'subtotal': subtotal
            })
    return items, total


@app.context_processor
def cart_count():
    cart = session.get('cart', {})
    return {'cart_count': sum(cart.values())}


# === ROUTES ===

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)


@app.route('/add/<int:id>')
def add_to_cart(id):
    cart = session.get('cart', {})
    key = str(id)
    cart[key] = cart.get(key, 0) + 1
    session['cart'] = cart
    flash('Added to cart!')
    return redirect(url_for('index'))


@app.route('/cart')
def cart():
    items, total = get_cart_items()
    return render_template('cart.html', items=items, total=total)


@app.route('/update/<int:id>', methods=['POST'])
def update_cart(id):
    cart = session.get('cart', {})
    qty = int(request.form.get('qty', 1))
    if qty > 0:
        cart[str(id)] = qty
    else:
        cart.pop(str(id), None)
    session['cart'] = cart
    return redirect(url_for('cart'))


@app.route('/remove/<int:id>')
def remove_from_cart(id):
    cart = session.get('cart', {})
    cart.pop(str(id), None)
    session['cart'] = cart
    return redirect(url_for('cart'))


# === STRIPE CHECKOUT ===

@app.route('/checkout', methods=['POST'])
def checkout():
    items, total = get_cart_items()

    if not items:
        flash('Cart is empty!')
        return redirect(url_for('cart'))

    # Создаём line_items для Stripe
    line_items = []
    for item in items:
        line_items.append({
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item['product']['name'],
                    'images': [item['product']['image']],
                },
                'unit_amount': int(item['product']['price'] * 100),  # в центах!
            },
            'quantity': item['quantity'],
        })

    try:
        # Создаём Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=url_for('success', _external=True),
            cancel_url=url_for('cart', _external=True),
        )

        # Перенаправляем на страницу оплаты Stripe
        return redirect(checkout_session.url)

    except Exception as e:
        flash(f'Payment error: {str(e)}')
        return redirect(url_for('cart'))


@app.route('/success')
def success():
    session.pop('cart', None)  # Очищаем корзину
    return render_template('success.html')


@app.route('/cancel')
def cancel():
    flash('Payment cancelled')
    return redirect(url_for('cart'))


if __name__ == '__main__':
    app.run(debug=True)
