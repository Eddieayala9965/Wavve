import { useEffect, useRef, useState } from "react";

const useWebSocket = (url, onMessage) => {
  const [isConnected, setIsConnected] = useState(false);
  const ws = useRef(null);

  useEffect(() => {
    ws.current = new WebSocket(url);

    ws.current.onopen = () => {
      console.log("WebSocket connected");
      setIsConnected(true);
    };

    ws.current.onmessage = (event) => {
      const messageData = JSON.parse(event.data);
      if (onMessage) {
        onMessage(messageData);
      }
    };

    ws.current.onclose = () => {
      console.log("WebSocket disconnected");
      setIsConnected(false);
    };

    ws.current.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    return () => {
      ws.current.close();
    };
  }, [url, onMessage]);

  const sendMessage = (data) => {
    if (ws.current && isConnected) {
      ws.current.send(JSON.stringify(data));
    }
  };

  return { isConnected, sendMessage };
};

export default useWebSocket;
