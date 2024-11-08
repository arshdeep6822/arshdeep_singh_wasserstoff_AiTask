from bs4 import BeautifulSoup
import re



## WE WILL NEED TO CLEAN THE POSTS FETCHED FROM THE WEBSITE AS IT MIGHT CONTAIN HTML TAGS AND OTHER THINGS THAT CANNOT BE HANDLED BY SentenceTransformer


class HTMLCleaner:
    @staticmethod
    def clean_html(html_content: str) -> str:
        """Clean HTML content and extract text"""
        soup = BeautifulSoup(html_content, 'html.parser')
        for script in soup(["script", "style", "code", "noscript"]):
            script.decompose()
        text = soup.get_text(separator=' ', strip=True)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()