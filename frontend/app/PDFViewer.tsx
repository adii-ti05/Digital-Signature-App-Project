"use client";
import { Document, Page, pdfjs } from "react-pdf";

pdfjs.GlobalWorkerOptions.workerSrc =
  `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

export function PdfViewer({ file }: { file: string }) {
  return (
    <Document file={file}>
      <Page pageNumber={1} scale={1.5} />
    </Document>
  );
}