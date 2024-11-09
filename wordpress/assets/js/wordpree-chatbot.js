jQuery(document).ready(function($) {
    const chatbotMessages = $('.chatbot-messages');
    const chatbotForm = $('#chatbot-form');
    const chatbotQuery = $('#chatbot-query');

    function addMessage(message, isUser = false) {
        const messageDiv = $('<div>')
            .addClass('message')
            .addClass(isUser ? 'user-message' : 'bot-message')
            .text(message);
        chatbotMessages.append(messageDiv);
        chatbotMessages.scrollTop(chatbotMessages[0].scrollHeight);
    }

    chatbotForm.on('submit', function(e) {
        e.preventDefault();
        
        const query = chatbotQuery.val().trim();
        if (!query) return;

        addMessage(query, true);
        chatbotQuery.val('');

        $.ajax({
            url: chatbotSettings.ajax_url,
            type: 'POST',
            data: {
                action: 'chatbot_query',
                query: query
            },
            success: function(response) {
                if (response.success) {
                    const data = response.data;
                    addMessage(data.final_response);
                    
                    // Optionally show thought process
                    console.log('Thought steps:', data.thought_steps);
                } else {
                    addMessage('Sorry, I encountered an error. Please try again.');
                }
            },
            error: function() {
                addMessage('Sorry, I encountered an error. Please try again.');
            }
        });
    });

    // Minimize functionality
    $('.minimize-btn').on('click', function() {
        $('.wp-flask-chatbot').toggleClass('minimized');
    });
});
