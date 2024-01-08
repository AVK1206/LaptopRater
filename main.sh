#!/bin/bash

set -e

uvicorn route:app --host 0.0.0.0 --port 8004 --reload
