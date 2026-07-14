import { useChannels } from "../hooks/useChannels";

export default function Home() {
  const query = useChannels();

  console.log(query);

  if (query.isPending) {
    return <h2>Loading...</h2>;
  }

  if (query.error) {
    return (
      <pre style={{ color: "red" }}>
        {JSON.stringify(query.error, null, 2)}
      </pre>
    );
  }

  return (
    <div>
      <h1>OpenStream Hub</h1>

      <h2>Total: {query.data.total}</h2>

      <pre>{JSON.stringify(query.data.items[0], null, 2)}</pre>
    </div>
  );
}
