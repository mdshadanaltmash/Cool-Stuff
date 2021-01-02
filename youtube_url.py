#It opens a browser to which asks user to select the quality of media to download
import webbrowser
url=input("Enter you youtube URL: ")
url=url[:12]+'ss'+url[12:]
webbrowser.open(url)
