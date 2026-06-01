import socket
import urllib.request
import json
import whois
import dns.resolver
import nmap

domain = input("Введите домен (example.com): ")

print("\n==============================")
print("🔍 OSINT ANALYSIS")
print("==============================")

# IP
ip = socket.gethostbyname(domain)
print(f"\n🌐 IP: {ip}")

# Geo + ISP (без requests)
try:
    url = f"http://ip-api.com/json/{ip}"
    with urllib.request.urlopen(url) as response:
        geo = json.loads(response.read().decode())

    if geo["status"] == "success":
        print(f"🏳 Страна: {geo['country']}")
        print(f"🏙 Город: {geo['city']}") 
        print(f"🏢 Провайдер: {geo['isp']}")
        print(f"📡 ASN: {geo['as']}")
except:
    print("Не удалось получить Geo данные")

# Server headers
try:
    req = urllib.request.Request(f"http://{domain}")
    with urllib.request.urlopen(req, timeout=5) as response:
        server = response.headers.get("Server", "Unknown")
except:
    server = "Unknown"

print(f"\n🖥 Server: {server}")

if "cloudflare" in server.lower():
    print("☁ Cloudflare: YES")
else:
    print("☁ Cloudflare: NO / UNKNOWN")

# WHOIS
print("\n📄 WHOIS:")
try:
    w = whois.whois(domain)
    print(f"Регистратор: {w.registrar}")
    print(f"Организация: {w.org}")
    print(f"Дата создания: {w.creation_date}")
    print(f"Истекает: {w.expiration_date}")
except:
    print("WHOIS недоступен")

# DNS
print("\n🔧 DNS:")
for r in ["A", "NS", "MX", "TXT"]:
    try:
        answers = dns.resolver.resolve(domain, r)
        print(f"{r}:")
        for a in answers:
            print(" ", a)
    except:
        pass

# Port Scan
print("\n🚪 Port scan:")
try:
    scanner = nmap.PortScanner()
    scanner.scan(ip, "21,22,25,80,443,3306,8080")

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                state = scanner[host][proto][port]["state"]
                print(f"Port {port}: {state}")
except:
    print("Nmap scan failed")

# Save
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"Domain: {domain}\nIP: {ip}\nServer: {server}\n")

print("\n💾 Результат сохранён в result.txt")
