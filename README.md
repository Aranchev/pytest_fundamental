After installing the new package, you need to update the requirements.txt file. The easiest way to do this is by running:

pip freeze > requirements.txt

With the virtual environment activated, install the dependencies listed in the requirements.txt file:

pip install -r requirements.txt