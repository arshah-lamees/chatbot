const chat = document.getElementById('chat');
const form = document.getElementById('input-area');
const messageInput = document.getElementById('message');
const sendBtn = document.getElementById('send');
const loading = document.getElementById('loading');

function addMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'msg';
    const bubble = document.createElement('span');
    bubble.className = 'bubble ' + (sender === 'user' ? 'user-bubble' : 'bot-bubble');
    bubble.innerText = text;
    msgDiv.appendChild(bubble);
    chat.appendChild(msgDiv);
    chat.scrollTop = chat.scrollHeight;
}

form.onsubmit = async (e) => {
    e.preventDefault();
    const userMsg = messageInput.value.trim();
    if (!userMsg) return;
    addMessage(userMsg, 'user');
    messageInput.value = '';
    sendBtn.disabled = true;
    loading.style.display = 'inline-block';
    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: userMsg })
        });
        const data = await res.json();
        addMessage(data.response, 'bot');
    } catch (err) {
        addMessage('[Error contacting server]', 'bot');
    }
    sendBtn.disabled = false;
    loading.style.display = 'none';
}; 