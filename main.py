#

var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('loves contributing to ScoreLab.');
}).listen(8080); 
