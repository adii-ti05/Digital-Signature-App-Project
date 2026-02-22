import "./globals.css";
import type { Metadata } from "next";
import { Sidebar } from "./Sidebar";
import { Topbar } from "./Topbar";

export const metadata: Metadata = {
  title: "Signature App",
  description: "Professional PDF Digital Signature Platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-gray-100 text-gray-900 antialiased">
        <div className="flex min-h-screen">
          
          {/* LEFT SIDEBAR */}
          <Sidebar />

          {/* RIGHT CONTENT AREA */}
          <div className="flex flex-1 flex-col">
            
            {/* TOPBAR */}
            <Topbar />

            {/* PAGE CONTENT */}
            <main className="flex-1 p-6 overflow-y-auto">
              {children}
            </main>

          </div>
        </div>
      </body>
    </html>
  );
}