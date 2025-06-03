# Quantum Random Number Generator (QRNG) - Private Implementation

## Project Overview

This project implements a robust Quantum Random Number Generator (QRNG) utilizing IBM Quantum's cloud-based quantum computers. Unlike traditional pseudo-random number generators (PRNGs) which operate on deterministic algorithms, this QRNG leverages the inherent, fundamental randomness of quantum mechanics. By measuring qubits in a state of superposition, it produces truly unpredictable bits, making it uniquely suited for applications requiring the highest level of cryptographic security and genuine unpredictability.

This repository serves as my private technical backbone and operational code for delivering specialized quantum randomness services to clients with critical security and randomness requirements.

## How It Works: The Quantum Randomness Process

The core mechanism of this QRNG is based on the principles of quantum mechanics:

1.  **Quantum Circuit Initialization:** A quantum circuit is constructed, containing a specified number of quantum bits (qubits), corresponding to the desired length of the random bit string.
2.  **Creating Superposition:** A Hadamard gate is applied to each qubit. This gate places each qubit into a superposition state, meaning it exists as both `0` and `1` simultaneously until measured. This is the source of the quantum randomness.
3.  **Quantum Measurement:** The superpositioned qubits are then measured. The act of measurement forces each qubit to "collapse" into a definite state – either `0` or `1` – with a 50/50 probability. The outcome of this collapse is inherently random and cannot be predicted.
4.  **Bit String Extraction:** The individual measurement outcomes from all qubits are concatenated to form a single, truly random bit string (e.g., "101100101011").
5.  **Execution on Quantum Hardware:** The prepared quantum circuit is executed on a real IBM Quantum processor (like `ibm_sherbrooke` or `ibm_brisbane`) to ensure the generation of genuine quantum randomness. A fallback to a local simulator is provided for development or in cases of hardware unavailability.

## Key Features & Capabilities

*   **True Quantum Randomness:** Generates random numbers rooted in the fundamental unpredictability of quantum mechanics, offering superior entropy compared to classical methods.
*   **IBM Quantum Hardware Integration:** Seamlessly connects to and utilizes high-performance IBM Quantum processors such as `ibm_sherbrooke` and `ibm_brisbane` for real-world quantum computation.
*   **Automated Backend Selection:** Intelligently attempts to connect to preferred quantum processors. If the primary choice is unavailable or non-operational, it automatically searches for and utilizes other available operational IBM Quantum backends.
*   **Robust Local Simulation Fallback:** Includes a robust fallback mechanism to a local Qiskit Aer simulator, ensuring the generation process can always proceed for development, testing, or during periods of quantum hardware downtime.
*   **Customizable Bit Length:** Supports the generation of random bit strings ranging from 8 to 256 bits, allowing for flexibility based on specific application requirements (e.g., cryptographic key lengths).
*   **Basic Randomness Verification:** Provides an immediate check of bit distribution (number of zeros and ones) and a simple entropy test to offer a quick indication of the randomness quality.

## Technical Requirements (For Development & Operation)

To set up and run this project, you will need:

*   **Python 3.8+**
*   **Required Python Libraries:**
    *   `qiskit`
    *   `qiskit-aer`
    *   `qiskit-ibm-runtime`
    *   `python-dotenv`
*   **IBM Quantum Account:** An active IBM Quantum account is necessary to obtain an API key for accessing IBM's quantum computing services. A free tier account provides sufficient access for specialized, low-volume random number generation tasks.

## Setup & Local Execution Instructions

These instructions are for setting up the environment to run the QRNG locally:

1.  **Obtain Project Files:**
    *   As this is a private repository, you would typically clone it if you have access rights:
        ```bash
        git clone https://github.com/shanuajns/Quantum-Random-Number-Generator.git
        cd Quantum-Random-Number-Generator
        ```
        (If you are operating entirely via the GitHub browser, you've already created and uploaded the files.)
2.  **Create a Virtual Environment (Highly Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install Python Dependencies:**
    ```bash
    pip install qiskit qiskit-aer qiskit-ibm-runtime python-dotenv
    ```
4.  **Configure IBM Quantum API Key:**
    *   Retrieve your personal API Token from your [IBM Quantum Experience Account page](https://quantum.ibm.com/account).
    *   Create a file named `.env` in the root directory of this project (next to `quantum_rng_api.py`).
    *   Add your API key to this `.env` file in the following format:
        ```
        IBM_API_KEY=YOUR_API_TOKEN_HERE
        ```
    *   **Crucial Security Note:** The `.env` file is intentionally excluded from version control (`.gitignore`) to protect your sensitive API key. Do NOT commit your actual `.env` file to any repository.

## How to Run the QRNG Script

1.  **Ensure your virtual environment is active:**
    ```bash
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
2.  **Execute the Python script:**
    ```bash
    python quantum_rng_api.py
    ```
3.  The program will prompt you to input the desired number of random bits (ranging from 8 to 256).

## Sample Output

Below is an example of the kind of output generated by the QRNG, demonstrating its connection to IBM Quantum hardware and the resulting random values:

```
=== Quantum Random Number Generator ===
Enter number of bits (8-256): 12
✅ Connected to IBM Quantum Cloud
ℹ️ Using IBM Quantum instance: Quantum_rng
🔧 Selected quantum processor: ibm_sherbrooke  # This may also show ibm_brisbane or another backend
🚀 Job submitted. ID: d0vaf57p51os73b2qsvg
🔗 Monitor at: https://quantum.ibm.com/jobs/d0vaf57p51os73b2qsvg
🎉 Quantum generation successful in 3.06s

Random bits: 100101110011
Decimal value: 2419

Quantum properties:
Bit distribution: 5 zeros, 7 ones
Entropy test: Pass
```

## Service Offering & Monetization Strategy

This project's advanced capabilities form the foundation for offering specialized, high-value quantum randomness services. Unlike mass-market random number generation, my focus is on delivering unique, highly secure, and verifiable random data for critical applications.

**I leverage this technology to provide:**

*   **Custom Quantum-Derived Cryptographic Key/Seed Generation:** For clients requiring the absolute highest level of unpredictability in their cryptographic keys, blockchain addresses, secure identifiers, or initial seeds for sensitive systems. Services include generating keys of specified lengths (e.g., 128-bit, 256-bit) and delivering them through secure, mutually agreed-upon channels.
*   **Quantum-Enhanced Pseudo-Random Number Generator (PRNG) Initialization:** For situations where clients utilize classical PRNGs but require a boost in initial entropy for specific, high-stakes events (e.g., lottery draws, highly sensitive simulations, secure protocol initiations). I provide a truly random, quantum-sourced seed to elevate the security and unpredictability of their existing systems.
*   **Expert Quantum Randomness Consulting:** Offering guidance and strategic advice on the application, integration, and verification of quantum randomness within client's existing security architectures and development processes.

**Monetization Approach:** My services are based on a premium, value-driven pricing model, reflecting the specialized nature and unparalleled security benefits of quantum-derived randomness. Given the resource-intensive nature of accessing quantum hardware, I focus on delivering bespoke, high-impact random data solutions rather than high-volume, low-value generation.

For inquiries regarding specialized quantum randomness services or consultations, please contact me directly.
```
