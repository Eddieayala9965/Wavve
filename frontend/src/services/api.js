import axios from "axios";
import Cookies from "js-cookie";

const BASE_URL = "http://127.0.0.1:8000";

// Axios instance
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Attach JWT token to requests
api.interceptors.request.use(
  (config) => {
    const token = Cookies.get("authToken"); // Get token from cookies
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

/**
 * User API Calls
 */
export const registerUser = async (userData) => {
  try {
    const response = await api.post("/users/register", userData); // Updated endpoint
    return response.data;
  } catch (error) {
    console.error("Register Error:", error.response?.data || error.message);
    throw error;
  }
};

export const loginUser = async (email, password) => {
  try {
    const response = await api.post("/auth/login", { email, password });
    return response.data;
  } catch (error) {
    console.error("Login Error:", error.response?.data || error.message);
    throw error;
  }
};

/**
 * Chat API Calls
 */
export const createChat = async (chatData) => {
  try {
    const response = await api.post("/chats/", {
      user1_id: chatData.user1_id, // Current user ID
      user2_id: chatData.user2_id, // Recipient user ID
    });
    return response.data;
  } catch (error) {
    console.error("Create Chat Error:", error.response?.data || error.message);
    throw error;
  }
};

export const fetchChatById = async (chatId) => {
  try {
    const response = await api.get(`/chats/${chatId}`);
    return response.data;
  } catch (error) {
    console.error("Fetch Chat Error:", error.response?.data || error.message);
    throw error;
  }
};

export const fetchChatsForUser = async (userId) => {
  try {
    const response = await api.get(`/chats/user/${userId}`);
    return response.data;
  } catch (error) {
    console.error("Fetch Chats Error:", error.response?.data || error.message);
    throw error;
  }
};

/**
 * Message API Calls
 */
export const createMessage = async (messageData) => {
  try {
    const response = await api.post("/message/", messageData);
    return response.data;
  } catch (error) {
    console.error(
      "Create Message Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export const fetchMessageById = async (messageId) => {
  try {
    const response = await api.get(`/message/${messageId}`);
    return response.data;
  } catch (error) {
    console.error(
      "Fetch Message Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

/**
 * Attachment API Calls
 */
export const createAttachment = async (attachmentData) => {
  try {
    const response = await api.post("/attachment/", attachmentData);
    return response.data;
  } catch (error) {
    console.error(
      "Create Attachment Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export const fetchAttachment = async (attachmentId) => {
  try {
    const response = await api.get(`/attachment/${attachmentId}`);
    return response.data;
  } catch (error) {
    console.error(
      "Fetch Attachment Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

/**
 * Read Receipts API Calls
 */
export const createReadReceipt = async (receiptData) => {
  try {
    const response = await api.post("/read_receipt/", receiptData);
    return response.data;
  } catch (error) {
    console.error(
      "Create Read Receipt Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export const fetchReadReceiptsForMessage = async (messageId) => {
  try {
    const response = await api.get(`/read_receipt/message/${messageId}`);
    return response.data;
  } catch (error) {
    console.error(
      "Fetch Read Receipts Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

/**
 * Typing Status API Calls
 */
export const setTypingStatus = async (statusData) => {
  try {
    const response = await api.post("/typing_status/", statusData);
    return response.data;
  } catch (error) {
    console.error(
      "Set Typing Status Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export const fetchTypingStatus = async (userId) => {
  try {
    const response = await api.get(`/typing_status/${userId}`);
    return response.data;
  } catch (error) {
    console.error(
      "Fetch Typing Status Error:",
      error.response?.data || error.message
    );
    throw error;
  }
};

export default api;
