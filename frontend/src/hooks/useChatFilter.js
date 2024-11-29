import { useState } from "react";

const useChatFilter = (chats) => {
  const [filter, setFilter] = useState("");

  const filteredChats = chats.filter((chat) =>
    chat.name.toLowerCase().includes(filter.toLowerCase())
  );

  return { filter, setFilter, filteredChats };
};

export default useChatFilter;
