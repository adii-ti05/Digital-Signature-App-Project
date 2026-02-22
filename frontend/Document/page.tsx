"use client";
import { useParams } from "next/navigation";
import { PdfViewer } from "../app/PDFViewer";
import { SignaturePad } from "../app/SignaturePad";

export default function DocumentPage() {
  const { id } = useParams();

  function sign() {
    fetch(`http://localhost:8000/sign/${id}`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    }).then(() => {
      alert("Signed Successfully");
      window.location.href = "/dashboard";
    });
  }

  return (
    <div>
      <PdfViewer file={`http://localhost:8000/pdf/${id}`} />
      <SignaturePad />
      <button
        onClick={sign}
        className="bg-green-600 text-white px-6 py-2 mt-4 rounded"
      >
        Generate Signed PDF
      </button>
    </div>
  );
}