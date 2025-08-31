#!/usr/bin/env python3
# stego_image.py
# Hide and extract DNA codons inside PNG images using LSB steganography.

from PIL import Image
import sys
from codons import text_to_codons, codons_to_text, set_key

def encode_image(infile, outfile, text, password=""):
    set_key(password)
    codons = text_to_codons(text)
    data = " ".join(codons).encode("utf-8")
    bits = ''.join(f"{b:08b}" for b in data)
    length = len(bits)

    img = Image.open(infile).convert("RGB")
    pixels = list(img.getdata())
    cap = len(pixels) * 3
    if length > cap:
        raise ValueError("Message too long for this image.")

    # Embed bits
    new_pixels = []
    idx = 0
    for r,g,b in pixels:
        rgb = [r,g,b]
        for c in range(3):
            if idx < length:
                rgb[c] = (rgb[c] & ~1) | int(bits[idx])
                idx += 1
        new_pixels.append(tuple(rgb))
    img.putdata(new_pixels)
    img.save(outfile)
    print(f"Encoded {len(codons)} codons into {outfile}")

def decode_image(infile, password=""):
    set_key(password)
    img = Image.open(infile).convert("RGB")
    pixels = list(img.getdata())
    bits = ""
    for r,g,b in pixels:
        bits += str(r & 1)
        bits += str(g & 1)
        bits += str(b & 1)
    # Rebuild bytes until we hit valid utf-8 codons string
    by = []
    for i in range(0, len(bits), 8):
        byte = int(bits[i:i+8], 2)
        by.append(byte)
        try:
            s = bytes(by).decode("utf-8")
            if all(x in "ATGC \n" for x in s.strip()):
                codons = s.split()
                return codons, codons_to_text(codons)
        except:
            pass
    return None, None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Encode: python stego_image.py encode cover.png stego.png 'Message' [password]")
        print("  Decode: python stego_image.py decode stego.png [password]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "encode":
        infile, outfile, text = sys.argv[2], sys.argv[3], sys.argv[4]
        pwd = sys.argv[5] if len(sys.argv) > 5 else ""
        encode_image(infile, outfile, text, pwd)
    elif cmd == "decode":
        infile = sys.argv[2]
        pwd = sys.argv[3] if len(sys.argv) > 3 else ""
        codons, msg = decode_image(infile, pwd)
        if codons:
            print("Codons:", " ".join(codons))
            print("Message:", msg)
        else:
            print("Decode failed.")
