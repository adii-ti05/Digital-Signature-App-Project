"use client";
import { useEffect, useState } from "react";
import { StatusBadge } from "../app/StatusBadge";

export default function Dashboard() {
  const [docs, setDocs] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/documents", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then(res => res.json())
      .then(data => setDocs(data));
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Dashboard</h2>

      <div className="grid gap-4">
        {docs.map(doc => (
          <div
            key={doc.id}
            className="bg-white p-4 shadow rounded flex justify-between"
          >
            <div>
              <p className="font-semibold">{doc.filename}</p>
              <StatusBadge status={doc.status} />
            </div>

            <a
              href={`/document/${doc.id}`}
              className="text-blue-500 underline"
            >
              Open
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}