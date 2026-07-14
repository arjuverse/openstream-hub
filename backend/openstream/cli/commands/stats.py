from openstream.database.session import SessionLocal
from openstream.models.channel import Channel
from openstream.models.epg_channel import EPGChannel
from openstream.models.programme import Programme
from openstream.models.playlist import Playlist


def run():

    db = SessionLocal()

    print("\nOpenStream Hub Statistics\n")
    print("-" * 40)

    print(f"Playlists : {db.query(Playlist).count()}")
    print(f"Channels  : {db.query(Channel).count()}")
    print(f"EPG Ch.   : {db.query(EPGChannel).count()}")
    print(f"Programs  : {db.query(Programme).count()}")

    matched = (
        db.query(Channel)
        .filter(Channel.epg_channel_id.isnot(None))
        .count()
    )

    total = db.query(Channel).count()

    percent = (matched / total * 100) if total else 0

    print(f"Matched   : {matched}/{total} ({percent:.2f}%)")

    db.close()
