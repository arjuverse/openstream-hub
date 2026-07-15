import {
  FolderKanban,
  Heart,
  Layers3,
  Tv,
} from "lucide-react";

import StatCard from "@/components/dashboard/StatCard";
import RecentChannels from "@/components/dashboard/RecentChannels";
import { useChannels } from "@/hooks/useChannels";

export default function Dashboard() {
  const { data, isPending, error } = useChannels();

  if (isPending) {
    return <div className="p-8">Loading...</div>;
  }

  if (error || !data) {
    return (
      <div className="p-8 text-red-600">
        Failed to load dashboard.
      </div>
    );
  }

  const uniqueCategories = new Set(
    data.items.map((c) => c.category).filter(Boolean)
  ).size;

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold">
          Dashboard
        </h1>

        <p className="mt-1 text-zinc-500">
          Welcome to OpenStream Hub
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <StatCard
          title="Channels"
          value={data.total}
          icon={Tv}
        />

        <StatCard
          title="Playlists"
          value={1}
          icon={FolderKanban}
        />

        <StatCard
          title="Categories"
          value={uniqueCategories}
          icon={Layers3}
        />

        <StatCard
          title="Favorites"
          value={0}
          icon={Heart}
        />
      </div>

      <RecentChannels channels={data.items.slice(0, 8)} />
    </div>
  );
}