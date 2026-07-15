import type { Channel } from "@/types/channel";

interface RecentChannelsProps {
  channels: Channel[];
}

export default function RecentChannels({
  channels,
}: RecentChannelsProps) {
  return (
    <div className="rounded-xl border bg-white p-6 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
      <h2 className="mb-4 text-xl font-semibold">
        Recent Channels
      </h2>

      <div className="space-y-3">
        {channels.map((channel) => (
          <div
            key={channel.id}
            className="flex items-center gap-4 rounded-lg border p-3 dark:border-zinc-800"
          >
            <img
              src={channel.logo_url || "/placeholder.png"}
              alt={channel.name}
              className="h-10 w-10 rounded object-contain"
            />

            <div>
              <div className="font-medium">
                {channel.name}
              </div>

              <div className="text-sm text-zinc-500">
                {channel.group_title ?? "Unknown"}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}