from openstream.utils.m3u_parser import parse_m3u


def test_parse_simple_playlist():
    playlist = """
#EXTM3U

#EXTINF:-1 tvg-id="bbc" group-title="News",BBC News
https://example.com/bbc.m3u8

#EXTINF:-1 tvg-id="cnn" group-title="News",CNN
https://example.com/cnn.m3u8
"""

    channels = parse_m3u(playlist)

    assert len(channels) == 2

    assert channels[0]["name"] == "BBC News"
    assert channels[0]["tvg-id"] == "bbc"
    assert channels[0]["group-title"] == "News"
    assert channels[0]["stream_url"] == "https://example.com/bbc.m3u8"

    assert channels[1]["name"] == "CNN"
