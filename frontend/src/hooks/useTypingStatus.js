import { useEffect, useState } from "react";

const useTypingStatus = (debounceTime = 2000) => {
  const [isTyping, setIsTyping] = useState(false);
  const [typingTimeout, setTypingTimeout] = useState(null);

  const startTyping = () => {
    setIsTyping(true);
    if (typingTimeout) {
      clearTimeout(typingTimeout);
    }
    setTypingTimeout(setTimeout(stopTyping, debounceTime));
  };

  const stopTyping = () => {
    setIsTyping(false);
    if (typingTimeout) {
      clearTimeout(typingTimeout);
    }
  };

  useEffect(() => {
    return () => {
      if (typingTimeout) {
        clearTimeout(typingTimeout);
      }
    };
  }, [typingTimeout]);

  return { isTyping, startTyping };
};

export default useTypingStatus;
