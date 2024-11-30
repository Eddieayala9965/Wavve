"use client";

import { useEffect, useState } from "react";
import { useChatStore } from "@/store/useChatStore";
import { fetchMessages, createMessage } from "@/services/api";
import { useParams, useRouter } from "next/navigation";

export default function ChatDetails() {
  const router = useRouter();
  const { chatid } = useParams();
  const { currentChat, fetchChatDetails } = useChatStore();

  const [messages, setMessages] = useState([]); // Store messages for chat
  const [newMessage, setNewMessage] = useState(""); // Input for new message
  const [error, setError] = useState("");

  useEffect(() => {
    if (chatid) {
      fetchChatDetails(chatid); // Fetch chat details by ID

      // Fetch messages for the chat
      const fetchChatMessages = async () => {
        try {
          const response = await fetchMessages(chatid);
          setMessages(response);
        } catch (err) {
          setError("Failed to load messages.");
          console.error(err);
        }
      };

      fetchChatMessages();
    }
  }, [chatid, fetchChatDetails]);

  // Handle sending a new message
  const handleSendMessage = async () => {
    if (!newMessage.trim()) return;

    try {
      const messageData = {
        chat_id: chatid,
        sender: localStorage.getItem("username"), // Retrieve username from localStorage
        content: newMessage,
      };

      const response = await createMessage(messageData); // Send new message
      setMessages((prev) => [...prev, response]); // Append to message list
      setNewMessage(""); // Clear input
    } catch (err) {
      setError("Failed to send message.");
      console.error(err);
    }
  };

  if (!currentChat) {
    return (
      <div className="flex flex-col items-center justify-center p-4">
        <p className="text-gray-500">No chat selected or found.</p>
        <button
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
          onClick={() => router.push("/chats")}
        >
          Back to Chats
        </button>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-screen p-4">
      {/* Chat Header */}
      <div className="p-4 bg-gray-200">
        <h2 className="text-xl font-bold">{currentChat.name}</h2>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 bg-gray-100">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`p-2 rounded mb-2 ${
              message.sender === localStorage.getItem("username")
                ? "bg-blue-500 text-white self-end"
                : "bg-gray-300"
            }`}
          >
            <strong>{message.sender}: </strong>
            {message.content}
          </div>
        ))}
      </div>

      {/* Message Input */}
      <div className="p-4 bg-gray-200 flex items-center">
        <input
          type="text"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type your message..."
          className="flex-1 p-2 border rounded"
        />
        <button
          onClick={handleSendMessage}
          className="ml-2 p-2 bg-blue-500 text-white rounded"
        >
          Send
        </button>
      </div>
    </div>
  );
}
