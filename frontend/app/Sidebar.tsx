"use client";
import Link from "next/link";

export function Sidebar() {
  return (
    <div className="w-64 bg-white shadow-md p-6">
      <h1 className="text-xl font-bold mb-6">DocSign</h1>

      <nav className="space-y-4">
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/upload">Upload</Link>
        <Link href="/audit">Audit Logs</Link>
      </nav>
    </div>
  );
}