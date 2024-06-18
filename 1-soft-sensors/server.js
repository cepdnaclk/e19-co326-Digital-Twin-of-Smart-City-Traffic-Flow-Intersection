const http = require('http');
const port = process.argv[2] || 8000;

// Create an HTTP server
const server = http.createServer((req, res) => {
  // Print request details to the console
  //console.log(`Incoming request: ${req.method} ${req.url}`);
  //console.log('Headers:', req.headers);

  // Collect request body data
  let body = '';
  req.on('data', chunk => {
    body += chunk.toString();
  });

  req.on('end', () => {
    console.log('Body:', body);

    // Send a response back to the client
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Request received\n');
  });
});

// Start the server on the specified port
server.listen(port, () => {
  console.log(`Server is listening on http://localhost:${port}/producer`);
});
