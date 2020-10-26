#!/bin/bash
pwd
pip install $MIRROR -U pip
export LIBRARY_PATH=/lib:/usr/lib
pip install $MIRROR --no-cache-dir -r requirements.txt

ls -l -h -tr
