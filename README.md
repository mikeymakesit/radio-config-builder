# Radio Config Builder

There's a broad range of software for programming amateur radios.  This project
is my attempt to only manage a single primary list of channels, and generate
configs for different radio and customer programming software (CPS)
combinations.

Compatible radios and CPS are in the `formats` folder.

## Set up

```bash
python3 -m venv .venv
. .venv/bin/activate
pip3 install -U pip
pip3 install -Ur requirements.txt
```

## Create channels as JSON

Edit the template `channels.json`.

## Generate

```bash
./build-config.py -h
usage: build-config.py [-h] -s SRC -d DST -r RADIO -c CPS

options:
  -h, --help         show this help message and exit
  -s, --src SRC      Source JSON file
  -d, --dst DST      Destination CSV file
  -r, --radio RADIO  Radio model
  -c, --cps CPS      CPS name

./build-config.py -s channels.json -d thd-75.csv -r thd75 -c rtsystems
Generating CSV for Kenwood TH-D75 for CPS rtsystems
```
