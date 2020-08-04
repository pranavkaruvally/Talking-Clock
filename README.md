# Talking-Clock
A talking clock made in Python which tries to emulate the old Nokia speaking clock

Just run the following commands to install the program:

	chmod +x install.sh
	./install.sh

To execute the program, type:
	
	speaktime.py

for all those who are using package managers other than aptitude, do the following:

Install the following packages:

	python3-pip
	espeak

Then using pip3, install pyttsx3 using the command:

	pip3 install pyttsx3

And then run the following commands:

	chmod +x speaktime.py
	sudo cp speaktime.py /usr/bin/speaktime.py

And now you could execute the program from a terminal or a run command by typing in:

	speaktime.py
