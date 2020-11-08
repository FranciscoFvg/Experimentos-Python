import webbrowser

while True:
    url = input('Digite a url do conteúdo: ')
    download = 'https://savefrom.net/' + url

    webbrowser.open(download)