import { create } from "zustand";
import { createChat, fetchChatsForUser } from "@/services/api";

export const useChatStore = create((set) => ({
  chats: [],
  currentChat: null,

  fetchChats: async () => {
    try {
      const userId = localStorage.getItem("userId");
      const data = await fetchChatsForUser(userId);
      set({ chats: data });
    } catch (error) {
      console.error("Error fetching chats:", error);
    }
  },

  createNewChat: async (chatData) => {
    try {
      const newChat = await createChat(chatData);
      set((state) => ({ chats: [...state.chats, newChat] }));
    } catch (error) {
      console.error("Error creating new chat:", error);
      throw error;
    }
  },

  setCurrentChat: (chat) => set({ currentChat: chat }),
}));
