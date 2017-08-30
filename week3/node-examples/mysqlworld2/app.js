var mysql = require('mysql');

var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: ''
});


connection.query('USE world');

connection.query('SELECT name, district FROM city WHERE CountryCode = "AUS"',function(err, result, fields) {
    if (err) {
        return console.error(err); 
    } else {
    	
	var arrayLength = result.length; 

	for (var i = 0; i <= arrayLength-1; i++) {
	    var line = result[i].name + " (" + result[i].district + ")";
	    console.log(line); 
	}
    }
}); 

connection.end(); 
