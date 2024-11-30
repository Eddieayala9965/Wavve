"use client";

import { useState } from "react";
import { createChat } from "@/services/api";

export default function CreateChatForm() {
  const [recipientUsername, setRecipientUsername] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      const chatData = {
        user1_username: localStorage.getItem("username"), // Get logged-in user's username
        user2_username: recipientUsername, // Input for the recipient's username
        name: `Chat between ${localStorage.getItem(
          "username"
        )} and ${recipientUsername}`,
      };
      await createChat(chatData);
      setSuccess("Chat created successfully!");
      setRecipientUsername("");
    } catch (err) {
      setError(
        err.response?.data?.detail || "Failed to create chat. Please try again."
      );
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
      <input
        type="text"
        placeholder="Recipient's Username"
        value={recipientUsername}
        onChange={(e) => setRecipientUsername(e.target.value)}
        className="p-2 border rounded"
        required
      />
      <button type="submit" className="p-2 bg-blue-500 text-white rounded">
        Create Chat
      </button>
      {error && <p className="text-red-500">{error}</p>}
      {success && <p className="text-green-500">{success}</p>}
    </form>
  );
}
