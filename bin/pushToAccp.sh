#!/bin/bash

read -p "Release branch? " release

cd ~/digi/ravenskeepChars/
git push herokuaccp $release:master

