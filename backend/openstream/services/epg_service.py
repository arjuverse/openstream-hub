from openstream.epg.parser import EPGParser


class EPGService:

    def __init__(self, repository):
        self.repository = repository

    def import_xml(self, xml_path: str):
        parser = EPGParser(self.repository)
        parser.import_xml(xml_path)
