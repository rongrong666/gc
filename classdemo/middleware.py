def simple_middleware(get_response):
    # 此处编写的代码仅在 Django 第一次配置和初始化的时候执行一次。
    print('init')

    def middleware(request):

        # 此处编写的代码会在每个请求处理视图前被调用。
        print('视图函数调用之前执行的区域')

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('视图函数调用之后执行的区域')

        return response

    return middleware


def simple_middleware2(get_response):
    # 此处编写的代码仅在 Django 第一次配置和初始化的时候执行一次。
    print('init2')

    def middleware(request):

        # 此处编写的代码会在每个请求处理视图前被调用。
        print('视图函数调用之前执行的区域2')

        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('视图函数调用之后执行的区域2')

        return response

    return middleware