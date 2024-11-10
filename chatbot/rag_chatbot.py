## the RAGChatbot class, a chatbot that uses a Retrieval-Augmented Generation (RAG) approach to answer queries by leveraging external content from a WordPress site.##
## It combines the fetched content with OpenAI's language model to provide informed, well-structured answer ##




from .content_fetcher import WordPressContentFetcher
from .text_splitter import TextSplitter
from .vector_store import VectorStore
from .ChainOfThought_processor import ChainOfThoughtProcessor
from openai import OpenAI
import os
from dotenv import load_dotenv
from typing import Dict

class RAGChatbot:
    def __init__(self):
        # Load environment variables from .env file if present
        load_dotenv()

        # Get API key from environment variable
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")

        self.content_fetcher = None
        self.vector_store = VectorStore()
        self.cot_processor = ChainOfThoughtProcessor(self.openai_api_key)
        self.client = OpenAI(api_key=self.openai_api_key)


## Initializes the chatbot by fetching, processing, and storing WordPress content ##
    def initialize(self, base_url: str):
        """Initialize the chatbot with a given base URL"""
        self.content_fetcher = WordPressContentFetcher(base_url)

        # Check API availability first
        if not self.content_fetcher.check_api_availability():
            raise Exception("WordPress REST API is not available for this site")

        # Fetch content
        posts_content = self.content_fetcher.fetch_all_posts()

        if not posts_content:
            raise Exception("No content could be fetched from the WordPress site")

        # Split texts
        split_posts = TextSplitter.split_texts(posts_content)

        # Add to vector store
        self.vector_store.add_texts(split_posts)

        print(f"Successfully initialized with {len(posts_content)} posts")


## Generates an initial response based on the query and relevant information retrieved from VectorStore ##
    def get_initial_response(self, query: str, relevant_text: str) -> str:
        """Generate initial response"""
        initial_prompt = f"""
        Given the following information, provide an initial answer to the query:
        Query: {query}
        Relevant Information: {relevant_text}
        """

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": initial_prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content


## Main method to handle the entire query processing pipeline, returning a response with detailed reasoning.##

    def process_query(self, query: str) -> Dict[str, str]:
        """Process a query and return response with reasoning"""
        # Get relevant texts
        relevant_texts = self.vector_store.search(query)
        relevant_text = ' '.join(relevant_texts)

        # Generate initial response
        initial_response = self.get_initial_response(query, relevant_text)

        # Generate reasoning steps
        thought_steps = self.cot_processor.develop_reasoning_steps(
            query,
            relevant_text,
            initial_response
        )

        # Generate final response
        final_response = self.cot_processor.refine_response(
            query,
            relevant_text,
            thought_steps
        )

        return final_response
