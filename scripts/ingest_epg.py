import sys
import os
import xml.etree.ElementTree as ET
from datetime import datetime

# Force Python to add the BACKEND directory to the path
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Now it will correctly find openstream inside the backend folder
from sqlalchemy.orm import Session
from openstream.database.session import SessionLocal
from openstream.models.epg_channel import EPGChannel
from openstream.models.programme import Programme
from openstream.models.channel import Channel

def parse_xmltv_time(time_str: str) -> datetime:
    """Converts XMLTV time string (e.g., '20260611120000 +0000') to a Python datetime object."""
    try:
        dt_str = time_str.split(" ")[0]
        return datetime.strptime(dt_str, "%Y%m%d%H%M%S")
    except Exception:
        return datetime.utcnow()

def ingest_xmltv(file_path: str, source_id: int = 1):
    db: Session = SessionLocal()
    
    print(f"Loading XMLTV file: {file_path}")
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Failed to parse XML: {e}")
        return
    EPGChannel.metadata.create_all(bind=db.get_bind())
    Programme.metadata.create_all(bind=db.get_bind())


    print("Processing EPG channels...")
    channel_map = {} 
    
    for channel_elem in root.findall("channel"):
        epg_id = channel_elem.get("id")
        if not epg_id:
            continue
            
        display_name = channel_elem.findtext("display-name") or epg_id
        icon_elem = channel_elem.find("icon")
        icon_url = icon_elem.get("src") if icon_elem is not None else None

        channel_record = db.query(EPGChannel).filter(EPGChannel.epg_id == epg_id).first()
        
        if not channel_record:
            channel_record = EPGChannel(
                epg_id=epg_id,
                display_name=display_name,
                icon=icon_url,
                source_id=source_id 
            )
            db.add(channel_record)
            db.commit()
            db.refresh(channel_record)
            
        channel_map[epg_id] = channel_record.id

    print("Processing EPG programmes...")
    programmes_to_insert = []
    
    for prog_elem in root.findall("programme"):
        epg_id = prog_elem.get("channel")
        
        if epg_id not in channel_map:
            continue
            
        title = prog_elem.findtext("title") or "Unknown Program"
        desc = prog_elem.findtext("desc")
        category = prog_elem.findtext("category")
        
        start_time = parse_xmltv_time(prog_elem.get("start", ""))
        stop_time = parse_xmltv_time(prog_elem.get("stop", ""))

        programmes_to_insert.append(
            Programme(
                epg_channel_id=channel_map[epg_id],
                title=title,
                description=desc,
                category=category,
                start_time=start_time,
                stop_time=stop_time
            )
        )

    if programmes_to_insert:
        print("Clearing old programmes...")
        db.query(Programme).delete()
        
        print(f"Inserting {len(programmes_to_insert)} new programmes...")
        db.bulk_save_objects(programmes_to_insert)
        db.commit()
        
    print("EPG ingestion complete!")
    db.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/ingest_epg.py <path_to_xmltv_file>")
        sys.exit(1)
        
    xml_path = sys.argv[1]
    ingest_xmltv(xml_path)