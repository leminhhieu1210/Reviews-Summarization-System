const $ = document.querySelector.bind(document);

$('.clear').addEventListener('click', (e) => {
	$("#textOrg").value = "";
	$('#textPredict').value = ""
})

$('#ex1').addEventListener('click', (e) => {
	$("#textOrg").value = "I started drinking the Thai Nguyen tea since I was twenty years old to help curb cravings. Since I liked it so well, I drink them all the time. It helps keep me happy all day, no matter how long.";
	$('#textPredict').value = ""
})

$('#ex2').addEventListener('click', (e) => {
	$("#textOrg").value = "My daughter loves these yogurt melts. Banana and mango are two of their favorite flavors. The yogurt Vinamilk melts themselves are a smaller size than the Moc Chau melts, which is nice for younger babies. These are tasty and organic. We've had a lot of success with all of the Vinamilk products for babies we've tried. Highly recommend.";
	$('#textPredict').value = ""
})

$('#ex3').addEventListener('click', (e) => {
	$("#textOrg").value = "My family has a dog. I call my dog is Cau Vang. Great dog food is shipped to my door monthly. My pet enjoyed the food from day one. Great amount of meat, fruit, and veggies!";
	$('#textPredict').value = ""
})


window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
// recognition.lang = "en-US";
recognition.lang = "vi-VN";
const content = document.querySelector("#textOrg");
recognition.interimResults = true; 

recognition.continuous = false; 

$(".speech").onclick = function (e) {
  e.preventDefault();
  content.value = "";
  recognition.start();
};


recognition.addEventListener("result", (e) => {
	console.log(e)
  let tran = e.results[0][0].transcript;
  content.value = tran;
});

recognition.addEventListener("end", (e) => {
  recognition.stop();
});
