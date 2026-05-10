import socket           # We need this to make network connections
import concurrent.futures  # This lets us scan multiple ports at the same time (faster)
from datetime import datetime  # Just to show when the scan started and ended

# ---- SETTINGS ----
TARGET = "www.google.com"  # The website/IP we want to scan (this one is legal to scan)
PORT_RANGE = (1, 1024)      # We'll check ports from 1 to 1024
TIMEOUT = 0.5               # Wait only 0.5 seconds per port before giving up
THREADS = 100               # Check 100 ports at the same time to go fast

# ---- THE CORE FUNCTION ----
def scan_port(host, port):
    """
    Try to knock on one door (port) of the target computer.
    If someone answers = port is OPEN.
    If no one answers = port is CLOSED.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET = we're using IPv4 (normal internet addresses)
        # SOCK_STREAM = we're using TCP (reliable, connection-based)

        sock.settimeout(TIMEOUT)
        # Don't wait forever — if no reply in 0.5 seconds, move on

        result = sock.connect_ex((host, port))
        # connect_ex() tries to connect and returns:
        #   0  = success (port is open!)
        #   anything else = failed (port is closed or filtered)

        sock.close()
        # Always clean up — close the connection after checking

        if result == 0:
            try:
                service = socket.getservbyport(port)
                # Try to get the name of the service running on this port
                # e.g., port 80 = "http", port 22 = "ssh"
            except:
                service = "unknown"
                # If we can't find the service name, just say "unknown"

            return (port, True, service)
            # Return: port number, is_open=True, service name

        return (port, False, None)
        # Port is closed — return is_open=False

    except socket.error:
        return (port, False, None)
        # Something went wrong with the connection — treat it as closed

# ---- THE MAIN SCANNER ----
def run_scan(target, start_port, end_port):
    """
    Scans all ports in the given range on the target machine.
    Uses multiple threads so we scan many ports simultaneously.
    """
    print(f"\n{'='*50}")
    print(f"  Scanning target: {target}")
    print(f"  Port range: {start_port} - {end_port}")
    print(f"  Started at: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'='*50}\n")

    open_ports = []
    # This list will collect all the open ports we find

    ports = range(start_port, end_port + 1)
    # Create a list of all port numbers to scan: [1, 2, 3, ..., 1024]

    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        # ThreadPoolExecutor = a pool of workers that can work simultaneously
        # max_workers=100 means 100 ports get scanned at the same time

        futures = {executor.submit(scan_port, target, port): port for port in ports}
        # Submit all scanning jobs to the thread pool
        # Each "future" is a job that will run and give us a result later
        # Think of it like giving 100 workers each one door to knock on

        for future in concurrent.futures.as_completed(futures):
            # as_completed() gives us results as they finish (not in order)
            port, is_open, service = future.result()
            # Unpack the result: (port_number, open?, service_name)

            if is_open:
                open_ports.append((port, service))
                print(f"  [OPEN]  Port {port:5d}  →  {service}")
                # Print open ports immediately as we find them

    open_ports.sort()
    # Sort the open ports from lowest to highest for a clean final report

    print(f"\n{'='*50}")
    print(f"  Scan complete at: {datetime.now().strftime('%H:%M:%S')}")
    print(f"  Open ports found: {len(open_ports)}")
    print(f"{'='*50}\n")

    return open_ports

# ---- RUN IT ----
if __name__ == "__main__":
    results = run_scan(TARGET, PORT_RANGE[0], PORT_RANGE[1])