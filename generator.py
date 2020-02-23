index = open("index.html", "w", encoding="utf-8")
index.write("""
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        font-family:Arial, sans-serif;
    }
    a {
        text-decoration: none;
    }
</style>
</head>
<body>
<h1>SpiddderTube</h1>
""")

f = open("videolist.txt", encoding="utf-8")
c = 0
while True:
    line = f.readline()
    if not line or c > 9:
        break
    c = c + 1
    index.write(line)
print("test")    
index.write("""
</body>
</html>
""")
index.close()