# certimus_2_SDS
Mengkonversi data seismik berformat MiniSEED dari Guralp Certimus ke dalam format MiniSEED struktur SDS.

Penggunaan:

    python convert.py

File konfigurasi di config.ini: 
    [paths]
    input_folder = D:\Lewotolok\mseed
    sds_root = SDS

    [header]
    new_network = VG
    new_station = 
    force_location = 00

    [station_map]
    005A69 = IBTB
    005869 = IBKC
    ; 00665 = ANYR

    [channel_map]
    SHZ = HHZ
    SHN = HHN
    SHE = HHE




Struktur SDS:

    <SDS_ROOT>/<YEAR>/<NET>/<STA>/<CHA.D>/<NET.STA.LOC.CHA.D.YEAR.DOY>
