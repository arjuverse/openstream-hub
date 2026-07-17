import { useQuery } from "@tanstack/react-query";
import { getNowPlaying } from "@/api/channel";

export function useNowPlaying(channelId: number) {
  return useQuery({
    queryKey: ["channel", channelId, "now-playing"],
    queryFn: () => getNowPlaying(channelId),
    enabled: !!channelId,
    refetchInterval: 60 * 1000, // Polls every 60 seconds to keep EPG fresh
  });
}