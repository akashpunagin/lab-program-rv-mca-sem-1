function getStudentObject(name, sapId, course, sem) {
        return {name, sapId, course, sem};
}

let students = [
	getStudentObject("Raju", "RVCE21MCA01", "MCA", 1),
	getStudentObject("Bheem", "RVCE21MCA02", "MCA", 1),
	getStudentObject("Ramu", "RVCE21MCA05", "MCA", 3),
	getStudentObject("Bhamu", "RVCE21MCA08", "MTech", 4),
	getStudentObject("Jaggu", "RVCE21MCA03", "MBA", 6),

];
