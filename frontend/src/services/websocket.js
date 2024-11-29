let socket = null;

export const connectWebSocket = (userId) => {
  socket = new WebSocket(`${process.env.NEXT_PUBLIC_WS_URL}/ws/${userId}`);

  socket.onopen = () => {
    console.log("WebSocket connection established.");
  };

  socket.onclose = () => {
    console.log("WebSocket connection closed.");
  };

  socket.onerror = (error) => {
    console.error("WebSocket error:", error);
  };
};

export const sendWebSocketMessage = (message) => {
  if (socket && socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify(message));
  } else {
    console.error("WebSocket is not connected.");
  }
};

export const disconnectWebSocket = () => {
  if (socket) {
    socket.close();
  }
};

export const onWebSocketMessage = (callback) => {
  if (socket) {
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      callback(data);
    };
  }
};
