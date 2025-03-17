#!/usr/bin/env python3

import argparse
import csv
import importlib
import json
from models import ChannelData, ChannelEntry
from sys import exit

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--src', type=str, required=True, help='Source JSON file')
parser.add_argument('-d', '--dst', type=str, required=True, help='Destination CSV file')
parser.add_argument('-r', '--radio', type=str, required=True, help='Radio model')
parser.add_argument('-c', '--cps', type=str, required=True, help='CPS name')
args = parser.parse_args()

# Import the module for the specified radio and CPS
try:
    modulePath = f'formats.{args.radio}.{args.cps}'
    radioSettings = importlib.import_module(modulePath)
    radio = radioSettings.RadioFormat()
    print(f'Generating CSV for {radio.brand} {radio.model} for CPS {args.cps}')
except ModuleNotFoundError:
    print(f"Can't find module for type {args.radio} CPS {args.cps}")
except Exception as e:
    print(f'An error occurred loading CSV type settings: {e}')

# Build channel object from the source JSON file
with open(args.src) as sf:
  src = ChannelData(json.load(sf))

with open(args.dst, "w") as o:
  csvOut = csv.DictWriter(o, fieldnames=radio.fieldOrder)
  chanNum = 0
  csvOut.writeheader()
  for chan in src.root:
    csvOut.writerow(radio.render_row(chan, chanNum))
    chanNum += 1
