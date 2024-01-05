#!/bin/bash

set -e

python db/mondb.py

uvicorn route:app --host 0.0.0.0 --port 8001 --reload
