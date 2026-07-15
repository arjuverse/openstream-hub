import {
  CalendarDays,
  Heart,
  LayoutDashboard,
  Settings,
  Tv,
} from "lucide-react";

import SidebarItem from "./SidebarItem";

export default function Sidebar() {
  return (
    <aside className="w-64 shrink-0 border-r bg-white dark:bg-zinc-950">
      <div className="p-6">

        <h1 className="mb-8 text-2xl font-bold">
          OpenStream Hub
        </h1>

        <nav className="space-y-2">
          <SidebarItem
            title="Dashboard"
            href="/dashboard"
            icon={LayoutDashboard}
          />

          <SidebarItem
            title="Channels"
            href="/channels"
            icon={Tv}
          />

          <SidebarItem
            title="TV Guide"
            href="/guide"
            icon={CalendarDays}
          />

          <SidebarItem
            title="Favorites"
            href="/favorites"
            icon={Heart}
          />

          <SidebarItem
            title="Settings"
            href="/settings"
            icon={Settings}
          />
        </nav>

      </div>
    </aside>
  );
}