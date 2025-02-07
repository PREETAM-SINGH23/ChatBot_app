# langgraph_workflow.py

from langgraph import LangGraph

from Server.supplier_product_chatbot.inventory.models import Product, Supplier

# Initialize LangGraph
graph = LangGraph()

# Define nodes for different intents
@graph.node
def handle_product_query(brand_name):
    # Logic to fetch products by brand
    products = Product.objects.filter(brand__icontains=brand_name)
    return products

@graph.node
def handle_supplier_query(product_type):
    # Logic to fetch suppliers by product type
    suppliers = Supplier.objects.filter(product_categories_offered__icontains=product_type)
    return suppliers

@graph.node
def handle_product_details(product_name):
    # Logic to fetch product details
    product = Product.objects.get(name__iexact=product_name)
    return product

# Define the main workflow
@graph.workflow
def chatbot_workflow(user_input):
    # Parse user input and determine intent
    if "show me all products under brand" in user_input.lower():
        brand_name = user_input.split("under brand")[-1].strip()
        return handle_product_query(brand_name)
    elif "which suppliers provide" in user_input.lower():
        product_type = user_input.split("provide")[-1].strip()
        return handle_supplier_query(product_type)
    elif "give me details of product" in user_input.lower():
        product_name = user_input.split("product")[-1].strip()
        return handle_product_details(product_name)
    else:
        return "I'm sorry, I didn't understand that."