#!/usr/bin/env bash
set -x # Echo on
hatch build .
mv piecewise_functions_fp-0* ./dist