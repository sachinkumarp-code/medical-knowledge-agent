import { Inter } from "next/font/google";
import "./globals.css";

// Load the premium Inter font
const inter = Inter({ 
  subsets: ["latin"], 
  variable: "--font-inter" 
});

export const metadata = {
  title: "Medical AI",
  description: "Advanced Medical Knowledge Agent",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${inter.variable} font-sans antialiased`}>
        {children}
      </body>
    </html>
  );
}