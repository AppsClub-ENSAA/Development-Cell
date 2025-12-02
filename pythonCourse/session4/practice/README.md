FastAPI Product Catalog Service

This project hosts a set of simple API endpoints designed to manage and query a large simulated product catalog (1 million items).

🛠️ Prerequisites

To run this application, you need:

Python 3.8+

⚙️ Setup and Installation

1. Save the Code

Save the provided Python code into a file named main.py.

2. Install Dependencies

Install the required Python packages using pip:

pip install fastapi uvicorn


3. Run the Server

Start the application using the uvicorn server. Note that the application will take a few moments to generate the 1,000,000 product items before the server is fully ready.

uvicorn main:app --reload


You should see confirmation output similar to this:

📦 Generating Warehouse Data (1 Million Items)...
✅ System Ready!
Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000) (Press CTRL+C to stop)


🌐 Accessing the API

1. Website Access

Once the server is running, you can access the interactive API documentation (Swagger UI) by opening the following link in your web browser:

http://127.0.0.1:8000/docs

2. Available Endpoints

You can test the following endpoints from the documentation interface:

Item Lookup:

/slow/{item_id}

/fast/{item_id}

Analytics:

/analytics/slow

/analytics/fast
