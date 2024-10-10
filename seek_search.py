import requests
from bs4 import BeautifulSoup
import re

try:
    response = requests.get("https://seek.com.au/it-help-desk-jobs/in-all-melbourne-vic")

    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

     # Find all script tags
    script_tags = soup.find_all('script')
    
    print(f"Found {len(script_tags)} script tags.")
    
    for i, tag in enumerate(script_tags, 1):
        print(f"\nScript Tag {i}:")
        
        # Print the first 200 characters of the script content
        content = tag.string if tag.string else ""
        print(content[:200] + "..." if len(content) > 200 else content)
        
        # Check if this script contains the job data
        if re.search(r'window.SEEK_REDUX_DATA', str(tag)):
            print("*** This script tag likely contains the job data ***")
except requests.RequestException as e:
    print(f"Error: {e}")