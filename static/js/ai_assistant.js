// my_website_project/static/js/ai_assistant.js

document.addEventListener('DOMContentLoaded', () => {
    // Get references to DOM elements
    const toggleButton = document.getElementById('ai-assistant-toggle');
    const chatWindow = document.getElementById('ai-assistant-window');
    const closeButton = document.getElementById('ai-assistant-close');
    const messageInput = document.getElementById('ai-assistant-input');
    const sendButton = document.getElementById('ai-assistant-send');
    const messagesContainer = document.getElementById('ai-assistant-messages');

    // Toggle chat window visibility
    toggleButton.addEventListener('click', () => {
        chatWindow.classList.toggle('hidden'); // Toggles display: none / block
        chatWindow.classList.toggle('show');   // Toggles animation classes
        if (!chatWindow.classList.contains('hidden')) {
            messagesContainer.scrollTop = messagesContainer.scrollHeight; // Scroll to bottom when opening
            messageInput.focus(); // Focus input for immediate typing
        }
    });

    // Close chat window
    closeButton.addEventListener('click', () => {
        chatWindow.classList.add('hidden');
        chatWindow.classList.remove('show');
    });

    /**
     * Adds a user message to the chat display with a user avatar.
     * @param {string} message - The text of the user's message.
     */
    function addUserMessage(message) {
        const messageDiv = document.createElement('div');
        // Tailwind classes for aligning message to the right and adding space for avatar
        messageDiv.className = 'flex items-start space-x-2 mb-3 justify-end';
        messageDiv.innerHTML = `
            <div class="user-message bg-blue-500 text-white p-2 rounded-lg max-w-[calc(100%-40px)]">
                ${message}
            </div>
            <div class="w-6 h-6 rounded-full bg-gray-400 flex-shrink-0 flex items-center justify-center">
                <i class="fas fa-user text-xs text-white"></i> {# User avatar icon #}
            </div>
        `;
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight; // Keep scrolled to bottom
    }

    /**
     * Adds an AI message to the chat display with the cartoon hero avatar.
     * @param {string} message - The text of the AI's message.
     * @param {boolean} isError - True if this is an error message, applies different styling.
     */
    function addAIMessage(message, isError = false) {
        const messageDiv = document.createElement('div');
        // Tailwind classes for aligning message to the left and adding space for avatar
        messageDiv.className = 'flex items-start space-x-2 mb-3';
        
        // Conditional styling based on whether it's an error message
        const messageClass = isError 
            ? 'ai-message bg-red-100 text-red-700 p-2 rounded-lg max-w-[calc(100%-40px)]'
            : 'ai-message bg-blue-100 text-blue-900 p-2 rounded-lg max-w-[calc(100%-40px)]';
            
        messageDiv.innerHTML = `
            <div class="w-6 h-6 rounded-full bg-cover bg-center flex-shrink-0"
                 style="background-image: url('/static/images/cartoon_hero.png');">
            </div>
            <div class="${messageClass}">
                ${message}
            </div>
        `;
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight; // Keep scrolled to bottom
    }

    /**
     * Handles sending a message to the Django backend AI assistant.
     */
    async function sendMessage() {
        const userMessage = messageInput.value.trim();
        if (userMessage === '') return; // Don't send empty messages

        addUserMessage(userMessage); // Display user's message immediately
        messageInput.value = '';     // Clear input field

        // Determine current page to provide context to the AI
        const pathSegments = window.location.pathname.split('/').filter(Boolean); // Get non-empty path segments
        let currentPage = 'About Me'; // Default page for context
        if (pathSegments.length > 0) {
            currentPage = pathSegments[0]; // Use the first segment as the page name
            if (pathSegments[0] === 'blog' && pathSegments.length > 1) {
                // If it's a blog post detail page, provide more specific context
                currentPage = 'blog post detail page';
            }
        }
        
        // Add a loading indicator while waiting for the AI response
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'ai-message bg-gray-100 text-gray-700 p-2 rounded-lg mb-2 self-start animate-pulse';
        loadingDiv.textContent = 'Hero Assistant is thinking...';
        messagesContainer.appendChild(loadingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        try {
            // Send message and current page info to Django backend
            const response = await fetch('/ai-assistant/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // CSRF token is not needed if @csrf_exempt is used on the view,
                    // but it's good practice for production:
                    // 'X-CSRFToken': getCookie('csrftoken'), 
                },
                body: JSON.stringify({
                    message: userMessage,
                    currentPage: currentPage
                }),
            });

            // Remove the loading indicator once response is received (or error occurs)
            messagesContainer.removeChild(loadingDiv);

            if (!response.ok) {
                // Attempt to read the error message from the server's JSON response
                const errorData = await response.json();
                throw new Error(`Server error: ${errorData.error || response.statusText}`);
            }

            const data = await response.json();
            const aiResponse = data.response;

            addAIMessage(aiResponse); // Display AI's response

        } catch (error) {
            console.error('Error communicating with AI assistant:', error);
            // Ensure loading indicator is removed even on error
            if (messagesContainer.contains(loadingDiv)) {
                messagesContainer.removeChild(loadingDiv);
            }
            // Display a user-friendly error message in the chat
            addAIMessage(`Sorry, I am having trouble connecting right now. Error: ${error.message}`, true);
        }
    }

    // Helper function to get CSRF token from cookies (uncomment and use if @csrf_exempt is removed)
    // function getCookie(name) {
    //     let cookieValue = null;
    //     if (document.cookie && document.cookie !== '') {
    //         const cookies = document.cookie.split(';');
    //         for (let i = 0; i < cookies.length; i++) {
    //             const cookie = cookies[i].trim();
    //             if (cookie.startsWith(name + '=')) {
    //                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    //                 break;
    //             }
    //         }
    //     }
    //     return cookieValue;
    // }

    // Event listeners for sending messages (click button or press Enter in input)
    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) { // Prevents sending if Shift+Enter (allows multiline input)
            e.preventDefault(); // Prevent default newline behavior for Enter key
            sendMessage();
        }
    });

    // Close chat when clicking outside the chat window or toggle button
    document.addEventListener('click', function(e) {
        if (!chatWindow.contains(e.target) && !toggleButton.contains(e.target)) {
            // Check if the click event target is outside both the chat window and the toggle button
            chatWindow.classList.add('hidden');
            chatWindow.classList.remove('show');
        }
    });
});
