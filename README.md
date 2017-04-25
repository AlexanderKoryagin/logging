### Some logging experiments

***

Preparations for Ubuntu:
```bash
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential
sudo pip install -U pip setuptools virtualenv
virtualenv --clear .venv && source .venv/bin/activate
pip install -U -r requirements.txt
```
To run script:
```bash
python start.py
python start.py --debug   OR   python start.py --D
```
