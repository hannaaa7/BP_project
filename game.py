import randomm
#کتابخانه ریاضی را فراخوانی میکنیم.
n = int(input())
#تعداد دست هایی که بازی باید انجام شود را از کاربر دریافت میکنیم
player = []
i = 0
while i < 20:
    player.append(i)
    i += 1
money = []
#یک لیست خالی از پول بازیکنان که 20 نفر هستنذ میسازیم
while len(money) < 20:
    money.append(25)
# یک حلقه ایجاد میکنیم و به تک تک بازیکن ها که 20 نفر هستن نفری 25 دلار میدهیم
i = 0
seed = "h"
while i < n:
    j = 0
    while j < len(player):
        daryaft = randomm.random_int(n=1, a=0, b=len(player), xn= seed)
        daryaft = daryaft[0]
        seed += "b"
#برای هربار تغییر مقدار اولیه و داشتن یک عدد رندوم متفاوت، مقدار ثابت را تغییر میدهیم
        money[player[j]-1] -= 1
        money[player[daryaft]-1] += 1
# از بازیکنی که نوبتش دشه یه واحد کم میکنیم و به بازیکنی که رندوم انتخاب شده یه واحد اضافه میکنیم
        if money[player[j]-1] == 0:
            player.remove(player[j])
# اگر پول یکی از بازیکنان صفر شود از لیست انتخاب رندوم حذف میکینم
        j += 1
    i += 1

print(money, len(player))
print(player, len(player))
# پول های باقی مانده هرکس و تعداد بازکین های باقی مانده
# پول بازیکن های باقی مانده و شماره بازیکن های باقی مانده 
