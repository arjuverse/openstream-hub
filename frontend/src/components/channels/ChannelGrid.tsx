import type { Channel } from "@/types/channel";
import ChannelCard from "./ChannelCard";

interface ChannelGridProps {
  channels: Channel[];
}

export default function ChannelGrid({
  channels,
}: ChannelGridProps) {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4">
      {channels.map((channel) => (
        <ChannelCard
          key={channel.id}
          channel={channel}
        />
      ))}
    </div>
  );
}