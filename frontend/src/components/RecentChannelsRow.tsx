import { Link } from "react-router-dom";
import { useRecentChannels } from "@/hooks/useRecentChannels";

export function RecentChannelsRow() {
  const { recentChannels } = useRecentChannels();

  // If there is no watch history yet, hide this entire section
  if (recentChannels.length === 0) {
    return null; 
  }

  return (
    <div className="mb-8">
      <h2 className="mb-4 text-xl font-bold">Recently Watched</h2>
      
      {/* Horizontal scrolling container */}
      <div className="flex gap-4 overflow-x-auto pb-4 scrollbar-hide">
        {recentChannels.map((channel) => (
          <Link
            key={channel.id}
            to={`/watch/${channel.id}`}
            className="flex-shrink-0 w-48 rounded-xl border border-zinc-200 bg-white p-4 transition-all hover:border-zinc-300 hover:shadow-md dark:border-zinc-800 dark:bg-zinc-900 dark:hover:border-zinc-700"
          >
            {/* Logo Area */}
            <div className="mb-3 flex aspect-video w-full items-center justify-center rounded-lg bg-zinc-100 p-2 dark:bg-zinc-800">
              {channel.logo_url ? (
                <img
                  src={channel.logo_url}
                  alt={channel.name}
                  className="max-h-full max-w-full object-contain"
                />
              ) : (
                <span className="text-sm text-zinc-400">No Logo</span>
              )}
            </div>

            {/* Channel Info */}
            <h3 className="truncate font-medium">{channel.name}</h3>
            {channel.group_title && (
              <p className="mt-1 truncate text-xs text-zinc-500">
                {channel.group_title}
              </p>
            )}
          </Link>
        ))}
      </div>
    </div>
  );
}