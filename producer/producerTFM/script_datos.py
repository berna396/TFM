#!/usr/bin/python

from os.path import isfile, join
import sys
import os

fileNameOk = "log_success"
fileNameError = "log_fail"
numOk = 1
numError = 1
fileContent = ""
flag = False
flagError = False
directoryNameOK = "/log_process/OK"
directoryNameERROR = "/log_process/ERROR"

# Se crea el directorio si no existe
os.makedirs(sys.argv[1] + directoryNameOK, exist_ok=False)
os.makedirs(sys.argv[1] + directoryNameERROR, exist_ok=False)

only_files = [f for f in os.listdir(sys.argv[1]) if isfile(join(sys.argv[1], f))]
for file in only_files:
    with open(sys.argv[1] + "/" + file) as file_in:
        for line in file_in:
            if flag:
                fileContent = fileContent + "\n" + line
                if "ERROR" in line:
                    flagError = True
                elif sys.argv[2] in line:
                    if flagError:
                        text_file = open(sys.argv[1] + directoryNameERROR + "/" + fileNameError + numError + ".log", "wt")
                        n = text_file.write(fileContent)
                        text_file.close()
                        numError = numError + 1
                    else:
                        text_file = open(sys.argv[1] + directoryNameOK + "/" + fileNameOk + numOk + ".log", "wt")
                        n = text_file.write(fileContent)
                        text_file.close()
                        numOk = numOk + 1
                    flag = False
                    flagError = False
                    fileContent = ""
            else:
                if sys.argv[2] in line:
                    fileContent = line
                    flag = True
