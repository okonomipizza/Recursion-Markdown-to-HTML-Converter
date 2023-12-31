import sys
import markdown

def isFileFormatValid(fileName, format):
    if format in fileName: return True
    return False


commandList = sys.argv

if not len(commandList) == 4:
    raise ValueError("Invalid number of arguments")

if not commandList[1] == "markdown":
    raise ValueError("Invalid command")
if not isFileFormatValid(commandList[2], ".md") and not isFileFormatValid(commandList[3], ".html"):
    raise ValueError("Invalid file format")

mdFile = commandList[2]
htmlFile = commandList[3]

md = ""
with open(mdFile, 'r') as f:
    md = f.read()

html = markdown.markdown(md, extensions=['tables'])

with open(htmlFile, 'w') as f:
    f.write(html)

print("HTML file generated")