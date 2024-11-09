document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('chatbot-form');
    const input = document.getElementById('query');
    const messages = document.getElementById('chatbot-messages');

    function addMessage(message, isUser = false) {
        const div = document.createElement('div');
        div.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        div.textContent = message;
        messages.appendChild(div);
        messages.scrollTop = messages.scrollHeight;
    }

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const query = input.value.trim();
        if (!query) return;

        addMessage(query, true);
        input.value = '';

        try {
            const response = await fetch('/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: query })
            });

            const data = await response.json();
            
            if (response.ok) {
                addMessage(data.final_response);
            } else {
                addMessage('Sorry, I encountered an error. Please try again.');
            }
        } catch (error) {
            console.error('Error:', error);
            addMessage('Sorry, I encountered an error. Please try again.');
        }
    });
});