import markdown

mdFile = input("Enter the path to the md file: ")

with open(mdFile, 'r') as f:
    text = f.read()

html = markdown.markdown(text)


with open('output.html', 'w') as f:
    f.write(html)