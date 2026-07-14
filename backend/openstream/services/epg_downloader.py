from pathlib import Path
import gzip
import shutil
import requests

from openstream.database.session import SessionLocal
from openstream.models.epg_source import EPGSource


class EPGDownloader:
    def __init__(self):
        self.db = SessionLocal()

    def download_all(self):

        sources = (
            self.db.query(EPGSource)
            .filter(EPGSource.enabled == True)
            .all()
        )

        Path("data/epg").mkdir(parents=True, exist_ok=True)

        for source in sources:

            print(f"\nDownloading {source.name}")

            filename = f"{source.name.lower()}.xml"

            outfile = Path("data/epg") / filename

            r = requests.get(source.url, stream=True, timeout=120)

            r.raise_for_status()

            if source.url.endswith(".gz"):

                gzfile = outfile.with_suffix(".xml.gz")

                with open(gzfile, "wb") as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)

                with gzip.open(gzfile, "rb") as fin:
                    with open(outfile, "wb") as fout:
                        shutil.copyfileobj(fin, fout)

                gzfile.unlink()

            else:

                with open(outfile, "wb") as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)

            print("Saved:", outfile)

        print("\nFinished.")