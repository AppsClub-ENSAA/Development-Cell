# FastAPI Product Catalog Service

A small API that manages and searches a big fake product catalog (1,000,000 items).

## Requirements
- Python 3.8+

## Setup

1. Put the code in a file
Save everything in a file called main.py.

2. Install packages
```pip install fastapi uvicorn```

3. Run the server
```uvicorn main:app --reload```

When it starts, you should see something like:
Generating Warehouse Data (1 Million Items)...
System Ready!
Uvicorn running on http://127.0.0.1:8000

## Using the API

Open the docs (Swagger UI):
http://127.0.0.1:8000/docs

## Endpoints:

Item lookup:
- /slow/{item_id}
- /fast/{item_id}

Analytics:
- /analytics/slow
- /analytics/fast
