import socket
import time

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning target: {target_ip}")
    print(f"Scanning ports: {start_port} to {end_port}")
    print("-" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout to avoid hanging on closed ports
            socket.setdefaulttimeout(1)
            # Attempt to connect to the port
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
                open_ports.append(port)
            else:
                print(f"Port {port}: CLOSED")
            sock.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Could not connect to server.")
            break

    print("-" * 50)
    print("Scan complete!")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    # Input target IP and port range
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    # Start the scan
    start_time = time.time()
    port_scanner(target_ip, start_port, end_port)
    end_time = time.time()

    print(f"Time taken: {end_time - start_time:.2f} seconds")
