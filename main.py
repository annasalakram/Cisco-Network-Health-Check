import os
import json
from datetime import datetime
from dotenv import load_dotenv
from napalm import get_network_driver

# 1. Load kredensial
load_dotenv()

def run_health_check():
    driver = get_network_driver('iosxr')
    
    # Inisialisasi variabel device agar tidak error saat close()
    device = None
    
    try:
        # Konfigurasi perangkat dengan timeout ditingkatkan (30 detik)
        device = driver(
            hostname=os.getenv('DEV_HOST'),
            username=os.getenv('DEV_USER'),
            password=os.getenv('DEV_PASS'),
            optional_args={
                'port': int(os.getenv('DEV_PORT')),
                'conn_timeout': 30,  # Solusi untuk 'No existing session'
                'global_delay_factor': 2
            }
        )

        print(f"[*] Mencoba menghubungi {os.getenv('DEV_HOST')} pada port {os.getenv('DEV_PORT')}...")
        
        # Buka koneksi
        device.open()
        print("[+] Koneksi berhasil! Mengambil data...")

        # Mengambil data via CLI
        commands = ['show version', 'show ipv4 interface brief']
        output = device.cli(commands)

        # Menyusun laporan
        report_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "host": os.getenv('DEV_HOST'),
            "data": output
        }

        # Simpan ke file JSON
        with open('health_report.json', 'w') as f:
            json.dump(report_data, f, indent=4)
        
        print("[+] Laporan berhasil disimpan di 'health_report.json'")

    except Exception as e:
        print(f"\n[!] GAGAL KONEKSI: {e}")
        print("-" * 50)
        print("TIPS TROUBLESHOOTING:")
        print("1. Pastikan VPN (Cloudflare WARP) dalam posisi CONNECTED.")
        print("2. Cek apakah Hostname di .env sudah benar untuk IOS-XR.")
        print("3. Jika port 22 gagal, coba ganti ke 57722 di file .env.")
        print("4. Tunggu 5 menit, mungkin Sandbox sedang proses booting.")
        print("-" * 50)

    finally:
        # Cek apakah device sudah dibuat dan koneksi terbuka sebelum ditutup
        if device is not None:
            try:
                device.close()
                print("[*] Sesi diakhiri secara bersih.")
            except:
                # Menghindari AttributeError 'IOSXR' has no attribute 'device'
                pass

if __name__ == "__main__":
    run_health_check()