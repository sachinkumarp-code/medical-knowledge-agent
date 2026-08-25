"use client";
import { useState } from "react";

export default function Home() {
  // 1. STATE MANAGEMENT
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  // 2. THE ACTION
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMsg = { role: "user", content: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setIsLoading(true);

    try {
      const res = await fetch("http://13.53.70.238:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userMsg.content }),
      });
      
      const data = await res.json();
      
      setMessages((prev) => [...prev, { role: "assistant", content: data.answer }]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "⚠️ System Error: Unable to reach the AI Inference Engine." },
      ]);
    }
    setIsLoading(false);
  };

  // 3. THE UI
  return (
    <div className="flex flex-col h-screen bg-[#111111] text-[#E0E0E0] font-sans selection:bg-[#00E676] selection:text-black">
      
      {/* Header */}
      <header className="py-4 text-center border-b border-[#333333] text-xs font-bold tracking-[0.2em] text-gray-500 shadow-sm">
        MEDICAL AI AGENT
      </header>

      {/* Chat History Area */}
      <main className="flex-1 overflow-y-auto w-full max-w-4xl mx-auto p-4 space-y-8 mt-4 scroll-smooth">
        {messages.length === 0 ? (
          <div className="flex items-center justify-center h-full text-gray-600 font-medium tracking-wide animate-fade-in-up">
            How can I assist with your medical data today?
          </div>
        ) : (
          messages.map((msg, idx) => (
            <div key={idx} className={`flex animate-fade-in-up ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
              <div className={`max-w-[85%] leading-relaxed tracking-wide shadow-sm transition-all duration-300 ${msg.role === "user" ? "bg-[#2A2A2A] text-white px-5 py-3 rounded-2xl" : "bg-transparent text-gray-300"}`}>
                {msg.role === "assistant" && <span className="mr-3 text-lg opacity-80 inline-block animate-pulse">🧬</span>}
                {msg.content}
              </div>
            </div>
          ))
        )}
        
        {/* Master-Level Thinking Animation */}
        {isLoading && (
          <div className="flex justify-start mt-4 animate-fade-in-up">
            <div className="bg-transparent text-gray-300 max-w-[85%] leading-relaxed flex items-center">
              <span className="mr-3 text-lg opacity-80 animate-pulse inline-block">🧬</span>
              <div className="flex space-x-2 items-center bg-[#1A1A1A] border border-[#333333] px-5 py-4 rounded-2xl shadow-lg">
                <div className="w-2 h-2 bg-[#00E676] rounded-full animate-bounce" style={{ animationDelay: "0ms", animationDuration: "1s" }}></div>
                <div className="w-2 h-2 bg-[#00E676] rounded-full animate-bounce" style={{ animationDelay: "150ms", animationDuration: "1s" }}></div>
                <div className="w-2 h-2 bg-[#00E676] rounded-full animate-bounce" style={{ animationDelay: "300ms", animationDuration: "1s" }}></div>
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Input Area */}
      <div className="w-full max-w-3xl mx-auto p-4 pb-8 bg-gradient-to-t from-[#111111] via-[#111111] to-transparent">
        <form onSubmit={handleSubmit} className="relative flex items-center group">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Message the Medical AI..."
            className="w-full bg-[#1A1A1A] border border-[#333333] rounded-2xl px-5 py-4 pr-12 focus:outline-none focus:border-[#00E676] focus:ring-1 focus:ring-[#00E676] focus:shadow-[0_0_20px_rgba(0,230,118,0.15)] shadow-xl text-white placeholder-gray-500 transition-all duration-300"
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={isLoading || !input.trim()}
            className="absolute right-4 p-2 text-gray-400 hover:text-[#00E676] disabled:opacity-30 hover:scale-110 active:scale-95 transition-all duration-200"
          >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-5 h-5">
              <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 10.5 12 3m0 0 7.5 7.5M12 3v18" />
            </svg>
          </button>
        </form>
        <p className="text-center text-[11px] text-gray-600 mt-3 font-medium tracking-wide">
          AI can make mistakes. Verify critical clinical information.
        </p>
      </div>
      
    </div>
  );
}