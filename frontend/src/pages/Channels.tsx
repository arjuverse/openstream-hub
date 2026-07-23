import React, { useState } from "react";
import { useChannels } from "../hooks/useChannels";
import { ChannelGrid } from "../components/channels/ChannelGrid";
import { ChannelSearch } from "../components/channels/ChannelSearch";
import { CategoryFilter } from "../components/channels/CategoryFilter";
import { PaginationBar } from "../components/channels/PaginationBar";

export const Channels: React.FC = () => {
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState<string | undefined>(undefined);

  const { data, isLoading, error } = useChannels({ page, search, category });

  return (
    <div className="container mx-auto px-4 py-8 space-y-6">
      <div className="flex flex-col md:flex-row justify-between items-center gap-4">
        <h1 className="text-3xl font-bold tracking-tight">Channels</h1>
        <ChannelSearch onSearch={setSearch} />
      </div>

      <CategoryFilter selectedCategory={category} onSelectCategory={setCategory} />

      {error && (
        <div className="bg-destructive/15 text-destructive p-4 rounded-md">
          Failed to load channels. Please try again later.
        </div>
      )}

      <ChannelGrid channels={data?.items || []} isLoading={isLoading} />

      {data && (
        <PaginationBar
          currentPage={page}
          totalPages={data.totalPages}
          onPageChange={setPage}
        />
      )}
    </div>
  );
};