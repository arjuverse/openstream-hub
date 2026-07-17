import { useQuery } from "@tanstack/react-query";
import { getChannels } from "@/api/channels";

interface UseChannelsParams {
  page: number;
  size: number;
  search?: string;
  category?: string;
  sort?: string;
  order?: string;
}

export function useChannels(params: UseChannelsParams) {
  return useQuery({
    queryKey: ["channels", params],
    queryFn: () => getChannels(params),
  });
}