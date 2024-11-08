from flask import Flask, request, jsonify
from chatbot.rag_chatbot import RAGChatbot

app = Flask(__name__)

def create_app(wordpress_base_url):
    """Factory function to create the Flask app with the provided Wordpress base URL"""
    # Initialize the chatbot
    chatbot = RAGChatbot()
    chatbot.initialize(wordpress_base_url)

    @app.route('/query', methods=['POST'])
    def process_query():
        query = request.json['query']
        response = chatbot.process_query(query)
        return jsonify(response)

    return app

if __name__ == '__main__':
    # You'll need to pass your own WORDPRESS_BASE_URL when running the app if you are not retreiving it from the Wordpress Plugin
    app = create_app(None)
    app.run(debug=True)