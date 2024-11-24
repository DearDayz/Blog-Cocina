console.log("oallalalala")
var counter = 0;

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + "chatbot"
    + '/'
);

chatSocket.onopen = function(e) {
//Usar para cargar el contexto
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if (data.type === "chatbot"){
        if (data.message === "Starting"){
            counter += 1
            message_div = document.createElement("div");
            message_div.className = "chat-message";
            message_content = document.createElement("div");
            message_content.className = "chat-message-content";
            message_div.id = `${counter}`
            message_div.appendChild(message_content)
            chat_log = document.getElementById("chat-box");
            chat_log.appendChild(message_div)
        }
        else if (data.message === "Finished"){
            // Se usará para evitar que el usuario envíe mensajes solo después que la IA termine el suyo
        }
        else {
            message_div = document.getElementById(`${counter}`)
            message_div.textContent += data.message
        }
    }
    else {
        message_div = document.createElement("div");
        message_div.className = "chat-message";
        message_content = document.createElement("div");
        message_content.className = "chat-message-content";
        chat_log = document.getElementById("chat-box");
        message_content.innerHTML = `<p>${data.message}</p>`
        message_div.appendChild(message_content)
        chat_log.appendChild(message_div)
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-input').focus();
document.querySelector('#chat-input').onkeyup = function(e) {
    if (e.key === 'Enter') {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};
