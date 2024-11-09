from flask import Flask, request, jsonify, render_template
from chatbot.rag_chatbot import RAGChatbot
from flask_cors import CORS
import os

def create_app(wordpress_base_url=None):
    app = Flask(__name__)
    CORS(app)  # Enable CORS for WordPress integration
    
    # Initialize chatbot with the WordPress URL
    chatbot = RAGChatbot()
    if wordpress_base_url:
        chatbot.initialize(wordpress_base_url)
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/query', methods=['POST'])
    def process_query():
        try:
            data = request.get_json()
            query = data.get('query')
            
            if not query:
                return jsonify({'error': 'No query provided'}), 400
            
            response = chatbot.process_query(query)
            return jsonify(response)
            
        except Exception as e:
            app.logger.error(f"Error processing query: {str(e)}")
            return jsonify({'error': 'Internal server error'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)