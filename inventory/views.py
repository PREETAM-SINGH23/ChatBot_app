# inventory/views.py

import nltk
from django.shortcuts import render
from .models import Product

# Ensure the punkt resource is downloaded
try:
    nltk.data.find('tokenizers/punkt')
    import nltk
    print(nltk.data.path,"path")
except LookupError:
    nltk.download('punkt')

def chatbot_response(request):
    user_input = request.GET.get('user_input')
    response = "I'm sorry, I didn't understand that."

    if user_input:
        # Tokenize the user input
        tokens = nltk.word_tokenize(user_input)
        print(tokens,"ss")
        # Filter out punctuation and create a list of keywords
        keywords = [word for word in tokens if word.isalnum()]
        
        # Fetch products that match the keywords
        products = Product.objects.filter(name__icontains=' '.join(keywords))
        
        if products.exists():
            response = "Here are the products I found:\n" + "\n".join([str(product) for product in products])
        else:
            response = "No products found matching your query."

    return render(request, 'chatbot_response.html', {'response': response})