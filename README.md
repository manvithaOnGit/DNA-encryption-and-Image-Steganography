# DNA-encryption-and-Image-Steganography

This project explores a novel approach to data security by combining DNA codon encryption with image steganography. Inspired by the way genetic information is stored and transmitted in biological systems, this method maps plaintext into codon sequences (triplets of nucleotides) and embeds them within digital images for secure transmission.

🔑 *Key Features*

DNA Codon Encryption: Text is converted into codon sequences (A, T, C, G) for biologically inspired encryption.

Image Steganography: Encoded DNA codons are embedded inside images without noticeable visual distortion.

Dual-Layer Security: Even if the image is intercepted, the hidden codon sequences require decryption.

Encode & Decode Modules: Scripts to encode plaintext → codons → stego-image and decode stego-image → codons → plaintext.

Upgradeable Design: Can be extended with quantum key distribution (QKD) or IoT hardware interfaces (ESP32 + OLED) in future versions.

🛠️ *Tech Stack*

Languages: Python (for core encryption + steganography)

Libraries: NumPy, OpenCV/PIL, etc.

Future Hardware: ESP32 + SSD1306 OLED for key generation/display


🚀 *How It Works*

Input Text → converted into DNA codon sequence.

Codon sequence is embedded inside an image file (PNG/JPEG).

Decoder extracts codons and translates back to original text.

🎯 *Applications*

Secure communication in biomedical data transfer

Digital watermarking and anti-piracy

Defense/security for sensitive transmissions

IoT devices where lightweight, layered encryption is required

📌 *Roadmap / Next Steps*
 Add GUI for easy encryption/decryption
 
 ESP32 + OLED integration for key exchange
 
 Explore Quantum Key Distribution (QKD) for encryption key security
 
 Publish detailed documentation & diagrams
