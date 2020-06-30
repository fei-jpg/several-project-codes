# 华氏温度转摄氏温度
fahrenheit = 0
print('Fahrenheit Celsius')
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 # 公式 C=(F-32)/1.8
    print('{:7d} {:10.2f}'.format(fahrenheit,celsius)) #7d、10为7、10个字符的宽度（同一行字空出多少空格）
    fahrenheit = fahrenheit + 25
