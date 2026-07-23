import React from "react";
import { useParams, useNavigate } from "react-router-dom";
import { useChannel } from "../hooks/useChannel";
import { VideoPlayer } from "../components/VideoPlayer";
import { Channel } from "../types/channel";

export const Watch: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { data: channel, isLoading, error } = useChannel(id || "");

  const handleChannelSelect = (selectedChannel: Channel) => {
    navigate(`/watch/${selectedChannel.id}`);
  };

  if (isLoading) {
    return <div className="flex justify-center items-center h-[80vh]">Loading stream...</div>;
  }

  if (error || !channel) {
    return <div className="text-center py-20 text-destructive">Channel not found or offline.</div>;
  }

  return (
    <div className="container mx-auto px-4 py-6 space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-4">
          <VideoPlayer src={channel.streamUrl || ""} poster={channel.icon} />
          <div>
            <h1 className="text-2xl font-bold">{channel.displayName}</h1>
            <p className="text-muted-foreground text-sm mt-1">EPG ID: {channel.epgId}</p>
          </div>
        </div>

        <div className="bg-card border rounded-lg p-4 space-y-4 h-fit">
          <h2 className="font-semibold text-lg">Broadcast Schedule</h2>
          <div className="text-sm text-muted-foreground">
            Live schedule and metadata will appear here as the EPG syncs.
          </div>
        </div>
      </div>
    </div>
  );
};