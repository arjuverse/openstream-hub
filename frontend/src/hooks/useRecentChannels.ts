import { useState, useEffect } from "react";
import type { Channel } from "@/types/channel";

const RECENT_CHANNELS_KEY = "openstream_recent_channels";
const MAX_RECENT = 10;

export function useRecentChannels() {
  const [recentChannels, setRecentChannels] = useState<Channel[]>([]);

  // Load from local storage on mount
  useEffect(() => {
    const stored = localStorage.getItem(RECENT_CHANNELS_KEY);
    if (stored) {
      try {
        setRecentChannels(JSON.parse(stored));
      } catch (e) {
        console.error("Failed to parse recent channels", e);
      }
    }
  }, []);

  // Add a new channel to the list
  const addRecentChannel = (channel: Channel) => {
    setRecentChannels((prev) => {
      // Remove the channel if it already exists to avoid duplicates
      const filtered = prev.filter((c) => c.id !== channel.id);
      
      // Add the new channel to the front of the array and limit to MAX_RECENT
      const updated = [channel, ...filtered].slice(0, MAX_RECENT);
      
      // Save back to local storage
      localStorage.setItem(RECENT_CHANNELS_KEY, JSON.stringify(updated));
      return updated;
    });
  };

  return { recentChannels, addRecentChannel };
}