import { api } from "./client";
import type { PaginatedChannels } from "@/types/channel";

interface GetChannelsParams {
  page: number;
  size: number;
  search?: string;
  category?: string;
  sort?: string;
  order?: string;
}

export async function getChannels(
  params: GetChannelsParams,
): Promise<PaginatedChannels> {
  const response = await api.get("/channels/", {
    params,
  });

  return response.data;
}