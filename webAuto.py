import webbrowser as wb

def AutoWeb():
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
    
    urls = (
        "https://www.udemy.com",
        "https://www.github.com",
        "https://www.gmail.com",
        "https://www.youtube.com"
    )
    
    for url in urls:
        print("Opening... " + url)
        wb.get(brave_path).open(url)

AutoWeb()
