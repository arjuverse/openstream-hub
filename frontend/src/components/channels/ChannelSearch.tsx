import { Search } from "lucide-react";

interface ChannelSearchProps {
  value: string;
  onChange: (value: string) => void;
}

export default function ChannelSearch({
  value,
  onChange,
}: ChannelSearchProps) {
  return (
    <div className="relative w-full">
      <Search
        size={18}
        className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
      />

      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Search channels..."
        className="w-full rounded-lg border border-gray-300 bg-white py-3 pl-10 pr-4 shadow-sm focus:border-blue-500 focus:outline-none"
      />
    </div>
  );
}