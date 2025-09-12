f=open("image.jpg","rb")
content=f.read()
f.close()

f=open("image5.jpg","wb")
f.write(content)
f.close()