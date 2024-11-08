## WE WOULD NEED TO FETCH DATA FROM THE WORDPRESS SITE SO THIS CLASS WILL FETCH DATA FROM WORDPRESS SITE AND RETURN CLEANED POSTS##
##THESE CLEANED POSTS WILL BE IN A LIST FORMAT AND WOULD BE USED FOR TRAINING THE CHATBOT## 


import requests
import json
import time
import re
from typing import List, Dict
from .html_cleaner import HTMLCleaner


class WordPressContentFetcher:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.api_endpoint = "/wp-json/wp/v2"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        }
        self.retry_count = 3
        self.retry_delay = 2  # seconds

    def _make_request(self, url: str, retries: int = 3) -> Dict:
        """Make HTTP request with retry logic and error handling"""
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=30)
                response.raise_for_status()
                
                # Try to decode JSON with error handling
                try:
                    return response.json()
                except json.JSONDecodeError as e:
                    # If JSON is malformed, try to clean the response
                    cleaned_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', response.text)
                    return json.loads(cleaned_text)
                    
            except requests.exceptions.RequestException as e:
                if attempt == retries - 1:
                    print(f"Failed to fetch URL after {retries} attempts: {url}")
                    print(f"Error: {str(e)}")
                    return {}
                time.sleep(self.retry_delay)
                
            except json.JSONDecodeError as e:
                if attempt == retries - 1:
                    print(f"Failed to decode JSON from URL: {url}")
                    print(f"Error: {str(e)}")
                    return {}
                time.sleep(self.retry_delay)

    def _get_total_pages(self) -> int:
        """Get total number of pages available"""
        url = f"{self.base_url}{self.api_endpoint}/posts?per_page=100"
        response = requests.head(url, headers=self.headers)
        total_pages = int(response.headers.get('X-WP-TotalPages', 1))
        return total_pages

    def fetch_all_posts(self) -> List[str]:
        """Fetch all posts from WordPress site with improved error handling"""
        all_posts_content = []
        total_pages = self._get_total_pages()
        
        for page in range(1, total_pages + 1):
            print(f"Fetching page {page} of {total_pages}")
            url = f"{self.base_url}{self.api_endpoint}/posts"
            params = {
                'per_page': 20,  # Reduced page size for better stability
                'page': page,
                'status': 'publish',
                '_fields': 'content'  # Only fetch content field to reduce response size
            }
            
            try:
                response = requests.get(url, params=params, headers=self.headers, timeout=30)
                response.raise_for_status()
                posts = response.json()
                
                for post in posts:
                    if 'content' in post and 'rendered' in post['content']:
                        cleaned_content = HTMLCleaner.clean_html(post['content']['rendered'])
                        if cleaned_content:  # Only add non-empty content
                            all_posts_content.append(cleaned_content)
                
                # Add delay between requests to avoid overwhelming the server
                time.sleep(1)
                
            except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
                print(f"Error on page {page}: {str(e)}")
                continue
                
        return all_posts_content
