console.log("Connected");

function getStudentDetails() {
	console.log("Getting student details");
	let xhttp = new XMLHttpRequest();

	xhttp.onreadystatechange = function() {
		let readyState = this.readyState;
		let status = this.status
		let xmlResponse = this.responseXML;

		if ( readyState === 4 && status == 200 ) {
			setStudentTable(xmlResponse);
		}
	}

	xhttp.open("GET", "students.xml", true);
	xhttp.send()
}

function getTextContentFromXML(response, label) {
	return response.getElementsByTagName(label)[0].childNodes[0].textContent;	
}

function setStudentTable(response) {
	console.log("Setting table");
	let tableContent = `
		<tr>
			<th>Name</th>
			<th>Sap Id</th>
			<th>Course</th>
			<th>Semester</th>
		</tr>
	`

	let students = response.getElementsByTagName("STUDENT");
	
	console.log("STUDENTS:", students)

	for (let i=0; i < students.length; i++) {
		let student = students[i]

		/*
		let name = student.childNodes[1].textContent
		let sapId = student.childNodes[3].textContent
		let course = student.childNodes[5].textContent
		let semester = student.childNodes[7].textContent
		*/

		let name =  getTextContentFromXML(student, "name")
		let sapId =  getTextContentFromXML(student, "sapid")
		let course = getTextContentFromXML(student, "course")
		let semester = getTextContentFromXML(student, "semester")
		
		tableContent = tableContent + `
			<tr>
				<td>${name}</td>
				<td>${sapId}</td>
				<td>${course}</td>
				<td>${semester}</td>
			</tr>
		`
	}

	document.getElementById("student-details").innerHTML = tableContent;
}
