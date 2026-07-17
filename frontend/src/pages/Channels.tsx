import { useState } from "react";
import { useChannels } from "@/hooks/useChannels";
import { useCategories } from "@/hooks/useCategories";
import { useDebounce } from "@/hooks/useDebounce";

import ChannelGrid from "@/components/channels/ChannelGrid";
import CategoryFilter from "@/components/channels/CategoryFilter";
import PaginationBar from "@/components/channels/PaginationBar";
import { RecentChannelsRow } from "@/components/RecentChannelsRow"; // Added import

export default function Channels() {
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState("");
  const debouncedSearch = useDebounce(search, 300);
  const [category, setCategory] = useState("All");

  const { data, isPending, error } = useChannels({
    page,
    size: 24,
    search: debouncedSearch,
    category: category === "All" ? undefined : category,
    sort: "name",
    order: "asc",
  });

  const { data: categoriesData } = useCategories();

  if (isPending) {
    return <div className="p-8">Loading channels...</div>;
  }

  if (error || !data) {
    return (
      <div className="p-8 text-red-600">
        Failed to load channels.
      </div>
    );
  }

  const categories = [
    "All",
    ...(categoriesData ?? []),
  ];

  const totalPages =
    data.total_pages ?? Math.ceil(data.total / 24);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">
          Channels
        </h1>

        <p className="mt-1 text-zinc-500">
          Showing {data.items.length} of{" "}
          {data.total.toLocaleString()} channels
        </p>
      </div>

      {/* Inserted the Recent Channels Row here */}
      <RecentChannelsRow />

      <input
        type="text"
        value={search}
        onChange={(e) => {
          setSearch(e.target.value);
          setPage(1);
        }}
        placeholder="🔍 Search channels..."
        className="w-full rounded-xl border border-zinc-300 bg-white px-4 py-3 shadow-sm outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-200 dark:border-zinc-700 dark:bg-zinc-900"
      />

      <CategoryFilter
        categories={categories}
        selected={category}
        onSelect={(value) => {
          setCategory(value);
          setPage(1);
        }}
      />

      <ChannelGrid channels={data.items} />

      <PaginationBar
        page={page}
        totalPages={totalPages}
        onPageChange={setPage}
      />
    </div>
  );
}