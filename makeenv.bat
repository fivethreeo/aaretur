call setenv.bat
c:\python27\Scripts\virtualenv.exe env --system-site-packages
pip install -r requirements.txt
python develop.py manage syncdb --all --noinput
npm install less
