export function StatusBadge({ status }: { status: string }) {
  const styles: any = {
    Pending: "bg-yellow-100 text-yellow-700",
    Signed: "bg-green-100 text-green-700",
    Rejected: "bg-red-100 text-red-700",
  };

  return (
    <span className={`px-3 py-1 rounded-full text-xs ${styles[status]}`}>
      {status}
    </span>
  );
}