import webbrowser

# command line -> python -m webbrowser -t "http://www.python.org"

webbrowser.open("https://www.python.org",new=1)
#
# help(webbrowser)


# Print default -> *objects, sep='', end='\n', file=None, flush=False
for i in range(10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=';',end='  ')

# using .get() for webbrowser NOTE: May be console based
chrome = webbrowser.get(using='google-chrome')
chrome.open_new("https://www.python.org/")
