import React from "react";
import { useRecentChannels } from "../hooks/useRecentChannels";
import { RecentChannelsRow } from "../components/dashboard/RecentChannels"; // Adjusted path
import { StatCard } from "../components/dashboard/StatCard";

export const Dashboard: React.FC = () => {
  const { data: recentChannels = [] } = useRecentChannels();

  return (
    <div className="container mx-auto px-4 py-8 space-y-8">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Dashboard</h1>
        <p className="text-muted-foreground">Welcome back to your OpenStream Hub streaming dashboard.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <StatCard title="Active Streams" value="12" description="Currently broadcasting live" />
        <StatCard title="Total Channels" value="148" description="Indexed in database" />
        <StatCard title="System Status" value="Healthy" description="All containers operational" />
      </div>

      <div className="space-y-4">
        <h2 className="text-xl font-semibold tracking-tight">Recent Channels</h2>
        <RecentChannelsRow channels={recentChannels} />
      </div>
    </div>
  );
};