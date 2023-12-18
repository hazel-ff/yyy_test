# 时间：2023/5/13 19:51

def caculation(a,b,form):
    try:
        if form =="+":
            res = a+b
        elif form=="-":
            res = a-b
        elif form=="*":
            res =a*b
        elif form=="/":
            res = a/b
        else:
            res = "出错了"
    except Exception as e:
        print(f"出现异常……")
        # res = "出错啦"

    finally:
        return res


if __name__ == '__main__':
    print(caculation(9.9,2,"="))





