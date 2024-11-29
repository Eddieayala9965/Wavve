"use client";

import { useState } from "react";
import { createChat } from "@/services/api";

export default function CreateChatForm() {
  const [user1Username, setUser1Username] = useState("");
  const [user2Username, setUser2Username] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      const chatData = {
        user1_username: user1Username,
        user2_username: user2Username,
        name: `Chat between ${user1Username} and ${user2Username}`,
      };
      await createChat(chatData);
      setSuccess("Chat created successfully!");
      setUser1Username("");
      setUser2Username("");
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
        placeholder="Your Username"
        value={user1Username}
        onChange={(e) => setUser1Username(e.target.value)}
        className="p-2 border rounded"
        required
      />
      <input
        type="text"
        placeholder="Recipient Username"
        value={user2Username}
        onChange={(e) => setUser2Username(e.target.value)}
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
