FROM ubuntu:latest
# Make a dir for our application
WORKDIR /Initialisation
# install dependency
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy source code
COPY /Initialisation .
# run the program
CMD ['python', "Initialisation.py"]