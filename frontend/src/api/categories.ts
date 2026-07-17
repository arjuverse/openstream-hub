import { api } from "./client";

export async function getCategories(): Promise<string[]> {
  const response = await api.get("/channels/categories");

  return response.data;
}