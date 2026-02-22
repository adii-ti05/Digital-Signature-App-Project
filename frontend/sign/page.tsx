"use client";
import { useParams } from "next/navigation";
import { PdfViewer } from "../app/PDFViewer";
import { useState } from "react";

export default function PublicSign() {
  const { token } = useParams();
  const [reason, setReason] = useState("");

  function sign() {
    fetch(`http://localhost:8000/public-sign/${token}`, {
      method: "POST",
    }).then(() => alert("Signed"));
  }

  function reject() {
    fetch(`http://localhost:8000/reject/${token}`, {
      method: "POST",
      body: JSON.stringify({ reason }),
    }).then(() => alert("Rejected"));
  }

  return (
    <div>
      <PdfViewer file={`http://localhost:8000/public-pdf/${token}`} />

      <button onClick={sign} className="bg-green-600 px-6 py-2 text-white rounded">
        Sign
      </button>

      <div className="mt-4">
        <textarea
          placeholder="Rejection Reason"
          value={reason}
          onChange={e => setReason(e.target.value)}
          className="border p-2 w-full"
        />
        <button
          onClick={reject}
          className="bg-red-600 px-6 py-2 text-white rounded mt-2"
        >
          Reject
        </button>
      </div>
    </div>
  );
}