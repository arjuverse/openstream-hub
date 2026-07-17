import { Heart, Play } from "lucide-react";
import { useNavigate } from "react-router-dom";

import type { Channel } from "@/types/channel";

interface ChannelCardProps {
  channel: Channel;
}

export default function ChannelCard({
  channel,
}: ChannelCardProps) {
  const navigate = useNavigate();

  return (
    <div className="rounded-xl border bg-white p-4 shadow-sm transition hover:shadow-md dark:border-zinc-800 dark:bg-zinc-900">
      <div className="flex items-center gap-4">
        <img
          src={channel.logo_url || "https://placehold.co/64x64?text=TV"}
          alt={channel.name}
          className="h-14 w-14 rounded-lg object-contain"
        />

        <div className="min-w-0 flex-1">
          <h3 className="truncate font-semibold">
            {channel.name}
          </h3>

          <p className="text-sm text-zinc-500">
            {channel.group_title || "Unknown"}
          </p>
        </div>
      </div>

      <div className="mt-4 flex gap-2">
        <button
          onClick={() => navigate(`/watch/${channel.id}`)}
          className="flex flex-1 items-center justify-center gap-2 rounded-lg bg-zinc-900 px-3 py-2 text-white transition hover:bg-black dark:bg-white dark:text-black"
        >
          <Play size={16} />
          Play
        </button>

        <button className="rounded-lg border p-2 hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800">
          <Heart size={18} />
        </button>
      </div>
    </div>
  );
}