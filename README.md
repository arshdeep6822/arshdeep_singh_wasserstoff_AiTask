## RAG CHATBOT FOR WORDPRESS WEBSITES

### ------------------------------------------------
**This project consists:**

1. The Chatbot WordPress Plugin:
   - This plugin will be integrated into a WordPress website.
   - The key responsibilities of the WordPress plugin are:
     - Provide a way to integrate the existing chatbot functionality into the WordPress site.
     - Fetch the website URL dynamically based on the site the plugin is deployed on.
     - Pass the dynamic website URL to the Flask application.

2. The Flask Application:
   - This is a separate component from the WordPress plugin.
   - The Flask application is responsible for the chatbot-specific functionality.
   - The main tasks of the Flask application are:
     - Initialize the chatbot instance using the website URL provided by the WordPress plugin.
     - Handle user queries and pass them to the chatbot's `generate_response` method.
     - Return the chatbot's responses back to the user.

The high-level flow is:

1. The user interacts with the chatbot interface on the WordPress site.
2. The WordPress plugin fetches the website URL dynamically.
3. The WordPress plugin passes the website URL to the Flask application.
4. The Flask application initialises the chatbot instance using the provided URL.
5. The user's queries are sent to the Flask application.
6. The Flask application passes the queries to the chatbot's `generate_response` method.
7. The chatbot's responses are returned to the Flask application.
8. The Flask application sends the responses back to the WordPress plugin, which displays them to the user.

This separation of concerns between the WordPress plugin and the Flask application allows for better modularity, maintainability, and flexibility in the overall system.

### ------------------------------------------------


### THE KEY COMPONENTS ARE - 


**1. Chatbot as a package:**

The chatbot code will be packaged as a reusable Python package that can be installed using setup.py.
This will allow the chatbot functionality to be easily integrated into other applications.



**2. Flask Application:**

The Flask application will be the main entry point for handling user queries.
It will be responsible for initializing the chatbot instance using the URL provided by the WordPress plugin.
It will pass the user queries to the chatbot's generate_response method and return the responses back to the WordPress plugin.
WordPress Plugin:
The WordPress plugin will be responsible for integrating the chatbot functionality into the WordPress site.
It will fetch the website URL dynamically and pass it to the Flask application.
It will receive the chatbot's responses from the Flask application and display them to the user.



**3. WordPress RAG Chatbot:**

A sophisticated chatbot that combines Retrieval-Augmented Generation (RAG) with Chain of Thought reasoning to provide intelligent responses based on WordPress content. The chatbot fetches content from WordPress sites, processes it through various embedding and search mechanisms, and generates well-reasoned responses using OpenAI's GPT models.


The system consists of several key components working together:

1. Content Retrieval (WordPressContentFetcher)-
- Fetches posts from WordPress sites using the WP REST API
- Implements robust error handling and retry mechanisms
- Cleans HTML content to extract meaningful text
- Includes rate limiting to prevent server overload

2. Text Processing-
- Splits large texts into manageable chunks using RecursiveCharacterTextSplitter
- Maintains context through configurable chunk overlap
- Removes HTML artifacts and normalizes text formatting

3. Vector Storage and Search (VectorStore)-
- Uses SentenceTransformers for generating embeddings
- Implements FAISS for efficient similarity search
- Stores and indexes processed text chunks
- Enables quick retrieval of relevant content

4. Chain of Thought Processing-
- Implements explicit reasoning steps for query processing
- Uses OpenAI's GPT-3.5-turbo model
- Breaks down complex queries into logical steps
- Refines responses through structured reasoning

5. Response Generation-
The chatbot processes queries in three stages:
stage 1 - Initial Response: Generates a first draft based on retrieved content
stage 2 - Thought Steps: Develops explicit reasoning steps
stage 3 - Final Response: Refines the answer based on the reasoning process

### Key Features

- **Robust Error Handling**: Implements retry mechanisms and graceful error recovery
- **Efficient Content Processing**: Uses chunking and vector search for fast retrieval
- **Chain of Thought Reasoning**: Provides transparent reasoning steps
- **Configurable Parameters**: Customizable chunk sizes, retry counts, and search parameters
- **WordPress Integration**: Seamless integration with any WordPress site's REST API

