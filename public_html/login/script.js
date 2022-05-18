var interval;
const intervalDuration = 1000;

async function handleSubmit(form) {
	console.log("Form Sumbit");
	const username = form.username.value;
	const password = form.password.value;

	console.log({username, password});

	const pattern = /[a-zA-Z]{4}[\d]{2}/;

	const isUsernameMatch = pattern.test(username);
	
	if (isUsernameMatch) {
		const date = new Date();
		
		const content = `
			Welcome ${username},
			You have been logged in at ${date}
			
			<br />
			<br />
			<br />
			<input type="button" onclick="handleStopInterval()" value="Stop" />

			<br />
			<br />
			<input type="button" onclick="handleResumeInterval()" value="Resume" />


		`;
		
		
		//document.write(content);

		const contentLength = content.split(" ").length;
		let currentIndex = 0;	

		while(currentIndex < contentLength) {
			//await new Promise(function () {
				setTimeout(function() { console.log({currentIndex}); }, 2000);
			//})
			currentIndex++;
		}

		addContentToDocument(content, currentIndex);
		
		interval = setInterval ( changeBackgroundColor, intervalDuration);
	} else {
		alert("Invalid username and password combination");
	}

}

function addContentToDocument(content, i) {

	//for(let i=0; i < contentLength; i++) {
		const word = content[i];
	//	setTimeout(function () {
			document.writeln(word);
	//	}, 1000 )		
	//}

}

function getRandomColorValue() {
	return Math.floor( Math.random() * 255 );
}

function handleStopInterval() {
	clearInterval(interval);
}

function handleResumeInterval() {
	interval = setInterval ( changeBackgroundColor, intervalDuration);
}

function changeBackgroundColor() {

	const rRandom = getRandomColorValue();
	const gRandom = getRandomColorValue();
	const bRandom = getRandomColorValue();

	//document.body.style.background = "lightblue"; 
	//document.body.style.background = "rgb(210,210,210)";
	
	document.body.style.background = `rgb(${rRandom},${gRandom},${bRandom})`;
}
