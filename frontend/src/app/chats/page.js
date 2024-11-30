"use client";

import { useEffect } from "react";
import { useChatStore } from "@/store/useChatStore";
import CreateChatForm from "@/components/CreateChatForm";
import { useRouter } from "next/navigation";

export default function ChatsPage() {
  const { chats, fetchChats } = useChatStore();
  const router = useRouter();

  useEffect(() => {
    const userId = localStorage.getItem("user_id"); // Ensure `user_id` is retrieved from localStorage
    if (userId) {
      fetchChats(userId); // Fetch chats for the logged-in user
    } else {
      console.error("User ID is not found in local storage.");
    }
  }, [fetchChats]);

  return (
    <div className="flex flex-col p-4">
      <h2 className="text-xl font-bold mb-4">Chats</h2>

      {/* Create Chat Form */}
      <div className="mb-6">
        <CreateChatForm />
      </div>

      {/* List of Chats */}
      <div className="space-y-4">
        {chats.length > 0 ? (
          chats.map((chat) => (
            <div
              key={chat.id}
              onClick={() => router.push(`/chats/${chat.id}`)} // Navigate to chat details
              className="p-4 border rounded hover:shadow cursor-pointer"
            >
              <p className="font-semibold">{chat.name}</p>
            </div>
          ))
        ) : (
          <p className="text-gray-500">No chats found. Start a new one!</p>
        )}
      </div>
    </div>
  );
}
