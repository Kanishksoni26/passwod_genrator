# Python TCP Port Scanner

A multithreaded TCP port scanner built using Python sockets and `ThreadPoolExecutor`.

This project scans a target host for open TCP ports within a specified range and displays the detected services running on those ports.

---

# Features

* TCP port scanning using Python sockets
* Multithreaded scanning for faster performance
* Configurable port range
* Timeout handling
* Basic service detection using `socket.getservbyport()`
* Clean terminal output

---

# Technologies Used

* Python 3
* Socket Programming
* Concurrent Futures (Multithreading)

---

# Project Structure

```text
port_scanner/
│
├── main.py          # Main scanner script
├── README.md        # Project documentation
└── requirements.txt # Dependencies (optional)
```

---

# How It Works

The scanner:

1. Creates TCP sockets using Python's `socket` module
2. Attempts to connect to ports on the target machine
3. Uses multiple threads to scan many ports simultaneously
4. Detects open ports using `connect_ex()`
5. Displays service names for known ports

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Move into the project directory:

```bash
cd your-repository-name
```

---

# Run the Scanner

```bash
python3 main.py
```

---

# Example Output

```text
==================================================
  Scanning target: scanme.nmap.org
  Port range: 1 - 1024
  Started at: 20:30:11
==================================================

  [OPEN]  Port    22  →  ssh
  [OPEN]  Port    80  →  http
  [OPEN]  Port   443  →  https

==================================================
  Scan complete at: 20:30:15
  Open ports found: 3
==================================================
```

---

# Important Concepts Used

## Socket Programming

Sockets are communication endpoints used to establish connections between devices over a network.

## TCP Connect Scan

This scanner performs a TCP Connect Scan by attempting a full TCP connection with the target port.

## Multithreading

`ThreadPoolExecutor` is used to scan multiple ports simultaneously, making the scanner significantly faster.

---

# Configuration

You can modify these values in `main.py`:

```python
TARGET = "www.google.com"
PORT_RANGE = (1, 1024)
TIMEOUT = 0.5
THREADS = 100
```

---

# Legal Disclaimer

This project is intended for:

* Educational purposes
* Personal learning
* Authorized security testing only

Do NOT scan systems without permission.

---

# Future Improvements

* Command-line argument support
* Banner grabbing
* UDP scanning
* Result export to files
* Web interface using Flask
* GUI version

---

# Author

Kanishk
