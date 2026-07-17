import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { useChannel } from "@/hooks/useChannel";
import { VideoPlayer } from "@/components/VideoPlayer";
import { useRecentChannels } from "@/hooks/useRecentChannels";
import { useFavorites } from "@/hooks/useFavorites";

export default function Watch() {
  const { id } = useParams();
  const channelId = Number(id);

  const { data, isPending, error } = useChannel(channelId);
  const { addRecentChannel } = useRecentChannels();
  const { toggleFavorite, isFavorite } = useFavorites();

  // Trigger the addition when channel data successfully loads
  useEffect(() => {
    if (data) {
      addRecentChannel(data);
    }
  }, [data]);

  if (isPending) {
    return <div className="p-8">Loading player...</div>;
  }

  if (error || !data) {
    return (
      <div className="p-8 text-red-600">
        Failed to load channel.
      </div>
    );
  }

  // Check if the current channel is in the favorites list
  const isFav = isFavorite(data.id);

  return (
    <div className="mx-auto max-w-7xl space-y-6 p-6">
      <VideoPlayer 
        streamUrl={data.stream_url} 
        poster={data.logo_url ?? undefined} 
      />

      <div className="flex items-center gap-4">
        <img
          src={data.logo_url ?? ""}
          alt={data.name}
          className="h-16 w-16 rounded-lg object-contain"
        />

        <div className="flex-1">
          <div className="flex items-center gap-3">
            <h1 className="text-3xl font-bold">
              {data.name}
            </h1>
            
            {/* Favorite Toggle Button */}
            <button
              onClick={() => toggleFavorite(data.id)}
              className={`p-2 rounded-full transition-colors ${
                isFav 
                  ? "text-red-500 bg-red-50 hover:bg-red-100 dark:bg-red-950/30 dark:hover:bg-red-900/50" 
                  : "text-zinc-400 hover:text-red-500 hover:bg-zinc-100 dark:hover:bg-zinc-800"
              }`}
              aria-label={isFav ? "Remove from favorites" : "Add to favorites"}
            >
              <svg 
                className="w-7 h-7 transition-all" 
                fill={isFav ? "currentColor" : "none"} 
                stroke="currentColor" 
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
          </div>

          <p className="mt-1 text-zinc-500">
            {data.group_title}
          </p>
        </div>
      </div>

      <div className="rounded-lg bg-zinc-100 p-4 dark:bg-zinc-800">
        <p className="font-medium">Stream URL</p>

        <p className="mt-2 break-all text-sm text-zinc-500">
          {data.stream_url}
        </p>
      </div>
    </div>
  );
}