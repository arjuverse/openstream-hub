import { useState, useEffect, useCallback } from "react";

const FAVORITES_KEY = "openstream_favorites";

export function useFavorites() {
  const [favoriteIds, setFavoriteIds] = useState<number[]>([]);

  // 1. Cleaner parsing logic
  useEffect(() => {
    try {
      const stored = JSON.parse(
        localStorage.getItem(FAVORITES_KEY) ?? "[]"
      );
      setFavoriteIds(stored);
    } catch {
      setFavoriteIds([]);
    }
  }, []);

  // 2. Toggling now only requires the ID
  const toggleFavorite = useCallback((channelId: number) => {
    setFavoriteIds((prev) => {
      const isFavorited = prev.includes(channelId);
      
      const updated = isFavorited
        ? prev.filter((id) => id !== channelId)
        : [...prev, channelId];
      
      localStorage.setItem(FAVORITES_KEY, JSON.stringify(updated));
      return updated;
    });
  }, []);

  // 3. Lookup is simplified directly against the ID array
  const isFavorite = useCallback((channelId: number) => {
    return favoriteIds.includes(channelId);
  }, [favoriteIds]);

  return { favoriteIds, toggleFavorite, isFavorite };
}