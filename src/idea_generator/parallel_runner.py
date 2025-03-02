#!/usr/bin/env python3
import subprocess
import sys
import signal
import threading

# Lists to store launched processes and their reading threads
processes = []
threads = []

def signal_handler(sig, frame):
    print("\nInterruption detected, stopping all processes...")
    for proc in processes:
        if proc.poll() is None:  # If the process is not terminated
            try:
                proc.terminate()  # Send SIGTERM (compatible with Unix and Windows)
            except Exception as e:
                print(f"Error while stopping process: {e}")
                sys.exit(1)
    sys.exit(0)

# Capture CTRL+C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

def read_output(prefix, proc):
    """
    Reads the process output line by line, prefixing each line.
    """
    # Read in real-time (line by line) the standard output of the process
    for line in proc.stdout:
        print(f"{prefix}{line}", end="")

def main():
    try:
        nb_instances = int(sys.argv[1])
    except (IndexError, ValueError):
        nb_instances = 1

    print(f"🚀 Launching {nb_instances} instance(s) of the idea generator...")

    exit_codes = [None] * nb_instances

    # Concurrent launch of instances
    for i in range(nb_instances):
        instance_number = i + 1
        print(f"🔄 Launching instance {instance_number}...")
        proc = subprocess.Popen(
            ["python", "src/idea_generator/main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1  # For line-by-line buffering
        )
        processes.append(proc)
        # Start a thread to read the process output and prefix each line
        t = threading.Thread(target=read_output, args=(f"[Instance {instance_number}] ", proc))
        t.start()
        threads.append(t)

    print("⏳ Waiting for all instances to complete...")

    # Wait for all processes to terminate
    for i, proc in enumerate(processes):
        proc.wait()
        exit_codes[i] = proc.returncode

    # Wait for all reading threads to complete
    for t in threads:
        t.join()

    # Check exit codes and display corresponding messages
    failed = 0
    for i, code in enumerate(exit_codes):
        instance_number = i + 1
        if code != 0:
            print(f"❌ Instance {instance_number} failed with code {code}")
            failed += 1
        else:
            print(f"✅ Instance {instance_number} completed successfully")

    print(f"✅ {nb_instances - failed}/{nb_instances} instances completed successfully")
    if failed > 0:
        print(f"❌ {failed} instance(s) failed")
        sys.exit(0)
    else:
        print("📝 Reports have been generated in the conversations/ directory")
        sys.exit(0)

if __name__ == "__main__":
    main()
