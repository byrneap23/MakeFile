# Andrew Byrne and Hannah Betts

.PHONY: files
files: number1.txt number2.txt

number1.txt:
	python3 python1.py
number2.txt:
	python3 python2.py

.PHONY: clean
clean:
	rm -f *.txt 
