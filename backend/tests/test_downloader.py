from openstream.services.downloader import download_playlist


def test_download_playlist():
    content = download_playlist("https://iptv-org.github.io/iptv/index.m3u")

    assert "#EXTM3U" in content
    assert len(content) > 1000
