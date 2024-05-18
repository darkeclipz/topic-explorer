---
title: Web Sockets
---

[Back to index](index.html)

---
# Networking
## Web Sockets

WebSockets are a protocol that provides full-duplex communication channels over a single TCP connection. They enable the server to send real-time updates to clients and facilitate two-way communication between a client (typically a web browser) and a server, which is different from the request-response model used in traditional HTTP connections. 

### Key Features:
1. **Full-Duplex Communication**: Both the client and the server can send messages to each other independently. This is unlike HTTP, where communication is typically initiated by the client in the form of requests, and the server responds to these requests.

2. **Single Connection**: WebSockets maintain a single connection that remains open for the duration of the communication session, significantly reducing overhead compared to repeatedly opening and closing HTTP connections.

3. **Real-Time Data Transfer**: WebSockets are ideal for applications that require real-time data updates, such as chat applications, live sports scores, or stock market updates.

### How WebSockets Work:
1. **Handshake**: The communication starts with an HTTP request known as the WebSocket handshake. During this handshake, the client requests an upgrade to the WebSocket protocol.
   
2. **Upgrade to WebSocket**: If the server supports WebSockets, it agrees to the upgrade by responding with an HTTP 101 status code, switching protocols from HTTP to WebSockets.

3. **Persistent Connection**: After the handshake, a persistent connection is established. The client and server can now exchange messages independently of each other without the need to re-establish connections.

4. **Data Frames**: Communication occurs through data frames that can be sent by either the client or the server. WebSockets support text frames and binary frames, providing flexibility in the type of data that can be transmitted.

### Example Use Cases:
- **Real-Time Applications**: Chat apps, online gaming, and collaborative tools.
- **Live Updates**: News feeds, live sports scores, stock tickers.
- **Interactive Services**: Customer support platforms, online auctions.

### Advantages:
- **Low Latency**: Because the connection remains open, WebSockets can send data as soon as it is available, reducing latency.
- **Efficient Resource Usage**: Unlike HTTP polling, which regularly polls the server for updates, WebSockets maintain an open line, leading to less CPU and memory usage on both the client and server sides.
- **Scalability**: Applications can scale more effectively, as the overhead associated with establishing and tearing down multiple HTTP connections is avoided.

### Example Code:
Here’s a simple example of how a WebSocket connection might be established and used in JavaScript on the client side:

```javascript
// Create a new WebSocket connection to the server
let socket = new WebSocket("ws://example.com/socket");

// When the connection is established
socket.onopen = function(event) {
    console.log("WebSocket is open now.");
    // Send a message to the server
    socket.send("Hello Server!");
};

// When a message is received from the server
socket.onmessage = function(event) {
    console.log("Message from server: ", event.data);
};

// When the connection is closed
socket.onclose = function(event) {
    console.log("WebSocket is closed now.");
};

// Handle any errors
socket.onerror = function(error) {
    console.log("WebSocket error: ", error);
};
```

### Server-Side (Node.js Example Using ws library):
```javascript
const WebSocket = require('ws');
const server = new WebSocket.Server({ port: 8080 });

server.on('connection', socket => {
    console.log('New client connected');
    
    // When a message is received from a client
    socket.on('message', message => {
        console.log('Received:', message);
        // Send a message to the client
        socket.send('Hello Client!');
    });

    // When the client disconnects
    socket.on('close', () => {
        console.log('Client disconnected');
    });
});
```

WebSockets provide a powerful means to facilitate interactive and real-time communication between clients and servers, enhancing the user experience for dynamic applications.

---
[Back to index](index.html)
