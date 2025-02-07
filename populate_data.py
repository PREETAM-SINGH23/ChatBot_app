# populate_data.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supplier_product_chatbot.settings')
django.setup()

from inventory.models import Supplier, Product

def populate():
    # Create sample suppliers
    supplier1 = Supplier.objects.create(
        name='Tech Supplies Inc.',
        contact_info='contact@techsupplies.com',
        product_categories_offered='Laptops, Desktops, Accessories'
    )

    supplier2 = Supplier.objects.create(
        name='Gadget World',
        contact_info='info@gadgetworld.com',
        product_categories_offered='Smartphones, Tablets, Accessories'
    )

    # Create sample products
    Product.objects.create(
        name='Laptop X1',
        brand='Brand A',
        price=999.99,
        category='Laptops',
        description='High-performance laptop for professionals.',
        supplier=supplier1
    )

    Product.objects.create(
        name='Smartphone Z',
        brand='Brand B',
        price=699.99,
        category='Smartphones',
        description='Latest smartphone with advanced features.',
        supplier=supplier2
    )

    Product.objects.create(
        name='Desktop Y',
        brand='Brand A',
        price=1299.99,
        category='Desktops',
        description='Powerful desktop for gaming and work.',
        supplier=supplier1
    )

    print("Sample data populated successfully!")

if __name__ == '__main__':
    populate()