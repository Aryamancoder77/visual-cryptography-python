# visual-cryptography-python
Author - Aryaman baliyan
# 🔐 Visual Cryptography (2-out-of-2 Scheme)

This project implements a 2-out-of-2 Visual Cryptography scheme where a secret image is split into two noise-like shares. Individually, shares reveal nothing. When combined, the original image appears.

## 📌 Concept

Visual Cryptography was introduced by Moni Naor and Adi Shamir (1984). It allows image-based secret sharing without requiring decryption algorithms.

## ⚙️ Tech Stack

- Python
- OpenCV
- NumPy

## 🚀 How It Works

1. Convert input image to binary
2. Generate two random shares
3. Each share looks like random noise
4. Overlay shares to reconstruct image

## 📂 Project Structure

visual-cryptography/
│
├── vc.py
├── input/
├── output/

## ▶️ Run the Project

```bash
pip install -r requirements.txt
python vc.py
