import urllib.request

from environs import Env

env = Env()

GS_FILE = "./backend/settings/acrsdsdsed.json"

url = env("GS_FILE_URL")
file = urllib.request.urlopen(url).read().decode('utf-8')
f = open(GS_FILE, "w+")
f.write(file)
f.close()

print("Done Creating file!")
