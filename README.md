# 🔐 Breaking Enigma: Simulating Historical Cryptosystems

This project is a Python-based graphical simulation of the **Enigma Machine**, the infamous cipher device used by Nazi Germany during World War II. Alongside the simulation, the project demonstrates basic cryptanalysis techniques historically used to crack Enigma-encrypted messages.

---

## 📜 Table of Contents

- [About The Project](#about-the-project)
- [How The Enigma Machine Works](#how-the-enigma-machine-works)
- [Cracking The Enigma](#cracking-the-enigma)
- [Project Features](#project-features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributors](#contributors)

---

## 📖 About The Project

A historical simulation that mimics the **rotor-based encryption process of the Enigma Machine**. This project was developed as part of our **Information Security** coursework.

We also recreated simple cryptanalysis techniques used by **Alan Turing and his team at Bletchley Park** to demonstrate how weaknesses in the Enigma system could be exploited.

---

## ⚙️ How The Enigma Machine Works

- **Rotors:** Substitute letters based on internal wirings and their positions.
- **Reflector:** Sends the signal back through the rotors.
- **Plugboard:** Swaps pairs of letters before and after the rotors.
- **Rotor Stepping:** Changes rotor positions after each key press, making encryption dynamic.

---

## 🔓 Cracking The Enigma

Historic weaknesses:
- No letter encrypted to itself.
- Known plaintext phrases (cribs).
- Limited key space due to daily key sheets.

We simulated:
- **Known-plaintext attacks**
- **Rotor position analysis**
- **Plugboard contradiction checks**

---

## 🎛️ Project Features

- GUI-based Enigma machine simulation.
- Dynamic rotor stepping mechanism.
- Plugboard configuration.
- Real-time encryption and decryption.
- Basic statistical analysis of ciphertext.

## 🚀 Usage

1. **Make sure Python is installed** on your system.  
   Download it from [python.org](https://www.python.org/downloads/) if you don't have it.

2. You can also run this project directly in **Visual Studio Code** with the Python extension installed.

3. **To run the simulation**, open your terminal or VS Code terminal, navigate to the project directory, and type:

```bash
python Enigma.py

```

## 👥 Creators
- Muhammad Jalil Ahmad [@JalilAhmad2004]
- Umar Farooq [@0ri4x]
- Abdul Moeez Siddiqui [@Abdul-Moeez4]
