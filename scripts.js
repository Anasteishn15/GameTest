console.log("ВОТ ЭТОТ SCRIPTS.JS ЗАПУСТИЛСЯ");

const params = new URLSearchParams(window.location.search);
const playerId = params.get("id");

console.log("PLayer: ", playerId);

const socket = new WebSocket("ws://127.0.0.1:8000/ws?id=" + playerId);



socket.onopen = function() {
   
   console.log("WebSocket connected");
}



socket.onerror = function(error) {
   console.log("WEBSOCKET ERROR", error);
};


const helloCount = document.getElementById("count");


socket.onmessage = function(event) {
   helloCount.textContent = "Your hellos: " + event.data;
};



const button = document.getElementById("hi")
button.addEventListener("click", function() {
   socket.send("hi");
});


