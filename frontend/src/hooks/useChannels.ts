import { useQuery } from "@tanstack/react-query";

import { getChannels } from "../api/channels";

export function useChannels(page = 1) {
  return useQuery({
    queryKey: ["channels", page],
    queryFn: () => getChannels(page),
  });
}
