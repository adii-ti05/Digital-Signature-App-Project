"use client";
import { DndContext, useDraggable } from "@dnd-kit/core";
import { useState } from "react";

function DraggableSignature() {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: "signature",
  });

  const style = {
    transform: transform
      ? `translate(${transform.x}px, ${transform.y}px)`
      : undefined,
  };

  return (
    <div
      ref={setNodeRef}
      style={style}
      {...listeners}
      {...attributes}
      className="bg-black text-white p-2 cursor-move"
    >
      Digital Signature
    </div>
  );
}

export function SignaturePad() {
  return (
    <DndContext>
      <DraggableSignature />
    </DndContext>
  );
}