"use client";

import { useEffect } from "react";
import { useChatStore } from "@/store/useChatStore";
import CreateChatForm from "@/components/CreateChatForm";

export default function Chats() {
  const { chats, fetchChats } = useChatStore();

  useEffect(() => {
    fetchChats(); // Fetch all available chats
  }, [fetchChats]);

  return (
    <div className="flex flex-col p-4">
      <h2 className="text-xl font-bold mb-4">Chats</h2>
      <CreateChatForm /> {/* Add the form here */}
      <div className="space-y-4">
        {chats.map((chat) => (
          <div key={chat.id} className="p-4 border rounded hover:shadow">
            <p className="font-semibold">{chat.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
