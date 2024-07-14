@echo off
echo Hello! Installing libs...
echo Thank you for installing SXServiseCLI 2024! We are currently installing the libraries...
echo Updating pip...
python -m pip install --upgrade pip

echo Installing necessary libraries...
pip install json
pip install hashlib
pip install tqdm
pip install requests
pip install subprocess
pip install os
pip install datetime
pip install colorama
pip install ctypes
pip install qrcode
pip install socketserver
pip install socket
pip install sys
pip install string
pip install platform
pip install http.server
pip install socketserver
pip install http
pip install plyer

echo libs installation completed!

python first_app_start.py
