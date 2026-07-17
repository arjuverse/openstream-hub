import { useQuery } from "@tanstack/react-query";
import { getChannel } from "@/api/channel";

export function useChannel(id: number) {
  return useQuery({
    queryKey: ["channel", id],
    queryFn: () => getChannel(id),
    enabled: !!id,
  });
}