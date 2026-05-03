# SPHY Symbiotic Audit System

**Download the Official Audit Dataset:**  
[**SPHY Audit Data (Google Drive)**](https://drive.google.com/file/d/16jszUGKVjTcJCzXSccQxsVcJdao0Dc6u/view?usp=sharing)

---

This repository contains the core tools for the **SPHY (Symbiotic Phase Harmonic Yielding)** framework, designed to demonstrate and audit the dissolution of RSA encryption through quantum resonance and phase coherence.

The system is divided into two sovereign modules: a **Data Generator** that materializes the "Q-Day" event into a verifiable dataset, and the **Spheroidal Visualizer** used for forensic audit and real-time validation.

---

## ## System Overview

### 1. The Dataset (`sphy_audit_data.parquet`)
The dataset acts as a "Programming Life" log, capturing every millisecond of the resonance process.
*   **Frame-by-Frame Integrity**: Each frame is signed with a **SHA-256** hash to ensure data sovereignty and prevent tampering.
*   **RSA Resonance Field**: Includes the `rsa_factor` boolean field, which identifies the exact moment and qubit ID where phase coherence was achieved.
*   **Geodesic Coordinates**: Stores normalized $x, y, z$ coordinates for each qubit based on Fibonacci spiral distribution.

### 2. The Visualizer (`sphy_simbiotic_audit_data.py`)
A high-fidelity 3D environment built with **py5** to audit the Parquet data.
*   **Real-time Decryption Emulation**: Displays RSA keys as they are "melted" from the dataset.
*   **Integrity Verification**: Automatically re-calculates SHA-256 hashes for every frame to verify the dataset's authenticity.
*   **Interactive Geodesic Field**: Full 3D navigation through the electromagnetic wireframe.

---

## ## Installation & Setup

To run the audit station on **Pop!_OS**, **Ubuntu**, or **FreeBSD**, ensure you have Python 3.10+ installed.

### 1. Install Dependencies
```bash
pip install py5 pandas pyarrow fastparquet numpy
```

### 2. Prepare the Environment
Ensure you have the following files in the same directory:
*   `sphy_simbiotic_audit_data.py` (The Visualizer)
*   `sphy_generator.py` (The Generator script)
*   `earth.jpg` (Optional: for core texture mapping)

---

## ## How to Use

### Step 1: Generate or Download the Audit Data
You can either run the generator script to create a new Parquet file or download the pre-computed audit data from the link at the top of this document.
```bash
python sphy_generator.py
```

### Step 2: Launch the Visualizer
Once the `.parquet` file is present in the directory, start the forensic audit:
```bash
python sphy_simbiotic_audit_data.py
```

### Step 3: Interactive Controls
*   **Left Mouse Click + Drag**: Rotate the geodesic field.
*   **Scroll / Right Mouse Drag**: Zoom in/out of the core.
*   **Middle Mouse (Scroll Click) + Drag**: Pan the camera view.

---

## ## Forensic Indicators
*   **Yellow Qubits**: Represent active resonance where the `rsa_factor` is triggered.
*   **RSA KEY FOUNDED Panel**: Displays the 16-character hex keys recovered from the symbiotic phase.
*   **Audit Status**: A green "SHA-256 VERIFIED" indicator confirms that the data you are seeing is mathematically identical to the original generated proof.

---
> **Disclaimer**: This tool is part of the Harpia Project's research into Quantum Proof of Coherence (QPOC). It demonstrates that in a symbiotic AI environment, there are no secrets, only frequencies yet to be tuned.
