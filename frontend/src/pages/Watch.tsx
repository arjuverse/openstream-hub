import { useEffect } from "react";
import { useParams } from "react-router-dom";
import { useChannel } from "@/hooks/useChannel";
import { useNowPlaying } from "@/hooks/useNowPlaying";
import { VideoPlayer } from "@/components/VideoPlayer";
import { useRecentChannels } from "@/hooks/useRecentChannels";
import { useFavorites } from "@/hooks/useFavorites";

export default function Watch() {
  const { id } = useParams();
  const channelId = Number(id);

  const { data, isPending, error } = useChannel(channelId);
  const { addRecentChannel } = useRecentChannels();
  const { toggleFavorite, isFavorite } = useFavorites();
  
  // Fetch the currently playing EPG data
  const { data: nowPlaying } = useNowPlaying(channelId);

  // Trigger the addition when channel data successfully loads
  useEffect(() => {
    if (data) {
      addRecentChannel(data.id); // Updated to use ID based on our previous optimization
    }
  }, [data, addRecentChannel]);

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

  const isFav = isFavorite(data.id);

  // Helper function to format ISO dates to local time (e.g., "8:00 AM")
  const formatTime = (isoString: string) => {
    return new Date(isoString).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  return (
    <div className="mx-auto max-w-7xl space-y-6 p-6">
      <VideoPlayer 
        streamUrl={data.stream_url} 
        poster={data.logo_url ?? undefined} 
      />

      <div className="flex items-center gap-4">
        <div className="flex h-16 w-16 items-center justify-center overflow-hidden rounded-lg bg-zinc-100 dark:bg-zinc-800">
          {data.logo_url ? (
            <img
              src={data.logo_url}
              alt={data.name}
              className="h-full w-full object-contain"
            />
          ) : (
            <span className="text-xs text-zinc-400">No Logo</span>
          )}
        </div>

        <div className="flex-1">
          <div className="flex items-center gap-3">
            <h1 className="text-3xl font-bold text-zinc-900 dark:text-zinc-100">
              {data.name}
            </h1>
            
            {/* Favorite Toggle Button */}
            <button
              onClick={() => toggleFavorite(data.id)}
              className={`rounded-full p-2 transition-colors ${
                isFav 
                  ? "bg-red-50 text-red-500 hover:bg-red-100 dark:bg-red-950/30 dark:hover:bg-red-900/50" 
                  : "text-zinc-400 hover:bg-zinc-100 hover:text-red-500 dark:hover:bg-zinc-800"
              }`}
              aria-label={isFav ? "Remove from favorites" : "Add to favorites"}
            >
              <svg 
                className="h-7 w-7 transition-all" 
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

          <p className="mt-1 text-sm text-zinc-500">
            {data.group_title || data.category}
          </p>
        </div>
      </div>

      {/* Now Playing EPG Section */}
      {nowPlaying && (
        <div className="rounded-xl border border-zinc-200 bg-white p-5 shadow-sm dark:border-zinc-800 dark:bg-zinc-900">
          <div className="mb-3 flex items-center gap-2">
            <span className="flex h-2.5 w-2.5 relative">
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-red-400 opacity-75"></span>
              <span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-red-500"></span>
            </span>
            <span className="text-xs font-bold uppercase tracking-wider text-red-500">
              Live Now
            </span>
          </div>
          
          <h2 className="text-xl font-semibold text-zinc-900 dark:text-zinc-100">
            {nowPlaying.title}
          </h2>
          
          <p className="mt-1 font-mono text-sm font-medium text-zinc-500">
            {formatTime(nowPlaying.start_time)} - {formatTime(nowPlaying.stop_time)}
          </p>

          {nowPlaying.description && (
            <p className="mt-3 leading-relaxed text-zinc-600 dark:text-zinc-400">
              {nowPlaying.description}
            </p>
          )}

          {nowPlaying.category && (
            <div className="mt-4 inline-flex items-center rounded-md bg-zinc-100 px-2.5 py-1 text-xs font-medium text-zinc-600 dark:bg-zinc-800 dark:text-zinc-300">
              {nowPlaying.category}
            </div>
          )}
        </div>
      )}

      <div className="rounded-lg bg-zinc-100 p-4 dark:bg-zinc-800">
        <p className="font-medium text-zinc-900 dark:text-zinc-100">Stream URL</p>
        <p className="mt-2 break-all font-mono text-sm text-zinc-500">
          {data.stream_url}
        </p>
      </div>
    </div>
  );
}