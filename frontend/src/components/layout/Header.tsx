export default function Header() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-6 dark:bg-zinc-950">
      <h2 className="text-lg font-semibold">
        Dashboard
      </h2>

      <div className="text-sm text-zinc-500">
        OpenStream Hub
      </div>
    </header>
  );
}