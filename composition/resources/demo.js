var http = require('http');
var fs = require('fs');
var port = {{ ctx.node.properties['listening_port'] }}
fs.writeFile("/var/run/nodejs/nodejs.pid", process.pid, (err) => {
  console.log(err);
});
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World');
}).listen(port);
console.log('Server running on port' + port);
