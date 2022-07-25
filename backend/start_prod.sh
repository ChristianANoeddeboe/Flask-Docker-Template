#!/bin/bash
gunicorn -b 0.0.0.0:5000 --workers=1 --threads=4 --timeout 600 --worker-class=gthread --worker-tmp-dir /dev/shm app:app