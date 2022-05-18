const intervalDuration = 1000;


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




function setWebContent(webContent) {
	console.log("Setting content")
	document.write(webContent)
}

function handleLoginSubmit(form) {
	const username = form.username.value;
	const password = form.password.value;

	console.log({username, password})

	if (username == "admin" && password == "admin") {
		const allUsers = getAllUsers();
	
		document.write("")
		for (let i=0; i<allUsers.length; i++) {
			document.writeln(`${i+1})Username: ${allUsers[i].username},`);
			document.writeln(`Content: ${allUsers[i].content}`);
			document.writeln("<br/ >");

		}
		document.writeln(`<br /><button><a href="login.html">Logout</a></button>`)
		return;
	}

	const foundUser = getUserFromUsername(username);

	if (foundUser == undefined) {
		return alert(`User ${username} has not been registered. Please register to continue`);
	} 

	if (foundUser.password != password) {
		return alert("Password invalid");
	}

	const userContent = foundUser.content;

	const webPageContent = `

		<h1>Welcome ${username}!</h1>
		<h3>Your content is ${userContent}</h3>
		<button onclick="handleStopInterval()">Stop</button>
		<button onclick="handleResumeInterval()">Resume</button>
		<button><a href="login.html">Logout</a></button>
		
	`;
	setWebContent(webPageContent);
	changeBackgroundColor();
	handleResumeInterval();
}

function handleRegisterSubmit(form) {
	const username = form.username.value;
	const content = form.content.value;
	const password = form.password.value;
	const confirmPassword = form.confirmPassword.value;

	console.log({username, content, password, confirmPassword});

	if (password !== confirmPassword) {
		return alert("Password and confirm password do not match");
	}
	
	const pattern = /[a-zA-Z]{4}[\d]{2}/;
	const isUsernameMatch = pattern.test(username);

	if (!isUsernameMatch) {
		return alert("Username should begin with 4 alphabets followed by 2 numbers");
	}

	const users = JSON.parse(localStorage.getItem("users"));

	if (!users) {
		console.log("users is null")	
		localStorage.setItem("users", JSON.stringify([]));
	} else {
		console.log("users is not null")
	}

	const user = {username, content, password};
	
	const foundUser = getUserFromUsername(user.username);

	if (foundUser == undefined) {
		addUserToLocalStorage(user);
		alert("Registered Successfully");
	} else {
		alert(`User ${username} already exists`);
	}
}

function getUserFromUsername(userToCheck) {
	const users = JSON.parse(localStorage.getItem("users"));

	function checkUser(user) {
		return user.username === userToCheck;
	}
	const foundUser = users.find(checkUser)
	return foundUser;
}

function getAllUsers() {
	const users = JSON.parse(localStorage.getItem("users"));
	return users;	

}

function displayUsers() {
	console.log("Displaying users")
	const users = JSON.parse(localStorage.getItem("users"));
	
	for (let i=0; i<users.length; i++){
		const user = users[i];
		console.log({user})
	}

}

function addUserToLocalStorage(user) {
	const users = JSON.parse(localStorage.getItem("users"));
	
	users.push(user);

	localStorage.setItem("users", JSON.stringify(users));
}
