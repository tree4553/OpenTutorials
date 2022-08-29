var fs = require('fs');

/*
console.log('A');
var result = fs.readFileSync('./sample.txt', 'utf8');
console.log(result);
console.log('C');
// A B C
*/

console.log('A');
fs.readFile('./sample.txt', 'utf8', function(err, result) {
    console.log(result);
});
console.log('C');
// A C B