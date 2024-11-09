## RAG CHATBOT FOR WORDPRESS WEBSITES


[PDF FOR THE EXPLANATION](Explanation.pdf)

### ------------------------------------------------


### THE KEY COMPONENTS ARE - 


**1. Chatbot as a package:**

The chatbot code is packaged as a reusable Python package that can be installed using setup.py.



**2. Flask Application:**

The Flask application is the main entry point for handling user queries.
It is responsible for initializing the chatbot instance using the URL provided by the WordPress plugin.
It passes the user queries to the chatbot's generate_response method and returns the responses back to the WordPress plugin.
WordPress Plugin:
The WordPress plugin is responsible for integrating the chatbot functionality into the WordPress site.
It fetches the website URL dynamically and passes it to the Flask application.
It recieves the chatbot's responses from the Flask application and display them to the user.



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

