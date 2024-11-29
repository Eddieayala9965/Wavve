import React, { useState } from "react";

const Attachments = ({ onUpload }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = () => {
    if (file) {
      onUpload(file);
      setFile(null);
    }
  };

  return (
    <div className="attachments flex items-center p-3">
      <input
        type="file"
        onChange={handleFileChange}
        className="flex-grow p-2 border border-gray-300 rounded-lg"
      />
      <button
        onClick={handleUpload}
        className="ml-3 bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600"
      >
        Upload
      </button>
    </div>
  );
};

export default Attachments;
