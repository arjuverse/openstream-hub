import { useChannels } from "@/hooks/useChannels";

export default function Dashboard() {
  const { data, isPending, error } = useChannels();

  if (isPending) {
    return <div className="p-8">Loading...</div>;
  }

  if (error) {
    console.error(error);

    return (
      <div className="p-8">
        <h1 className="text-2xl font-bold text-red-600">
          Backend Error
        </h1>

        <pre>{JSON.stringify(error, null, 2)}</pre>
      </div>
    );
  }

  return (
    <div className="space-y-6 p-8">
      <h1 className="text-3xl font-bold">
        OpenStream Hub
      </h1>

      <div>Total channels: {data?.total}</div>

      <div>Current page: {data?.page}</div>

      <div>Page size: {data?.size}</div>

      <div>Loaded: {data?.items.length}</div>

      <hr />

      <div className="space-y-2">
        {data?.items.slice(0, 10).map((channel) => (
          <div
            key={channel.id}
            className="rounded border p-3"
          >
            <div className="font-semibold">{channel.name}</div>

            <div className="text-sm text-gray-500">
              {channel.group_title}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}