const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
  let fp = path.join(__dirname, req.url === '/' ? 'index.html' : req.url);
  fs.readFile(fp, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end('Not found');
    } else {
      const ext = path.extname(fp).slice(1);
      const mimes = { html: 'text/html', css: 'text/css', js: 'application/javascript' };
      res.writeHead(200, { 'Content-Type': mimes[ext] || 'text/plain' });
      res.end(data);
    }
  });
});

server.listen(3456, () => {
  console.log('Server running at http://localhost:3456');
});
