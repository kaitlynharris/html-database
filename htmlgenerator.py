import os
import webbrowser

def createPage(bodytext):
    sale = open("newpage.html", "w+")

    sale.write('<html>\n\t<body>\n\t' +bodytext+ '\n\t</body>\n</html>')

    sale.close()

    dirpath = os.path.dirname(os.path.abspath(__file__))
    filepath = 'file://' + dirpath + '/newpage.html'

    webbrowser.open_new_tab(filepath)

def main():
    createPage("Stay tuned for our amazing summer sale!")


if __name__ == '__main__':
    main()
