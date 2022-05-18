function getStudentDetails() {
	console.log("Get student details", students);

	let tableContent = `
		<tr>
			<th>Name</th>
			<th>Sap Id</th>
			<th>Course</th>
			<th>Semester</th>

		</tr>
	`;

	for(let i=0; i < students.length; i++) {
		let student = students[i];

		tableContent = tableContent + `
			<tr>
				<td>${student.name}</td>
				<td>${student.sapId}</td>
				<td>${student.course}</td>
				<td>${student.sem}</td>
			</tr>

		`;
		
	}

	document.getElementById("student-details").innerHTML = tableContent;
}
