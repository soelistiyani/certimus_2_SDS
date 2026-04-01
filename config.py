import configparser
import os

def load_config(config_path="config.ini"):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"File konfigurasi tidak ditemukan: {config_path}")
    
    config = configparser.ConfigParser()
    config.read(config_path)

    return {
        "input_folder":  config.get("paths", "input_folder"),
        "sds_root":      config.get("paths", "sds_root"),
        "new_network":   config.get("header", "new_network", fallback=None) or None,
        "new_station":   config.get("header", "new_station", fallback=None) or None,
        "force_location":config.get("header", "force_location", fallback=None) or None,
        "station_map":   dict(config.items("station_map")) if config.has_section("station_map") else {},
        "channel_map":   dict(config.items("channel_map")) if config.has_section("channel_map") else {},
    }