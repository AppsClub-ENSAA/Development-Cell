from fastapi import FastAPI
import time
import random

app = FastAPI()

# --- 1. SETUP DATA ---
print("📦 Generating Warehouse Data (1 Million Items)...")

BAD_DATABASE = []
PROMO_ITEMS = [] # List for Promo IDs
CHEAP_ITEMS = [] # List for Cheap IDs (< 150$)


for i in range(1_000_000):
    name = f"Product-{i}"
    price = i * 0.5
    
    BAD_DATABASE.append([i, name, price])

    if random.random() < 0.1:
        PROMO_ITEMS.append(i)
        
    if price < 150:
        CHEAP_ITEMS.append(i)

print("✅ System Ready!")

# --- 2. ENDPOINT: INDIVIDUAL ITEM RETRIEVAL ---

@app.get("/slow/{item_id}") 
def get_item_slow(item_id: int):
    """
    Retrieves an item by item_id using a linear search (O(N) complexity).
    Uses the inefficient list-of-lists (BAD_DATABASE).
    """
    start = time.time()
    
    result = None
    for record in BAD_DATABASE:
        if record[0] == item_id:
            result = {"name": record[1], "price": record[2]}
            break
            
    duration = time.time() - start
    return {"item": result, "time_taken": duration}


@app.get("/fast/{item_id}")
def get_item_fast(item_id: int):
    start = time.time()
    name = price = None
    
    # TASK 1: Implement the logic to retrieve the item data directly efficiently

    
    duration = time.time() - start
    return {"item": {"name": name, "price": price}, "time_taken": duration}


# --- 3. ENDPOINT: ANALYTICS (Finding "Cheap Promo" Items) ---

@app.get("/analytics/slow")
def get_deals_slow():
    """
    Finds the intersection of PROMO_ITEMS and CHEAP_ITEMS using a loop 
    and list membership checking (O(N*M) worst-case complexity).
    """
    start = time.time()
    
    count = 0
    for p_id in PROMO_ITEMS:
        if p_id in CHEAP_ITEMS:
            count += 1
            
    duration = time.time() - start
    return {"count": count, "time_taken": duration}



@app.get("/analytics/fast")
def get_deals_fast():
    start = time.time()
    
    # TASK 2: Implement the efficient analytics logic.
    count = 0 

    
    duration = time.time() - start
    return {"count": count, "time_taken": duration}
