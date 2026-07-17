import { api } from "./client";
import type { Channel } from "@/types/channel";

export async function getChannel(id: number): Promise<Channel> {
  const response = await api.get(`/channels/${id}`);
  return response.data;
}