# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
# 比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便
import json

# d = dict(name='Bob', age=20, score=88)
# djson = json.dumps(d) # 返回json格式的str
# print(d, djson)
# print(d['name'], isinstance(djson,str))

# # JSON标准规定JSON编码是UTF-8
# json_str = '{"name": "Bob", "age": 20, "score": 88}'
# d_copy = json.loads(json_str)
# print(d_copy, isinstance(d_copy, dict))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象
def stu2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }
s = Student('Bob', 20, 88)

# print(json.dumps(s))
# print(json.dumps(s, default=stu2dict))

# 通常class的实例都有一个__dict__属性，
# 它就是一个dict，用来存储实例变量
print('s.__dict__: %s' % s.__dict__)
print(json.dumps(s, default=lambda x : x.__dict__))

def dict2stu(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"name": "json", "age": 25, "score": 78}'
print(json.loads(json_str, object_hook=dict2stu))