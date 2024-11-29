"use client";

import { useEffect } from "react";
import { useMessageStore } from "@/store/messageStore";
import { useParams, useRouter } from "next/navigation";

export default function Messages() {
  const router = useRouter();
  const { chatid } = useParams(); // Assumes `chatid` is passed via the URL
  const { fetchMessagesByChat, messages, currentChat } = useMessageStore();

  useEffect(() => {
    if (chatid) {
      fetchMessagesByChat(chatid);
    }
  }, [chatid, fetchMessagesByChat]);

  if (!chatid) {
    return <div>Please select a chat to view messages.</div>;
  }

  return (
    <div className="flex flex-col p-4">
      <h2 className="text-xl font-bold mb-4">
        {currentChat?.name || "Chat Messages"}
      </h2>
      <div className="space-y-4">
        {messages.map((message) => (
          <div
            key={message.id}
            className="p-4 border rounded hover:shadow cursor-pointer"
            onClick={() => router.push(`/messages/${message.id}`)} // Navigate to `[messageid]/page.js`
          >
            <p className="text-gray-800">{message.content}</p>
            <p className="text-sm text-gray-500">
              Sent by {message.sender} on{" "}
              {new Date(message.timestamp).toLocaleString()}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
