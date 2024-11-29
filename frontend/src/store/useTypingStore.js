import { create } from "zustand";

const useTypingStore = create((set) => ({
  typingStatus: {},
  setTypingStatus: (chatId, userId, isTyping) =>
    set((state) => ({
      typingStatus: {
        ...state.typingStatus,
        [chatId]: {
          ...state.typingStatus[chatId],
          [userId]: isTyping,
        },
      },
    })),
}));

export default useTypingStore;
