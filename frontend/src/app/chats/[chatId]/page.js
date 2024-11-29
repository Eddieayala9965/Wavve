"use client";

import { useEffect } from "react";
import { useChatStore } from "@/store/chatStore";
import { useParams, useRouter } from "next/navigation";

export default function ChatDetails() {
  const router = useRouter();
  const { chatid } = useParams();
  const { currentChat, fetchChatDetails } = useChatStore();

  useEffect(() => {
    if (chatid) {
      fetchChatDetails(chatid); // Fetch details for the selected chat
    }
  }, [chatid, fetchChatDetails]);

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
    <div className="flex flex-col p-4">
      <h2 className="text-xl font-bold mb-4">{currentChat.name}</h2>
      <p className="text-gray-600 mb-4">Chat ID: {currentChat.id}</p>
      <p className="text-gray-500">
        Participants: {currentChat.participants.join(", ")}
      </p>
      {/* Add options for editing chat or managing participants */}
    </div>
  );
}
