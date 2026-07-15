export interface Channel {
  id: number;
  name: string;
  stream_url: string;
  tvg_id: string | null;
  tvg_name: string | null;
  logo_url: string | null;
  group_title: string | null;
  category: string | null;
  country: string | null;
  language: string | null;
  playlist_id: number;
  epg_channel_id: number | null;
}

export interface PaginatedChannels {
  items: Channel[];
  total: number;
  page: number;
  size: number;
}