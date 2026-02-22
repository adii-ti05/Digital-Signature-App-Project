"use client";
import { useEffect, useState } from "react";

export default function AuditPage() {
  const [logs, setLogs] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/audit", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    })
      .then(res => res.json())
      .then(data => setLogs(data));
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Audit Trail</h2>

      <table className="w-full bg-white shadow rounded">
        <thead>
          <tr className="border-b">
            <th className="p-2">Action</th>
            <th>User</th>
            <th>IP</th>
            <th>Timestamp</th>
          </tr>
        </thead>

        <tbody>
          {logs.map(log => (
            <tr key={log.id} className="border-b">
              <td className="p-2">{log.action}</td>
              <td>{log.user}</td>
              <td>{log.ip}</td>
              <td>{log.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}