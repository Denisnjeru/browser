# needs webbrowser- launches a browser  on your default webbrowser 
##takes from the clipboard or commandline 
# py 3
# by denis ndumbe 
"""
https://twitter.com
https://instagram.com
https://web.facebook.com
https://www.reddit.com
links ordered as how they are copied on the clipboard an example 
"""

import webbrowser, sys ,pyperclip  #  webbrowser for opening a browser  and operating the tabs : sys getting input from command line : pyperclip for taking input from the clipboard 

 
if len(sys.argv) > 1:
    # get address from command line 
    address = ''.join(sys.argv[1:])  # getting the address from commandline 
else:
    # getting from clipboard
    if pyperclip.paste().__contains__('\r\n'):
        lst = pyperclip.paste().split()
        i = 0
        while i < len(lst):
            webbrowser.open(lst[i])
            i = i + 1
            






