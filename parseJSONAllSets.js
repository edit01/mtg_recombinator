

var fs = require('fs');
var obj = JSON.parse(fs.readFileSync('AllSets.json', 'utf8')); 

/*
for(key in obj){
	
	console.log(key);
}
*/

console.log(Object.keys(obj));
console.log(Object.keys(obj).length);

var i = 0;
Object.keys(obj).forEach(function(key){
	i += 1;
	console.log(i + "\t" + obj[key].code + "\t" + obj[key].name);
});

console.log(obj["LEA"].name);
console.log(obj["KTK"].name);

//console.log(obj.KTK);
