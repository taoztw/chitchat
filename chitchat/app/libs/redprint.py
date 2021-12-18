class Redprint:
    """
    需要实现的功能：
        1. 接收传入的参数 红图名字 name
        2. 指定prefix_url
        3. route()装饰器实现
        4. register方法实现
    """
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options): # 模仿蓝图实现
        def decorator(f):
            # 从源码中看到 这个会调用蓝图的self.add_url_rule方法，
            # 但是在redprint中无法获得蓝图的对象。所以我们这里的思想就是
            # 先保存 rule，f，**options的变量。
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None): # bp蓝图对象
        if url_prefix is None:
            url_prefix = '/' + self.name
        # bp就是蓝图对象
        for f, rule, options in self.mound:
            # 将endpoint修改为红图加上函数的名字
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__) # 字典 pop函数
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)