#!/usr/bin/python

from os.path import isfile, join
import sys
import os

fileNameOk = "log_success"
fileNameError = "log_fail"
fileContent = ""
flag = False
flagError = False
flagFind = False
directoryNameOK = "/log_process/OK"
directoryNameERROR = "/log_process/ERROR"

# Se crea el directorio si no existe
os.makedirs(sys.argv[1] + directoryNameOK, exist_ok=True)
os.makedirs(sys.argv[1] + directoryNameERROR, exist_ok=True)

list_ids = []

only_files = [f for f in os.listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]

for file in only_files:
    with open(sys.argv[1] + "/" + file, encoding='latin-1') as file_in:
        for line in file_in:
            if sys.argv[2] in line:
                line_split = line.split(" | ")
                list_ids.append(line_split[3].replace("[", "").replace("]", ""))

for idOp in list_ids:
    for file in only_files:
        with open(sys.argv[1] + "/" + file, encoding='latin-1') as file_in:
            for line in file_in:
                if line.startswith("2021"):
                    if idOp in line:
                        fileContent = fileContent + line
                        if "ERROR" in line:
                            flagError = True
                        flagFind = True
                    else:
                        flagFind = False
                elif flagFind:
                    fileContent = fileContent + line

    if flagError:
        text_file = open(sys.argv[1] + directoryNameERROR + "/"
                         + fileNameError + idOp + ".log", "wt")
        n = text_file.write(fileContent)
        text_file.close()
    else:
        text_file = open(sys.argv[1] + directoryNameOK + "/" + fileNameOk + idOp+ ".log", "wt")
        n = text_file.write(fileContent)
        text_file.close()

    flagError = False
    fileContent = ""

