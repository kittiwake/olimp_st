import time

# 2. ТОТ ЖЕ САМЫЙ цикл, но с print'ом
start = time.time()
sum = 0
for i in range(100000):
    sum += i
    print(sum)  # <--- ЭТА СТРОКА ВСЕ УБИВАЕТ
print(f"Сложение c print: {time.time() - start:.5f} сек")
# 1. Быстрый цикл (сложение, процессор доволен)
start = time.time()
sum = 0
for i in range(100000):
    sum += i
print(f"Сложение без print: {time.time() - start:.5f} сек")
