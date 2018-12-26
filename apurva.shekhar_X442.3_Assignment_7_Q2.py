#The input function will read a single line of text from the terminal.
#If you wanted to read several lines of text, you could embed this function
#inside a while loop and terminate the loop when the user of the program presses
#the interrupt key (Ctrl-C under UNIX, Linux and Windows.) Write such a program,
#and note its behavior when it receives the interrupt signal. Use a try/except
#clause to make the program behave more gracefully.


import sys

def readingtext():
    text = input("Enter text--")
    try:
        while True:
            extra_text = input("Enter more text or hit ctl+c to exit--")
            text = extra_text + text
            print (text)
    except KeyboardInterrupt:
        print ("\nYou ended the program.")
        sys.exit()

readingtext()
