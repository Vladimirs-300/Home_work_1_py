# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (x or y or z or w) == (not x and not y and not z and not w):
                    print(x, y, z, w)


# Сделал по аналогии задачи из семинара. Не уверен, что жто верное решение.                  