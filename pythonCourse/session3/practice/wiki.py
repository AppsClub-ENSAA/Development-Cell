
#!/usr/bin/env python3
"""
🌐 Web Scraping & Functions 

You have a list `data` of GDP values (floats). Write three functions:

* `my_min(data)` → returns the smallest value
* `my_max(data)` → returns the largest value
* `my_average(data)` → returns the arithmetic mean

**Do not use** Python's built-in `min()`, `max()`, or `sum()`.

After that, print the results .

"""

import requests
from bs4 import BeautifulSoup

from functions import summary 

# Stable example: Wikipedia table with country GDP
URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)

#print(response)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup)


table = soup.find("table", {"class": "wikitable"})
# print(table)
data = []

for row in table.find_all("tr")[1:]:  # skip header
    cols = row.find_all("td")
    # print(table)
    
    if cols:
        gdp_text = cols[1].text.strip()  # GDP column
        gdp_text = gdp_text.replace(",", "")
     
        try:
            value = float(gdp_text)
            data.append(value)
        except ValueError:
            continue
        
