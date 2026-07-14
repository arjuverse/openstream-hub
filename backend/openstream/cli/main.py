import argparse

from openstream.database.session import SessionLocal
from openstream.repositories.channel_repository import ChannelRepository
from openstream.services.channel_matcher import ChannelMatcher
from openstream.services.epg_downloader import EPGDownloader
from openstream.services.epg_manager import EPGManager


def stats():
    db = SessionLocal()

    try:
        from openstream.models.channel import Channel
        from openstream.models.epg_channel import EPGChannel
        from openstream.models.programme import Programme
        from openstream.models.playlist import Playlist

        playlists = db.query(Playlist).count()
        channels = db.query(Channel).count()
        epg_channels = db.query(EPGChannel).count()
        programmes = db.query(Programme).count()

        matched = (
            db.query(Channel)
            .filter(Channel.epg_channel_id.is_not(None))
            .count()
        )

        percentage = (
            (matched / channels) * 100
            if channels
            else 0
        )

        print("\nOpenStream Hub Statistics\n")
        print("----------------------------------------")
        print(f"Playlists : {playlists}")
        print(f"Channels  : {channels}")
        print(f"EPG Ch.   : {epg_channels}")
        print(f"Programs  : {programmes}")
        print(f"Matched   : {matched}/{channels} ({percentage:.2f}%)")

    finally:
        db.close()


def import_epg():
    db = SessionLocal()

    try:
        manager = EPGManager(db)
        manager.import_all()
    finally:
        db.close()


def match():
    db = SessionLocal()

    try:
        matcher = ChannelMatcher(
            ChannelRepository(db)
        )

        matched = matcher.match()

        print(f"\nMatched {matched} channels")

    finally:
        db.close()


def download_epg():
    downloader = EPGDownloader()
    downloader.download_all()


def main():
    parser = argparse.ArgumentParser(
        prog="openstream",
        description="OpenStream Hub CLI",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    subparsers.add_parser(
        "stats",
        help="Show database statistics",
    )

    subparsers.add_parser(
        "import-epg",
        help="Import XMLTV files",
    )

    subparsers.add_parser(
        "match",
        help="Match IPTV channels with EPG",
    )

    subparsers.add_parser(
        "download-epg",
        help="Download XMLTV files",
    )

    args = parser.parse_args()

    if args.command == "stats":
        stats()

    elif args.command == "import-epg":
        import_epg()

    elif args.command == "match":
        match()

    elif args.command == "download-epg":
        download_epg()


if __name__ == "__main__":
    main()