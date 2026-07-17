from math import ceil

from openstream.repositories.channel_repository import ChannelRepository


class ChannelService:
    def __init__(
        self,
        repository: ChannelRepository,
    ):
        self.repository = repository

    def get(
        self,
        channel_id: int,
    ):
        return self.repository.get(channel_id)

    def get_categories(self) -> list[str]:
        return self.repository.get_categories()

    def get_channels(
        self,
        page: int,
        size: int,
        search: str | None = None,
        group: str | None = None,
        category: str | None = None,
        matched: bool | None = None,
        sort: str = "name",
        order: str = "asc",
    ):
        items, total = self.repository.get_channels(
            page=page,
            size=size,
            search=search,
            group=group,
            category=category,
            matched=matched,
            sort=sort,
            order=order,
        )

        return {
            "items": items,
            "page": page,
            "size": size,
            "total": total,
            "total_pages": ceil(total / size),
        }