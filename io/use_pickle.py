import pickle

# with open('dump.txt', 'wb') as f:
#     d = dict(name='Bob', age=20, score=88)
#     bytesObj = pickle.dumps(d)
#     print(bytesObj)
#     pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)
