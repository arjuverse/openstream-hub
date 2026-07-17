import { Link } from "react-router-dom";
import type { Channel } from "@/types/channel";
import { useFavorites } from "@/hooks/useFavorites";

interface ChannelGridProps {
  channels: Channel[];
}

export default function ChannelGrid({ channels }: ChannelGridProps) {
  const { toggleFavorite, isFavorite } = useFavorites();

  if (channels.length === 0) {
    return (
      <div className="py-12 text-center text-zinc-500">
        No channels found.
      </div>
    );
  }

  return (
    <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 xl:grid-cols-8">
      {channels.map((channel) => {
        const isFav = isFavorite(channel.id);

        return (
          <Link
            key={channel.id}
            to={`/watch/${channel.id}`}
            className="group relative flex flex-col overflow-hidden rounded-xl border border-zinc-200 bg-white transition-all hover:border-zinc-300 hover:shadow-md dark:border-zinc-800 dark:bg-zinc-900 dark:hover:border-zinc-700"
          >
            {/* Favorite Toggle Button (Absolute Positioned in Top Right) */}
            <button
              onClick={(e) => {
                e.preventDefault(); // Prevents the Link from firing
                e.stopPropagation();
                toggleFavorite(channel.id);
              }}
              className="absolute right-2 top-2 z-10 rounded-full bg-black/40 p-1.5 text-white backdrop-blur-sm transition-all hover:bg-black/60 hover:scale-110"
              aria-label={isFav ? "Remove from favorites" : "Add to favorites"}
            >
              <svg
                className="h-5 w-5 transition-all"
                fill={isFav ? "#ef4444" : "none"} // red-500
                stroke={isFav ? "#ef4444" : "currentColor"}
                viewBox="0 0 24 24"
                strokeWidth={isFav ? "0" : "2"}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                />
              </svg>
            </button>

            {/* Logo Area */}
            <div className="flex aspect-video w-full items-center justify-center bg-zinc-100 p-4 dark:bg-zinc-800">
              {channel.logo_url ? (
                <img
                  src={channel.logo_url}
                  alt={channel.name}
                  className="max-h-full max-w-full object-contain drop-shadow-sm transition-transform duration-300 group-hover:scale-105"
                  loading="lazy"
                />
              ) : (
                <span className="text-sm text-zinc-400">No Logo</span>
              )}
            </div>

            {/* Channel Info */}
            <div className="flex flex-1 flex-col p-3">
              <h3 className="line-clamp-1 font-medium text-zinc-900 dark:text-zinc-100">
                {channel.name}
              </h3>
              {channel.group_title && (
                <p className="mt-1 line-clamp-1 text-xs text-zinc-500">
                  {channel.group_title}
                </p>
              )}
            </div>
          </Link>
        );
      })}
    </div>
  );
}