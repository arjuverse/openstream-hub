from datetime import datetime
from xml.etree.ElementTree import iterparse

from sqlalchemy.orm import Session

from openstream.models.epg_channel import EPGChannel
from openstream.models.programme import Programme


class EPGParser:
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def parse_datetime(value: str) -> datetime:
        value = value.split()[0]
        return datetime.strptime(value, "%Y%m%d%H%M%S")

    def import_xml(self, xml_path: str):

        channel_map = {}

        context = iterparse(xml_path, events=("end",))

        for event, elem in context:

            if elem.tag == "channel":

                epg_id = elem.attrib["id"]

                display = elem.findtext("display-name", default=epg_id)

                icon = None

                icon_elem = elem.find("icon")

                if icon_elem is not None:
                    icon = icon_elem.attrib.get("src")

                channel = EPGChannel(
                    epg_id=epg_id,
                    display_name=display,
                    icon=icon,
                )

                self.db.add(channel)
                self.db.flush()

                channel_map[epg_id] = channel.id

                elem.clear()

            elif elem.tag == "programme":

                epg_id = elem.attrib.get("channel")

                if epg_id not in channel_map:
                    elem.clear()
                    continue

                programme = Programme(
                    epg_channel_id=channel_map[epg_id],
                    title=elem.findtext("title", ""),
                    description=elem.findtext("desc"),
                    category=elem.findtext("category"),
                    start_time=self.parse_datetime(elem.attrib["start"]),
                    stop_time=self.parse_datetime(elem.attrib["stop"]),
                )

                self.db.add(programme)

                elem.clear()

        self.db.commit()
