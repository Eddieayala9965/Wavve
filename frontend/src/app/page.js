"use client";

import Link from "next/link";

export default function Home() {
  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 max-w-lg w-full">
        <h1 className="text-3xl font-bold text-center mb-6">
          Welcome to Wavve
        </h1>
        <p className="text-gray-700 text-center mb-8">
          A secure messaging app designed for real-time communication.
        </p>
        <div className="flex justify-center space-x-4">
          <Link
            href="/login"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Login
          </Link>
          <Link
            href="/register"
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Register
          </Link>
        </div>
      </div>
    </div>
  );
}
