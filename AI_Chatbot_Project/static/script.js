let count = 0;
function sendMessage(){
let input=document.getElementById("user-input");
let message=input.value.trim();
if(message==="")return;
let chatBox=document.getElementById("chat-box");
chatBox.innerHTML+=`<div class="user-message">${message}</div>`;
chatBox.innerHTML+=`<div class="bot-message typing">Bot is typing...</div>`;
chatBox.scrollTop=chatBox.scrollHeight;
fetch("/get_response",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:message})})
.then(response=>response.json())
.then(data=>{
let typingMessages=document.querySelectorAll(".typing");
let lastTyping=typingMessages[typingMessages.length-1];
setTimeout(()=>{
lastTyping.classList.remove("typing");
lastTyping.innerHTML=data.response;
saveChat();
},1000);
});
count++;
document.getElementById("count").innerText=count;
input.value="";
}
function quickAsk(topic){
document.getElementById("user-input").value=topic;
sendMessage();
}
document.addEventListener("DOMContentLoaded",function(){
let input=document.getElementById("user-input");
if(input){
input.addEventListener("keypress",function(e){
if(e.key==="Enter"){
sendMessage();
}
});
}
loadChat();
});
function toggleTheme(){
document.body.classList.toggle("light-mode");
localStorage.setItem("theme",document.body.classList.contains("light-mode"));
}
if(localStorage.getItem("theme")==="true"){
document.body.classList.add("light-mode");
}
function startVoice(){
if(!('webkitSpeechRecognition'in window)){
alert("Voice recognition not supported");
return;
}
let recognition=new webkitSpeechRecognition();
recognition.lang="en-US";
recognition.start();
recognition.onresult=function(event){
let speech=event.results[0][0].transcript;
document.getElementById("user-input").value=speech;
sendMessage();
};
}
function exportChat(){
let chatContent=document.getElementById("chat-box").innerText;
let blob=new Blob([chatContent],{type:"text/plain"});
let url=window.URL.createObjectURL(blob);
let a=document.createElement("a");
a.href=url;
a.download="chat_history.txt";
a.click();
window.URL.revokeObjectURL(url);
}
function saveChat(){
localStorage.setItem("chatHistory",document.getElementById("chat-box").innerHTML);
}
function loadChat(){
let history=localStorage.getItem("chatHistory");
if(history){
document.getElementById("chat-box").innerHTML=history;
}
}
function clearChat(){
document.getElementById("chat-box").innerHTML="";
localStorage.removeItem("chatHistory");
count=0;
document.getElementById("count").innerText=count;
}