## RAG CHATBOT FOR WORDPRESS WEBSITES


[PDF FOR THE EXPLANATION](Explanation.pdf)

### ------------------------------------------------
<img width="1023" alt="Screenshot 2024-11-10 at 12 26 43 AM" src="https://github.com/user-attachments/assets/e59a6c73-b36d-401d-a3e6-44281c845001">


### THE KEY COMPONENTS ARE - 


**1. Wordpress Plugin:**

The Wordpress plugin is using Flask application of the chatbot to be plugged in to any wordpress app , and it responds to queries made by the user. The wordpress Plugin also retrieves the dymnamic url of the site the chatbot is plugged to and gives it to the Flask app that initilises the chtabot and fetches the sites content



**2. Flask Application:**

The Flask application is the main entry point for handling user queries.
It is responsible for initializing the chatbot instance using the URL provided by the WordPress plugin.
It passes the user queries to the chatbot's generate_response method and returns the responses back to the WordPress plugin.
WordPress Plugin:
The WordPress plugin is responsible for integrating the chatbot functionality into the WordPress site.
It fetches the website URL dynamically and passes it to the Flask application.
It recieves the chatbot's responses from the Flask application and display them to the user.



**3. RAG Chatbot as a PAckage:**

The chatbot code is packaged as a reusable Python package that can be installed using setup.py 

It is a sophisticated chatbot that combines Retrieval-Augmented Generation (RAG) with Chain of Thought reasoning to provide intelligent responses based on WordPress content. The chatbot fetches content from WordPress sites, processes it through various embedding and search mechanisms, and generates well-reasoned responses using OpenAI's GPT models.


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

