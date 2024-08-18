import os
import sys
import shlex
import subprocess
from concurrent.futures import ThreadPoolExecutor

def convert_evtx_to_xml(evtx_file):
    output_dir = "parsed"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    evtx_file_quoted = shlex.quote(evtx_file)
    output_file = os.path.join(output_dir, os.path.splitext(evtx_file)[0] + ".xml")
    output_file_quoted = shlex.quote(output_file)
    
    command = f"evtx_dump.py {evtx_file_quoted} > {output_file_quoted}"

    print(f"Processing file: {evtx_file}")
    
    sys.stdout.write(f"Processing file: {evtx_file} ... ")
    sys.stdout.flush()
    
    # Do the thing
    command = f"evtx_dump.py {evtx_file_quoted} > {output_file_quoted}"
    subprocess.run(command, shell=True)
    
    sys.stdout.write("done!\n")
    sys.stdout.flush()


def main():
    cwd = os.getcwd()
    
    # Get a list of .evtx files in the current dir
    evtx_files = [files for files in os.listdir(cwd) if files.endswith(".evtx")]
    
    # If there aren't any evtx files tell the user
    if not evtx_files:
        print("Files with the .evtx extention are not in the current working directory.")
        return

    # Parse several files concurrently 
    with ThreadPoolExecutor() as executor:
        executor.map(convert_evtx_to_xml, evtx_files)

# This is a python thing that acts as a conditional block that ensures the main function only runs when the script is run directly. I saw it was good to do (IDK python well)
if __name__ == "__main__":
    main()