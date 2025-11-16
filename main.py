patchname = "make spwn strings funi!!!"
patchdata = [
    (b"\x72\xE2\x37", b"wirtting tu levl:"),
    (b"\x72\xCF\xF3", b"\x77\x69\x72"),
    (b"\x72\xCF\xFC", b"\x75"),
    (b"\x72\xCF\xFF", b"\x65\x69\x76"),
    (b"\x72\xD0\x04", b"\x79"),
    (b"\x72\xD0\x0D", b"\x61\x75"),
    (b"\x72\xD0\x11", b"\x68\x70\x6E"),
    (b"\x72\xD0\x15", b"\x67"),
    (b"\x72\xD0\x19", b"\x69"),
    (b"\x72\xD0\x1C", b"\x69"),
    (b"\x72\xD0\x1E", b"\x64"),
    (b"\x72\xD0\x20", b"\x68\x73"),
    (b"\x72\xD0\x25", b"\x65\x6E\x21"),
]

data = b"PATCH" # Header
data += patchname.encode("utf-8") + b"\x00" # Patch Name + EOL

for addr, content in patchdata:
    data += addr # Packet Address
    data += bytes([len(content)]) # Packet Data Length
    data += content # Packet Data

with open("patch.ips", "wb") as f:
    f.write(data)

print("Wrote " + str(len(data)) + " bytes to patch.ips")