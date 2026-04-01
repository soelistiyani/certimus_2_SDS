import os
from obspy import read, UTCDateTime
from config import load_config

# =============================
# FUNCTION SDS WRITER
# =============================
def write_trace_to_sds(tr, sds_root):
    net   = tr.stats.network
    sta   = tr.stats.station
    loc   = tr.stats.location if tr.stats.location else ""
    cha   = tr.stats.channel
    start = tr.stats.starttime
    end   = tr.stats.endtime

    current_time = UTCDateTime(start.date)
    while current_time <= end:
        year = current_time.year
        doy  = current_time.julday

        day_start = UTCDateTime(year=year, julday=doy)
        day_end   = day_start + 86400
        tr_day    = tr.copy().trim(day_start, day_end, pad=False)

        if len(tr_day.data) == 0:
            current_time += 86400
            continue

        sds_path = os.path.join(sds_root, f"{year}", net, sta, f"{cha}.D")
        os.makedirs(sds_path, exist_ok=True)

        filename  = f"{net}.{sta}.{loc}.{cha}.D.{year}.{doy:03d}"
        full_path = os.path.join(sds_path, filename)

        tr_day.write(full_path, format="MSEED", append=os.path.exists(full_path))
        print(f"Written: {full_path}")
        current_time += 86400

# =============================
# PROCESS FILE
# =============================
def process_file(file_path, sds_root, cfg):
    print(f"Processing: {file_path}")
    try:
        st = read(file_path)
        for tr in st:
            if cfg["new_network"]:
                tr.stats.network = cfg["new_network"]

            sta_lower = tr.stats.station.lower()
            if sta_lower in cfg["station_map"]:
                # Gunakan nama dari station_map
                tr.stats.station = cfg["station_map"][sta_lower]
            elif cfg["new_station"]:
            # Fallback: pakai new_station jika tidak ada di station_map
                tr.stats.station = cfg["new_station"]

            if cfg["force_location"] is not None:
                tr.stats.location = cfg["force_location"]

            cha_lower = tr.stats.channel.lower()
            if cha_lower in cfg["channel_map"]:
                tr.stats.channel = cfg["channel_map"][cha_lower]

            write_trace_to_sds(tr, sds_root)
    except Exception as e:
        print(f"Error: {e}")

# =============================
# BATCH LOOP
# =============================
def batch_convert(input_folder, sds_root, cfg):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith((".mseed", ".msd", ".miniseed")):
                full_path = os.path.join(root, file)
                process_file(full_path, sds_root, cfg)

# =============================
# MAIN
# =============================
if __name__ == "__main__":
    cfg = load_config("config.ini")
    batch_convert(cfg["input_folder"], cfg["sds_root"], cfg)
    print("Batch edit + conversion selesai.")