#!/usr/bin/python
from logreduce import Classifier, Tokenizer, render_html

clf = Classifier(
    # A function to normalize filename, for example to remove dates or id
    filename_to_modelname=lambda fn: fn,
    # A function to ignore some file, for example configuration file
    keep_file=lambda _: True,
    # A function to process line
    process_line=Tokenizer.process
)

clf.train(["/home/adrian/Desktop/TFM/Modelo/LOG_OK/log_success1.log"])


result = clf.process(["/home/adrian/Desktop/TFM/Modelo/LOG_ERROR/log_fail1.log"])
with open("reports/report1.html", "w") as of:
    of.write(render_html(result))
