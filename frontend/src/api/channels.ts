import { api } from "./client";
import type { PaginatedChannels } from "@/types/channel";

export async function getChannels(
  page = 1,
  size = 24
): Promise<PaginatedChannels> {
  const response = await api.get("/channels/", {
    params: {
      page,
      size,
    },
  });

  return response.data;
}