from openstream.database.session import SessionLocal
from openstream.repositories.channel_repository import ChannelRepository
from openstream.services.channel_matcher import ChannelMatcher


def run():

    db = SessionLocal()

    matcher = ChannelMatcher(
        ChannelRepository(db)
    )

    matcher.match()

    db.commit()

    db.close()
