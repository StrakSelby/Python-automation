import subprocess
import os

absoulte_path = input("Input the absoulte path of the logfile: ")

# Get the absolute path to the project root
absoulte_path = os.path.expanduser(absoulte_path)

file_name = input("Input the logfile name: ")

# join the file path with the file
log_file_path = os.path.join(absoulte_path, file_name)

# Ensure that the path is absolute
log_file_path = os.path.abspath(log_file_path)

# to clear the input terminal
# os.system("clear")

try:
# Use grep to find lines containing "error" in a log file
        grep_process = subprocess.Popen(['grep', '-i', 'system',log_file_path], stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE ,text=True)
        
        # Capture stderr and stdout
        stdout, stderr = grep_process.communicate()

        if stderr:
                # If there is an error output, raise an exception
                raise FileNotFoundError(stderr.strip())

        error_count = 0
        # Read lines containing "error" from standard input (provided by subprocess)
        for line in stdout.splitlines():
                # Process each error line
                error_count += 1
                print(f"Found: {line.strip()}")

        print("Finished analyzing errors.")
        print(f"There are {error_count} errors in this logfile")

except Exception as e:
        print(f"{e}")       


