from openstream.repositories.metadata_repository import MetadataRepository


class MetadataService:
    def __init__(self, repository: MetadataRepository):
        self.repository = repository

    def stats(self):
        return self.repository.get_stats()

    def categories(self):
        return self.repository.get_categories()

    def countries(self):
        return self.repository.get_countries()

    def languages(self):
        return self.repository.get_languages()