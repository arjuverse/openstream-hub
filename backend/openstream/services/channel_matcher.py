from rapidfuzz import fuzz

from openstream.epg.utils import normalize_channel_name
from openstream.models.channel import Channel
from openstream.models.epg_channel import EPGChannel


class ChannelMatcher:

    FUZZY_THRESHOLD = 94

    def __init__(self, repository):
        self.repository = repository

    def match(self):

        db = self.repository.db

        channels = db.query(Channel).all()
        epg_channels = db.query(EPGChannel).all()

        # ---------------------------------------------------------
        # Build lookup dictionaries
        # ---------------------------------------------------------

        exact_lookup = {}

        normalized_epg = []

        for epg in epg_channels:

            norm = normalize_channel_name(epg.display_name)

            exact_lookup[norm] = epg

            normalized_epg.append(
                (
                    norm,
                    epg,
                )
            )

        matched = 0

        for channel in channels:

            name = normalize_channel_name(channel.name)

            if not name:
                continue

            match = None

            # =====================================================
            # STEP 1
            # Exact normalized match
            # =====================================================

            if name in exact_lookup:

                match = exact_lookup[name]

            # =====================================================
            # STEP 2
            # Contains match
            # =====================================================

            if match is None:

                for norm, epg in normalized_epg:

                    if len(norm) < 5:
                        continue

                    if norm in name or name in norm:

                        match = epg
                        break

            # =====================================================
            # STEP 3
            # RapidFuzz fallback
            # =====================================================

            if match is None:

                best = None
                best_score = 0
                second_score = 0

                for norm, epg in normalized_epg:

                    score = fuzz.token_set_ratio(name, norm)

                    if score > best_score:

                        second_score = best_score
                        best_score = score
                        best = epg

                    elif score > second_score:

                        second_score = score

                if (
                    best is not None
                    and best_score >= self.FUZZY_THRESHOLD
                    and (best_score - second_score) >= 8
                ):
                    match = best

            # =====================================================
            # Save match
            # =====================================================

            if match is not None:

                channel.epg_channel_id = match.id
                matched += 1

        db.commit()

        print(f"\nMatched {matched} channels")

        return matched