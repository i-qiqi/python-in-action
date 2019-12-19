# python-in-action

## 基础

- 交换：`a, b = b, a`
    ```
    # 在python中，会在过程中生成一个元组 c，并且c = (b ,a)，
    # 然后进行a = c[0] ， b = c[1] 的操作
    ```
- with原理
    ```
    # with语句适用于对资源访问的场景，确保不管使用过程中是否发生异常都会执行必要的“清理”
    # 自定义上下文管理器来对软件系统中的资源进行管理, 比如数据库连接、共享资源的访问控制
    ```
## 高阶函数
### 闭包

### 模块
- 弄懂这个只需要在google上搜索： python if name == 'main

然后看stack overflow上的第一个回答就知道了。

### 参考
- [Jupyter documentation](https://jupyter.org/documentation)
