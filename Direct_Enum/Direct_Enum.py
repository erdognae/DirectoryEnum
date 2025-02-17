import requests
import sys

# Komut satırı argümanlarının kontrolü
if len(sys.argv) != 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

url = sys.argv[1]

# Dosyanın güvenli açılması ve alt dizinlerin yüklenmesi
try:
    with open("./directorylist/example.txt") as file:#Örnek liste değiştirilebilir
        directories = file.read().splitlines()
except FileNotFoundError:
    print("The file example.txt was not found.")
    sys.exit(1)

# Alt dizinlerin taranması
for dir in directories:
    dir_enum = f"https://{url}/{dir}"
    try:
        r = requests.get(dir_enum)
        if r.status_code != 404:
            print("Valid directory:", dir_enum)
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {dir_enum}")
