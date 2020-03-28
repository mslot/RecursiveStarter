import toml
import glob
import os

settings = None

with open("config/settings.toml", encoding="utf-8") as settings_file:
    content = settings_file.read()
    settings = toml.loads(content)

sln_files = glob.glob("./**/*.sln",recursive=True)

os.system("start " + sln_files[0])