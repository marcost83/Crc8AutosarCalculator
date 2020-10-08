import argparse
from crccheck.crc import Crc8Autosar

# Parsing arguments passed
parser = argparse.ArgumentParser(description="Calculates CRC-8/Autosar")
parser.add_argument("message", help="the message to be encoded")
args = parser.parse_args()



try:
# processing CRC-8/Autosar
    data = bytearray.fromhex(args.message)
except ValueError:
    print("Provide a valid hex string")
else:
    crc = Crc8Autosar.calchex(data)
    print(crc)