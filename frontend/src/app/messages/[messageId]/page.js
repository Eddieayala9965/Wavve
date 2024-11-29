"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useMessageStore } from "@/store/messageStore";

export default function MessageDetails({ params }) {
  const { messageid } = params;
  const { fetchMessageById, updateMessage, deleteMessage, currentMessage } =
    useMessageStore(); // Zustand store
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  const [editedContent, setEditedContent] = useState("");
  const router = useRouter();

  useEffect(() => {
    const fetchData = async () => {
      await fetchMessageById(messageid);
      setLoading(false);
    };

    if (!messageid) {
      router.push("/messages"); // Redirect if no message ID
    } else {
      fetchData();
    }
  }, [messageid, fetchMessageById, router]);

  const handleEdit = async () => {
    await updateMessage(messageid, { content: editedContent });
    setIsEditing(false);
  };

  const handleDelete = async () => {
    await deleteMessage(messageid);
    router.push("/messages"); // Redirect after delete
  };

  if (loading) return <div>Loading message details...</div>;

  if (!currentMessage) return <div>Message not found!</div>;

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold">Message Details</h2>
      {isEditing ? (
        <div>
          <textarea
            className="w-full p-2 border rounded"
            value={editedContent}
            onChange={(e) => setEditedContent(e.target.value)}
          />
          <button
            onClick={handleEdit}
            className="bg-blue-500 text-white px-4 py-2 rounded mt-2"
          >
            Save
          </button>
          <button
            onClick={() => setIsEditing(false)}
            className="bg-gray-500 text-white px-4 py-2 rounded mt-2 ml-2"
          >
            Cancel
          </button>
        </div>
      ) : (
        <div>
          <p>
            <strong>Content:</strong> {currentMessage.content}
          </p>
          <p>
            <strong>Sender:</strong> {currentMessage.sender}
          </p>
          <p>
            <strong>Timestamp:</strong>{" "}
            {new Date(currentMessage.timestamp).toLocaleString()}
          </p>
          {currentMessage.attachments?.length > 0 && (
            <div>
              <strong>Attachments:</strong>
              <ul>
                {currentMessage.attachments.map((attachment) => (
                  <li key={attachment.id}>{attachment.name}</li>
                ))}
              </ul>
            </div>
          )}
          <button
            onClick={() => {
              setEditedContent(currentMessage.content);
              setIsEditing(true);
            }}
            className="bg-green-500 text-white px-4 py-2 rounded mt-2"
          >
            Edit
          </button>
          <button
            onClick={handleDelete}
            className="bg-red-500 text-white px-4 py-2 rounded mt-2 ml-2"
          >
            Delete
          </button>
        </div>
      )}
    </div>
  );
}
