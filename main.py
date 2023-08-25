import webbrowser
import requests

print("Let us visit an old website")

site = input("type in the website URL? ")
era = input("type the year, month and day like 20151128: ")
url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"

response = requests.get(url)
response.raise_for_status()
data = response.json()
print(data)

try:
  old_site = data["achived_snapshots"]["closests"]["url"]
  print("This is the site" , old_site)
  print("this should appear in your webbrowser")
  webbrowser.open(old_site)
except:
  print("Sorry your website was not found")
