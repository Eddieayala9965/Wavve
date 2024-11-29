"use client";

import { useState } from "react";
import { createChat } from "@/services/api";

export default function CreateChatForm() {
  const [recipientId, setRecipientId] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    try {
      const currentUserId = "replace-this-with-current-user-id";
      await createChat({ user1_id: currentUserId, user2_id: recipientId });
      setSuccess("Chat created successfully!");
      setRecipientId("");
    } catch (err) {
      console.error("Create Chat Error: ", err);
      setError("Failed to create chat. Please try again.");
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col space-y-4 p-4 bg-gray-100 rounded shadow"
    >
      <label htmlFor="recipientId" className="text-lg font-semibold">
        Start a New Chat
      </label>
      <input
        id="recipientId"
        type="text"
        placeholder="Enter recipient user ID"
        value={recipientId}
        onChange={(e) => setRecipientId(e.target.value)}
        className="p-2 border rounded"
        required
      />
      <button
        type="submit"
        className="p-2 bg-blue-500 text-white rounded hover:bg-blue-700 transition"
      >
        Start Chat
      </button>
      {error && <p className="text-red-500">{error}</p>}
      {success && <p className="text-green-500">{success}</p>}
    </form>
  );
}
