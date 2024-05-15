// document.addEventListener('DOMContentLoaded', function() {
//     const input = document.querySelector('.input input');
//     const messagesContainer = document.querySelector('.messages');

//     // Add event listener for keypress event
//     input.addEventListener('keypress', function(event) {
//         // Check if the key pressed is Enter (keycode 13)
//         if (event.keyCode === 13) {
//             // Prevent the default behavior of form submission (if any)
//             event.preventDefault();

//             // Create a new message bubble
//             const newMessage = document.createElement('div');
//             newMessage.classList.add('message', 'sent');
//             const bubble = document.createElement('div');
//             bubble.classList.add('bubble');
//             const text = document.createElement('div');
//             text.classList.add('text');
//             text.textContent = input.value;
//             bubble.appendChild(text);
//             newMessage.appendChild(bubble);

//             // Append the new message bubble to the messages container
//             messagesContainer.appendChild(newMessage);

//             // Clear the input field
//             input.value = '';

//             // Scroll to the bottom of the messages container
//             messagesContainer.scrollTop = messagesContainer.scrollHeight;
//         }
//     });
// });

var messages = document.getElementById("chatcontainer");

function scrollToBottom() {
    chatcontainer.scrollTop = chatcontainer.scrollHeight;
}
function postMessage() {
    scrollToBottom();
}