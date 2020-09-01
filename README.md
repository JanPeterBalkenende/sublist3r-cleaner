# sublist3r-cleaner
A very simple python project that does one thing: clean the output you get from sublist3r in an output file, so you can use the file in combination with HTTProbe. 
I know it's not too useful, and definitely not revolutionary in any way, but I decided I needed the python practice.

sublist3r-cleaner basically clears the output file of a sublist3r search from symbols that obstruct a proper httprobe search. 
sublist3r-cleaner can be used as following:

1) download the cleaner.py file and store it in a place of your choosing
2) run sublist3r to generate an output file, for example:
sublist3r -d domain.com > outputfile.txt
3) Run cleaner.py and specify your filepath. For example:
python3 cleaner.py
>What is the path to your sublist3r output file?
/home/user/Documents
4) sublist3r-cleaner now replaced your outputfile with a cleaned version which you can now use with httprobe.

Thank you for using my little script!
