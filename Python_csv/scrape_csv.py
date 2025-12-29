import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

# 1. URL and Headers (Headers help avoid the AttributeError)
url = "https://en.wikipedia.org/wiki/Delimiter-separated_values"
headers = {'User-Agent': 'Mozilla/5.0'}

# 2. Get the page content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find the CSV text 
# We add a check to make sure it actually finds the tag first
csv_tag = soup.find('pre')

if csv_tag:
    csv_text = csv_tag.get_text().strip()
    
    # 4. Save to CSV file
    with open("wiki_data.csv", "w") as f:
        f.write(csv_text)

    # 5. Verify with Pandas
    df = pd.read_csv(io.StringIO(csv_text))
    print("--- SUCCESS! Data found: ---")
    print(df)
else:
    print("Error: Could not find the data on the page. Please check your internet.")