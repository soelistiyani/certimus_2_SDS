# certimus_2_SDS
Mengkonversi data seismik berformat MiniSEED dari Guralp Certimus ke dalam format MiniSEED struktur SDS.

Penggunaan:

    python convert.py

Format File dari Certimus: 
    SerialNumber_SensornumberTipedataChannelA_______00SamplingRate_Number.mseed
    005869_S1SeisZA_______00100_00012.mseed

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

Keterangan:
[paths]
Input_folder: berisi direktori data mseed yang dicopy dari Certimus
Sds_root: folder output untuk data format SDS

[header]
New_network: untuk data PVMBG menggunakan network VG
New_station: jika hanya konversi 1 stasiun, maka wajib diisi dengan nama stasiun. Jika konversi lebih dari 1 stasiun maka kosongkan parameter ini, namun station mapping harus diisi. 
force_location: untuk data PVMBG secara default locationnya 00 kecuali jika ada perubahan lokasi sensor/perubahan sensor. 

[station_map]
004E69 = TDNR (serial number = nama stasiun baru)
; 00665 = ANYR tanda ; artinya tidak dibaca

[station_map]
SHZ = HHZ     → mapping komponen SHZ ke HHZ, dst
SHN = HHN
SHE = HHE


Output Struktur SDS:

    <SDS_ROOT>/<YEAR>/<NET>/<STA>/<CHA.D>/<NET.STA.LOC.CHA.D.YEAR.DOY>
