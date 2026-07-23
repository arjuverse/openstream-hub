import React from "react";

export const Favorites: React.FC = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold tracking-tight">Favorite Channels</h1>
      <p className="text-muted-foreground mt-2">Your pinned channels will appear here.</p>
    </div>
  );
};