from pathlib import Path
import gzip
import lzma
import shutil

import requests


class EPGDownloader:
    def __init__(self, download_dir: str = "data/epg"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)

    def download(self, url: str) -> Path:
        filename = url.split("/")[-1]

        filepath = self.download_dir / filename

        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        return self.extract(filepath)

    def extract(self, filepath: Path) -> Path:

        if filepath.suffix == ".gz":

            xml_path = filepath.with_suffix("")

            with gzip.open(filepath, "rb") as src:
                with open(xml_path, "wb") as dst:
                    shutil.copyfileobj(src, dst)

            return xml_path

        if filepath.suffix == ".xz":

            xml_path = filepath.with_suffix("")

            with lzma.open(filepath, "rb") as src:
                with open(xml_path, "wb") as dst:
                    shutil.copyfileobj(src, dst)

            return xml_path

        return filepath

