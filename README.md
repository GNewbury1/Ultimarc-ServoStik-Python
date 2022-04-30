# Ultimarc ServoStik Python

This is a small script that allows setting the ServoStik to either 4-way or 8-way control. This was created as the current solutions seem unable to handle **multiple** ServoStiks. This script has been tested when there were two control boards connected.

## Usage

If you haven't already, you need to install the `pyusb` module. This can be done as:

```bash
$ pip3 install pyusb
```

The script itself is very simple. Run it like so:

```bash
# Set to 4-way control
$ python3 servo_stik.py 4
# Set to 8-way control
$ python3 servo_stik.py 8
```