# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.


n = True
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            if ~(x or y or z) == ~ x & ~ y & ~ z:
                n = True
            else:
                n = False
                break
print(n)


