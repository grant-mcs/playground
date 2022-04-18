from fileinput import close
import os 
import sys

def print_usage():
    print("Usage:")
    print("This script edits a Kubernetes manifest file to include a new version number on a container image.")
    print("\n  update-k8s-manifest.py <manifest file path> <new container image version>")

if len(sys.argv) != 3:
    print("\nERROR! Incorrect number of arguments provided (" + str(len(sys.argv)) + "), expected 2\n")
    print_usage()
    sys.exit(1)

lines = []

with open(sys.argv[1], 'r') as manifestFile:
    lines = manifestFile.readlines()

outputFile = ""
inSpec = False
inContainers = False
updateDone = False
for line in lines:
    if updateDone:
        outputFile += line
    elif inSpec and inContainers:
        if line.lstrip().startswith("image:"):
            imageIndex = line.find("image:")
            whitespace = line[:imageIndex]
            outputFile += whitespace + "image: " + sys.argv[2] + os.linesep
            updateDone = True
        else:
            outputFile += line
    elif inSpec:
        if line.lstrip().startswith("containers:"):
            inContainers = True
        outputFile += line
    else:
        if line.lstrip().startswith("spec:"):
            inSpec = True
        outputFile += line

with open(sys.argv[1], 'w') as yaml_file:
    yaml_file.write(outputFile)

