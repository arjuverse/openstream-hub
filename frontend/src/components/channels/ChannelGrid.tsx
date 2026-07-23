import React from "react";
import { Channel } from "@/types/channel";

interface ChannelGridProps {
  channels: Channel[];
  isLoading: boolean;
}

export const ChannelGrid: React.FC<ChannelGridProps> = ({ channels, isLoading }) => {
  if (isLoading) {
    return <div className="text-center py-10">Loading channels...</div>;
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      {channels.map((channel) => (
        <div key={channel.id} className="border bg-card rounded-lg p-4 space-y-2">
          <h3 className="font-semibold">{channel.displayName}</h3>
        </div>
      ))}
    </div>
  );
};