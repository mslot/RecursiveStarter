import glob
import os

sln_files = glob.glob("./**/*.sln",recursive=True)

os.system("start " + sln_files[0])