import { Link, useLocation } from "react-router-dom";
import type { LucideIcon } from "lucide-react";

interface SidebarItemProps {
  title: string;
  href: string;
  icon: LucideIcon;
}

export default function SidebarItem({
  title,
  href,
  icon: Icon,
}: SidebarItemProps) {
  const location = useLocation();

  const active = location.pathname === href;

  return (
    <Link
      to={href}
      className={[
        "flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors",
        active
          ? "bg-zinc-900 text-white dark:bg-white dark:text-black"
          : "text-zinc-700 hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-800",
      ].join(" ")}
    >
      <Icon size={18} />
      <span>{title}</span>
    </Link>
  );
}