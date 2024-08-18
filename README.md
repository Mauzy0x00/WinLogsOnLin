I created this because I had to parse many windows logs files and I didn't want to run the parsing script on each file manually 

# How to parse many files
- Ensure python-evtx is installed
  - https://github.com/williballenthin/python-evtx
- Run `ParseAllEVTX.py` in the directory that has all of your evtx files
- This will create a directory called `parsed` and will output each .evtx file here as an `.xml` file

# How to mass search your parsed Windows logs
- Create a txt file that has a search term on a new line
- Ensure that your file paths have two back slashes (with an extra `\`) (ex. `C:\\WINDOWS\\system32`)
- Run `SearchLogs.py` with the arg `<YOUR_FILE_HERE>`
