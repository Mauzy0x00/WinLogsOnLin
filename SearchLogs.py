# I was very intoxicated when I wrote this. I don't know python well but it seems to work as I want. 
# Hooray. Thank you W3Schools and stackoverflow

import os
import subprocess
import argparse

def grep_files(query_file):
    # Check if the file exists
    if not os.path.isfile(query_file):
        print(f"Query file {query_file} does not exist")
        return

    # Read the from the file yeah
    with open(query_file, 'r') as f:
        queries = [line.strip() for line in f if line.strip()]

    # Get the the cwd LIST
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # Read Da files and use GREP!
    for query in queries:
        print(f"Searching for query : {query}")
        for file in files:
            command = f"grep -H '{query}' {file}"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            if result.stdout:
                print(f"Results in {file}:")
                print(result.stdout)
            else:
                print(f"No matches found in {file}.")

def main():

    parser = argparse.ArgumentParser(description='Search Windows log files using search terms that are in a txt file')
    parser.add_argument('query_file', type=str, help='File path')
    
    args = parser.parse_args()
    
    grep_files(args.query_file)

if __name__ == "__main__":
    main()