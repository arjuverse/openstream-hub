interface PaginationBarProps {
  page: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

export default function PaginationBar({
  page,
  totalPages,
  onPageChange,
}: PaginationBarProps) {
  return (
    <div className="mt-8 flex items-center justify-center gap-2">
      <button
        onClick={() => onPageChange(page - 1)}
        disabled={page === 1}
        className="rounded-lg border px-4 py-2 disabled:cursor-not-allowed disabled:opacity-40"
      >
        ← Previous
      </button>

      {Array.from({ length: totalPages }, (_, i) => i + 1)
        .slice(Math.max(0, page - 3), Math.min(totalPages, page + 2))
        .map((p) => (
          <button
            key={p}
            onClick={() => onPageChange(p)}
            className={`rounded-lg px-4 py-2 ${
              p === page
                ? "bg-zinc-900 text-white dark:bg-white dark:text-black"
                : "border"
            }`}
          >
            {p}
          </button>
        ))}

      <button
        onClick={() => onPageChange(page + 1)}
        disabled={page === totalPages}
        className="rounded-lg border px-4 py-2 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Next →
      </button>
    </div>
  );
}