#!/bin/bash

# Read in arguments
while getopts ":d:a:" arg; do
  case $arg in
    d) # specify beer csv location
      data=${OPTARG};;
    a) # anonymize or not
      anon=${OPTARG};;
  esac
done

Rscript -e \
  "rmarkdown::render('index.Rmd', output_dir='site', \
  params = list(data_file='$data', anonymize='$anon'))"
