import argparse
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument("--listfiles", help="Lists specific files within the directory.")
parser.add_argument("--long", help="Lists all files within the directory.")
args = parser.parse_args()

if args.listfiles:
        listed_files = [f for f in glob.glob("*.py")]
        print(listed_files)

if args.long:
        listed_files = os.listdir()
        print(listed_files)