from io import BytesIO
f = BytesIO()
len = f.write('中文'.encode('utf-8'))
print(len,f.getvalue())