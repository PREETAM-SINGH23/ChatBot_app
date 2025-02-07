# Supplier Product Chatbot

A Django-based chatbot application that allows users to query information about products and suppliers. The chatbot utilizes LangGraph for workflow management and integrates with an open-source language model for enhanced responses.

## Features

- Query products by brand.
- Retrieve suppliers based on product types.
- Get detailed information about specific products.

## Technologies Used

- Django
- NLTK (Natural Language Toolkit)
- SQLite (default database)

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/supplier_product_chatbot.git
cd supplier_product_chatbot
```

## Download NLTK Data
You may need to download the NLTK punkt tokenizer. You can do this by running the following commands in the Django shell:
```bash
python manage.py shell
```

Then, in the shell:

```bash
import nltk
nltk.download('punkt')
```
## Database Setup
1. Run migrations to set up the database:
```bash
python manage.py migrate
```
2. Populate the database with sample data (if applicable):
```bash
python populate_data.py
```

## Running the Application
To start the Django development server, run:
```bash
python manage.py runserver
```
You can access the chatbot at http://127.0.0.1:8000/chatbot/.

## Usage
- Type your queries in the input box and press "Send".
- Example queries:
  - "Show me all products under brand X."
  - "Which suppliers provide laptops?"
  - "Give me details of product ABC."
 
## Acknowledgments
- Django
- NLTK

  
### Notes
- **Populate Data**: If you have a script for populating the database with sample data, ensure that the command is correct.

This `README.md` file provides a comprehensive overview of your project and should help users understand how to set it up and use it effectively. Feel free to modify it according to your project's specific needs!
