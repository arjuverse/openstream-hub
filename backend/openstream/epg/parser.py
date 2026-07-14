from xml.etree.ElementTree import iterparse

from openstream.epg.utils import (
    normalize_channel_name,
    parse_xmltv_datetime,
)
from openstream.models.epg_channel import EPGChannel


class EPGParser:
    PROGRAMME_BATCH_SIZE = 5000

    def __init__(self, repository):
        self.repository = repository

    def import_xml(self, xml_path: str):

        print(f"\nLoading {xml_path}\n")

        try:

            channel_map = {}
            batch = []

            imported_channels = 0
            imported_programmes = 0
            skipped_programmes = 0

            context = iterparse(xml_path, events=("end",))

            for _, elem in context:

                tag = elem.tag

                # ==========================================================
                # CHANNEL
                # ==========================================================

                if tag == "channel":

                    epg_id = elem.attrib.get("id")

                    if not epg_id:
                        elem.clear()
                        continue

                    display_name = elem.findtext(
                        "display-name",
                        default=epg_id,
                    )

                    icon = None

                    icon_elem = elem.find("icon")

                    if icon_elem is not None:
                        icon = icon_elem.attrib.get("src")

                    existing = self.repository.get_channel(epg_id)

                    if existing:

                        channel_map[epg_id] = existing.id

                    else:

                        channel = self.repository.add_channel(
                            EPGChannel(
                                epg_id=epg_id,
                                display_name=display_name,
                                icon=icon,
                            )
                        )

                        channel_map[epg_id] = channel.id
                        imported_channels += 1

                        if imported_channels % 100 == 0:
                            print(f"Channels: {imported_channels}")

                    elem.clear()
                    continue

                # ==========================================================
                # PROGRAMME
                # ==========================================================

                if tag == "programme":

                    epg_id = elem.attrib.get("channel")

                    channel_id = channel_map.get(epg_id)

                    # fallback normalization
                    if channel_id is None:

                        normalized = normalize_channel_name(epg_id)

                        for key, value in channel_map.items():

                            if normalize_channel_name(key) == normalized:
                                channel_id = value
                                break

                    if channel_id is None:
                        skipped_programmes += 1
                        elem.clear()
                        continue

                    try:

                        batch.append(
                            {
                                "epg_channel_id": channel_id,
                                "title": elem.findtext("title", ""),
                                "description": elem.findtext("desc"),
                                "category": elem.findtext("category"),
                                "episode": elem.findtext("episode-num"),
                                "rating": elem.findtext("rating/value"),
                                "start_time": parse_xmltv_datetime(
                                    elem.attrib["start"]
                                ),
                                "stop_time": parse_xmltv_datetime(
                                    elem.attrib["stop"]
                                ),
                            }
                        )

                    except Exception:
                        skipped_programmes += 1

                    if len(batch) >= self.PROGRAMME_BATCH_SIZE:

                        self.repository.bulk_insert_programmes(batch)

                        imported_programmes += len(batch)

                        print(
                            f"Programmes: {imported_programmes}"
                        )

                        batch.clear()

                    elem.clear()

            # Insert remaining programmes

            if batch:

                self.repository.bulk_insert_programmes(batch)

                imported_programmes += len(batch)

            self.repository.commit()

            print()
            print("=" * 60)
            print(f"Channels imported   : {imported_channels}")
            print(f"Programmes imported : {imported_programmes}")
            print(f"Skipped programmes  : {skipped_programmes}")
            print("=" * 60)

        except Exception:

            self.repository.rollback()
            raise
            