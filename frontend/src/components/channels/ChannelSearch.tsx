import React from "react";
import { Input } from "@/components/ui/input";

interface ChannelSearchProps {
  onSearch: (query: string) => void;
}

export const ChannelSearch: React.FC<ChannelSearchProps> = ({ onSearch }) => {
  return (
    <div className="w-full md:w-72">
      <Input
        placeholder="Search channels..."
        onChange={(e) => onSearch(e.target.value)}
      />
    </div>
  );
};