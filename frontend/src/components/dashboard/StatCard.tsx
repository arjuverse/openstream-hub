import React from "react";

interface StatCardProps {
  title: string;
  value: string | number;
  description: string;
}

export const StatCard: React.FC<StatCardProps> = ({ title, value, description }) => {
  return (
    <div className="bg-card border rounded-lg p-6 space-y-2 shadow-sm">
      <h3 className="text-sm font-medium text-muted-foreground">{title}</h3>
      <div className="text-2xl font-bold">{value}</div>
      <p className="text-xs text-muted-foreground">{description}</p>
    </div>
  );
};