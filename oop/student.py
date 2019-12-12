class Student(object):
    def __init__(self, name, score, alias):
        self.name = name
        self.score = score
        self.__alias = alias

    def print_score(self):
        print('%s: %s' % (self.name , self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else :
            return 'C'
    
    def get_alias(self):
        return self.__alias


if __name__ == '__main__':
    bart =  Student('Bart Simpson', 59, ('car' , 'cat'))
    bart.print_score()
    # 不能直接访问__alias是因为Python解释器对外把__alias变量改成了_Student__alias
    # 不同版本的Python解释器可能会把__alias改成不同的变量名
    print(bart.__alias) 
    # 外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name
    # 变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量
    bart.__alas = ('Car')
    print(bart.get_alias())