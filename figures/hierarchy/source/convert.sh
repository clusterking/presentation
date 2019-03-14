#!/usr/bin/env bash

for f in *.svg; do; echo $f; inkscape $f --export-pdf ../${f%.*}.pdf; done
