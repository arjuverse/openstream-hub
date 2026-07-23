import React from "react";
import { Channel } from "@/types/channel";

interface RecentChannelsRowProps {
  channels: Channel[];
}

export const RecentChannelsRow: React.FC<RecentChannelsRowProps> = ({ channels }) => {
  return (
    <div className="flex gap-4 overflow-x-auto pb-2">
      {channels.length === 0 ? (
        <p className="text-sm text-muted-foreground">No recent channels found.</p>
      ) : (
        channels.map((channel) => (
          <div key={channel.id} className="min-w-[150px] bg-card border rounded-lg p-3">
            <p className="font-medium truncate">{channel.displayName}</p>
          </div>
        ))
      )}
    </div>
  );
};