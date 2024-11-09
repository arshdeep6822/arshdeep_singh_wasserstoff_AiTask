<?php
/*
Plugin Name: WordPress Flask Chatbot
Description: A chatbot powered by Flask and RAG
Version: 1.0
Author: Arshdeep Singh
*/

if (!defined('ABSPATH')) exit;

class WordPressFlaskChatbot {
    private $plugin_path;
    private $plugin_url;

    public function __construct() {
        $this->plugin_path = plugin_dir_path(__FILE__);
        $this->plugin_url = plugin_dir_url(__FILE__);
        
        add_action('wp_enqueue_scripts', array($this, 'enqueue_scripts'));
        add_action('wp_footer', array($this, 'render_chatbot'));
        add_shortcode('chatbot', array($this, 'chatbot_shortcode'));
        
        // Add AJAX handlers
        add_action('wp_ajax_chatbot_query', array($this, 'handle_query'));
        add_action('wp_ajax_nopriv_chatbot_query', array($this, 'handle_query'));
    }

    public function enqueue_scripts() {
        wp_enqueue_style(
            'wordpress-chatbot',
            $this->plugin_url . 'assets/css/wordpress-chatbot.css',
            array(),
            '1.0.0'
        );

        wp_enqueue_script(
            'wordpress-chatbot',
            $this->plugin_url . 'assets/js/wordpress-chatbot.js',
            array('jquery'),
            '1.0.0',
            true
        );

        wp_localize_script('wordpress-chatbot', 'chatbotSettings', array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'site_url' => get_site_url(),
            'flask_url' => 'http://localhost:5000' // Configure this based on your Flask app URL
        ));
    }

    public function render_chatbot() {
        include $this->plugin_path . 'templates/chatbot.php';
    }

    public function chatbot_shortcode() {
        ob_start();
        $this->render_chatbot();
        return ob_get_clean();
    }

    public function handle_query() {
        $query = sanitize_text_field($_POST['query']);
        
        // Make request to Flask app
        $response = wp_remote_post('http://localhost:5000/query', array(
            'body' => json_encode(array('query' => $query)),
            'headers' => array('Content-Type' => 'application/json'),
        ));

        if (is_wp_error($response)) {
            wp_send_json_error('Failed to connect to chatbot service');
        }

        $body = wp_remote_retrieve_body($response);
        wp_send_json_success(json_decode($body));
    }
}

new WordPressFlaskChatbot();