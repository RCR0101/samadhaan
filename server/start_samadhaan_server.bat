@echo off
conda activate samadhaan

start /b python samadhaan-server.py
start /b python grievance_enhancer.py

echo Both scripts are running in the background.
