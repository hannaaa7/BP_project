import math
# کتابخانه ریاضی را فراخوانی میکنیم.
def random_float(n, a, b, xn="h"):
# یک تابع رندوم برای اعداد اعشاری میسازیم که چند ورودی نیاز دارد. تعداد اعداد مورد نیاز، ابتدای بازه،انتهای بازه و مقدار ثابت اولیه که برای مقدار ثابت اولیه یک حالت پیش فرض هم در نظر میگیریم
    xn = hash(xn)
#مقدار ثابت اولیه را با استفاده از تابع hash به صورت رندوم انتخاب میکنیم
    d = 1103515245
    c = 12345
    m = 2**31
#به یکسری متنغیر یکسری اعداد تست شده را نسبت میدهیم
    _list = []
    while len(_list) != n:
#یک حلقه تعریف میکنیم که تا زمانی که تعداد آرایه های لیست برابر تعداد رندمی که نیاز داریم نشده، همچنان ادامه دهد.
        xn = (d * xn + c) % m
# فرمول دنباله تصادفی اعداد
        xm = xn / m
#برای اینکمه عدد اعشاری شود
        xl = xm * (b - a) + a
# برای اینکه در دامنه باشد عدد
        _list.append(xl)
#مقدار به دست آمده را در لیست مورد نظر میریزیم
    return _list
