import { useQuery } from "@tanstack/react-query";
import { getChannels } from "@/api/channels";

export function useChannels(page = 1, size = 24) {
  return useQuery({
    queryKey: ["channels", page, size],
    queryFn: () => getChannels(page, size),
  });
}