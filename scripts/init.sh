#!/bin/bash
pwd
#export MIRROR="-i https://pypi.doubanio.com/simple"
export MIRROR="-i https://mirrors.cloud.tencent.com/pypi/simple"
pip install $MIRROR -U pip
export LIBRARY_PATH=/lib:/usr/lib
pip install $MIRROR --no-cache-dir -r requirements.txt

ls -l -h -tr
