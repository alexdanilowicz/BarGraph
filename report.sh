#!/bin/bash

# Read in arguments
while getopts ":d:o:n:a:" arg; do
  case $arg in
    d) # specify beer csv location
      data=${OPTARG};;
    o) # output directory
      out_dir=${OPTARG};;
    n) # name of file
      name=${OPTARG};;
    a) # anonymize or not
      anon=${OPTARG};;
  esac
done

echo "$data" "$out_dir" "$name" "$anon"

Rscript -e \
  "rmarkdown::render('index.Rmd', output_dir='$out_dir', output_file='$name', \
  params = list(data_file='$data', anonymize='$anon'))"
