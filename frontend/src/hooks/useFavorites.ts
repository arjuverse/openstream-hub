import { useState, useEffect } from "react";
import type { Channel } from "@/types/channel";

const FAVORITES_KEY = "openstream_favorites";

export function useFavorites() {
  const [favorites, setFavorites] = useState<Channel[]>([]);

  // Load from local storage on mount
  useEffect(() => {
    const stored = localStorage.getItem(FAVORITES_KEY);
    if (stored) {
      try {
        setFavorites(JSON.parse(stored));
      } catch (e) {
        console.error("Failed to parse favorites", e);
      }
    }
  }, []);

  // Toggle favorite status (Add if missing, remove if exists)
  const toggleFavorite = (channel: Channel) => {
    setFavorites((prev) => {
      const isFavorited = prev.some((c) => c.id === channel.id);
      let updated;
      
      if (isFavorited) {
        // Remove from favorites
        updated = prev.filter((c) => c.id !== channel.id);
      } else {
        // Add to favorites
        updated = [...prev, channel];
      }
      
      localStorage.setItem(FAVORITES_KEY, JSON.stringify(updated));
      return updated;
    });
  };

  // Helper function to quickly check if a channel is favorited
  const isFavorite = (channelId: number) => {
    return favorites.some((c) => c.id === channelId);
  };

  return { favorites, toggleFavorite, isFavorite };
}