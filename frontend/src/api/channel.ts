import { api } from "./client";
import type { Channel } from "@/types/channel";

export async function getChannel(id: number): Promise<Channel> {
  const response = await api.get(`/channels/${id}`);
  return response.data;
}

export interface Programme {
  id: number;
  title: string;
  description: string | null;
  category: string | null;
  start_time: string;
  stop_time: string;
  episode: string | null;
  rating: string | null;
}

export async function getNowPlaying(id: number): Promise<Programme | null> {
  const response = await api.get(`/channels/${id}/now-playing`);
  return response.data;
}