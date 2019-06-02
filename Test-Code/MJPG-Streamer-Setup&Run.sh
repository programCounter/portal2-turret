#!/bin/bash

# Basic shell script to install and run mjpeg-streamer
# Author: Riley Larche (Program Counter)
# Date Created: 2019-05-20
# Date Updated: 2019-05-20

setup(){
  echo "[INFO] Setting up MJPG-streamer in the CWD. User intervention may be required."
  echo "[INFO] Installing the required dependincies."
  sudo apt-get install cmake libjpeg8-dev
  sudo apt-get install gcc g++
  sleep 1
  echo "[INFO] Downloading MJPG-streamer-experimential."
  git clone https://github.com/jacksonliam/mjpg-streamer.git
  sleep 1
  echo "[INFO] Building and installing."
  cd mjpg-streamer/mjpg-streamer-experimental
  make distclean
  make CMAKE_BUILD_TYPE=Debug
  sudo make install
}

run(){
  echo "[INFO] Starting MJPG-streamer with input_raspicam."
  cd mjpg-streamer/mjpg-streamer-experimental
  export LD_LIBRARY_PATH=.
  ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 1920 -y 1080 -fps 30 -ex night"
  echo "View camera stream at: http://<Raspberry Pi's IP>:8080/?action=stream"
}

echo "[WARN] This script needs sudo permission. Make sure to run with sudo."
echo "Do you wish to setup/re-install MJPG-streamer? [y/n]: "
read ans
if [[ $ans == 'y' || $ans == 'Y' ]]; then
  setup
else
  run
fi
