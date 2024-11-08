<?php
/*
Plugin Name: Chatbot Plugin
Plugin URI: https://example.com/chatbot-plugin
Description: Integrate the chatbot functionality into WordPress
Version: 1.0
Author: Your Name
Author URI: https://example.com
*/
class ChatbotPlugin {
    private $api_url;
    public function __construct() {
        $this->api_url = get_site_url() . '/query';        ## GETS THE URL OF THE SITE THIS PLUGIN IS PLUGGED UPON ##
        add_action('wp_footer', array($this, 'render_chatbot'));
        add_shortcode('chatbot', array($this, 'chatbot_shortcode'));
    }

    public function render_chatbot() {
        $wordpress_base_url = get_site_url();
        ?>
        <div id="chatbot-container"></div>
        <script>
            function processQuery(query) {
                fetch('<?php echo $this->api_url; ?>', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ query: query })
                })
                .then(response => response.json())
                .then(data => {
                    // Display the chatbot's response
                    document.getElementById('chatbot-container').innerHTML = data.final_response;
                })
                .catch(error => {
                    console.error('Error processing query:', error);
                });
            }
        </script>
        <?php
    }

    public function chatbot_shortcode($atts, $content = null) {
        ob_start();
        $this->render_chatbot();
        return ob_get_clean();
    }
}

// Create the Flask app with the Wordpress base URL
$app = create_app(get_site_url());

new ChatbotPlugin();
?>