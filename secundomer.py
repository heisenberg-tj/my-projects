# Секундомер
import time
while True:
    try:
        limit = int(input("До скольких секунд считать?: "))
        seconds = 0
        break
    except ValueError:
        print("Нужно вводить только цифры!")
while seconds <= limit:
    print(seconds)
    seconds += 1
    time.sleep(1)
    if seconds > 11:
        while True:
            print(11)
            time.sleep(1)
print("Секундомер дошёл до конца и остановился!")
