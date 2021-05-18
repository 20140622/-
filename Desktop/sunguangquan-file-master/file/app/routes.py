from flask import Blueprint, render_template, request
from app.models import Brand, Product
import json
web = Blueprint('web', __name__, url_prefix='/')


@web.route('/')
def index():
    return render_template('index.html')


@web.route('/brand')
def get_brand():
    return render_template('brand.html')


@web.route('/search', methods=['POST'])
def search():
    k = request.form.get('keyword')
    product = Product.query.filter_by(brandCN=k)

    for p in product:
        print(dir(p))
    return render_template('search.html', product=product)
