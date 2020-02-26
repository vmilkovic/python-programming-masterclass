import webbrowser

webbrowser.open('https://www.python.org')

help(webbrowser)

chrome = webbrowser.get(using='google-chrome')
chrome.open_new('https://www.python.org')


