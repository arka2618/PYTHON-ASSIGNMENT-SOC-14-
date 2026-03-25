#Open and Read a file
f = open("Demofile.txt", "r")
content = f.read()
print(content)
f.close()
#Write a file
f = open("Demofile.txt", "a")
W =  f.write("\nIf your days are lonely, you are a loner")
print(W)
f.close
