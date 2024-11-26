# print("Men siz o'ylagan sonni topaman!")
# print("Iltimos, 1 va 100 orasidagi sonni o'ylang.")
# start = 1
# end = 100
# step = 0
# max_steps = 3
# stop = False
# while start <= end and step < max_steps:
#     taxmin = (start + end) // 2
#     step += 1
#     javob = input(f"Siz o'ylagan son {taxmin} dan kichikmi? (ha/yo'q): ").lower()
#
#     if javob == "ha":
#         end = taxmin - 1
#     elif javob == "yo'q":
#         start = taxmin + 1
#     else:
#         print("Iltimos, faqat 'ha' yoki 'yo'q' deb javob bering.")
#         continue
#
# if step == max_steps:
#     print("3 ta urinishda topolmadim")
# else:
#     print(f"Men siz o'ylagan sonni {taxmin} deb topdim!")
# #     print(f"Bu {step}-chi qadamda amalga oshdi.")
# from pyqtgraph.examples.customPlot import tickViewer
# from weasyprint.css.validation.descriptors import system

#
# # 11.
# n = int(input("n ni kiriting: "))
# S = 0
# for i in range(n + 1):
#     S += (n + i) ** 2
# print("natija:", S)
#
# # 12.
# n = int(input("n ni kiriting: "))
# S = 1
# for i in range(1, n + 1):
#     S *= (1 + i / 10)
# print("12:", S)
#
# # 13.
# n = int(input("n ni kiriting: "))
# S = 0
# for i in range(1, n + 1):
#     S += (1 + i / 10) * (-1) ** (i + 1)
# print("natija:", S)
#
# # 14.
# n = int(input(" n ni kiriting: "))
# S = 0
# for i in range(1, n + 1):
#     S += (2 * i - 1) ** 2
# print("natija:", S)
#
# # 15.
# a = float(input("a ni kiriting: "))
# n = int(input("n ni kiriting: "))
# S = 1
# for _ in range(n):
#     S *= a
# print(" natija:", S)
#
# # 16.
# a = float(input(" a ni kiriting: "))
# n = int(input(" n ni kiriting: "))
# print(" natijalar:")
# for i in range(1, n + 1):
#     print(a ** i)
#
# # 17.
# a = float(input(" a ni kiriting: "))
# n = int(input("n ni kiriting: "))
# S = 0
# for i in range(n + 1):
#     S += a ** i
# print(" natija:", S)
#
# # 18.
# a = float(input("For18 uchun a ni kiriting: "))
# n = int(input("For18 uchun n ni kiriting: "))
# S = 0
# for i in range(n + 1):
#     S += (-1) ** i * a ** i
# print("natija:", S)
#
# # 19.
# n = int(input(" n ni kiriting: "))
# S = 1
# for i in range(1, n + 1):
#     S *= i
# print("For19 natija:", S)
#
# # 20.
# n = int(input(" n ni kiriting: "))
# S = 0
# for i in range(1, n + 1):
#     faktorial = 1
#     for j in range(1, i + 1):
#         faktorial *= j
#     S += faktorial
# print("natija:", S)
#
# # 21.
# n = int(input("n ni kiriting: "))
# S = 1  # 1 ni qo'shib boshlaymiz
# faktorial = 1
# for i in range(1, n + 1):
#     faktorial *= i
#     S += 1 / faktorial
# print("natija:", S)
#
# # 22.
# x = float(input("x ni kiriting: "))
# n = int(input(" n ni kiriting: "))
# S = 1  # 1 ni qo'shib boshlaymiz
# faktorial = 1
# for i in range(1, n + 1):
#     faktorial *= i
#     S += (x ** i) / faktorial
# print(" natija:", S)
#
# # 23.
# x = float(input(" x ni kiriting: "))
# n = int(input(" n ni kiriting: "))
# S = 0
# for i in range(n + 1):
#     faktorial = 1
#     for j in range(1, 2 * i + 2):
#         faktorial *= j
#     S += (-1) ** i * (x ** (2 * i + 1)) / faktorial
# print(" natija:", S)
#
# # 24.
# x = float(input("x ni kiriting: "))
# n = int(input(" n ni kiriting: "))
# S = 1
# for i in range(1, n + 1):
#     faktorial = 1
#     for j in range(1, 2 * i + 1):
#         faktorial *= j
#     S += (-1) ** i * (x ** (2 * i)) / faktorial
# print("natija:", S)
#
# # 25. For25: x - x^2/2 + x^3/3 - ... + (-1)^(n-1) * x^n / n
# x = float(input("For25 uchun x ni kiriting: "))
# n = int(input("For25 uchun n ni kiriting: "))
# S = 0
# for i in range(1, n + 1):
#     S += (-1) ** (i - 1) * (x ** i) / i
# print("natija:", S)
#
# # 26.
# x = float(input(" x ni kiriting: "))
# n = int(input(" n ni kiriting: "))
# S = 0
# for i in range(n + 1):
#     S += (-1) ** i * (x ** (2 * i + 1)) / (2 * i + 1)
# print("natija:", S)
#
# # 27.
# n = int(input("n ni kiriting: "))
# S = 1
# for i in range(1, n + 1):
#     numerator = 1
#     denominator = 1
#     for j in range(1, i + 1):
#         numerator *= 2 * j - 1
#         denominator *= 2 * j
#     S += numerator / denominator
# print("natija:", S)
#
# # 28.
# n = int(input(" n ni kiriting: "))
# S = 1
# currentTerm = 1
# for i in range(1, n + 1):
#     currenTerm *= -1 / ((2 * i) ** 2)
#     S += currenTerm
# print(" natija:", S)
#
# # 29.
# # A = float(input(" A ni kiriting: "))
# B = float(input(" B ni kiriting: "))
# n = int(input(" n ni kiriting: "))
# h = (B - A) / n
# points = []
# for i in range(n + 1):
#     points.append(A + i * h)
# print("natija:", points)
# print("🔴")
# print("🟡")
# print("🟢")
# print("⚫️")

# import os
# import time
# while True:
#     os.system("clear")
#     print("🔴")
#     print("⚫️")
#     print("⚫️")
#
#     time.sleep(6)
#     os.system('clear')
#     print("⚫️")
#     print("🟡")
#     print("⚫️")
#     time.sleep(2.5)
#
#     for _ in range(3):
#         os.system('clear')
#         print("⚫️")
#         print("🟡")
#         print("⚫️")
#         time.sleep(1 / 2)
#         os.system('clear')
#         print("⚫️")
#         print("⚫️")
#         print("⚫️")
#         time.sleep(1 / 2)
#         os.system('clear')
#
#     os.system('clear')
#     print("⚫️")
#     print("⚫️")
#     print("🟢")
#     time.sleep(6)
#     os.system('clear')
#     print("⚫️")
#     print("🟡")
#     print("⚫️")
#     time.sleep(2.5)
#
#     for _ in range(3):
#         os.system('clear')
#         print("⚫️")
#         print("🟡")
#         print("⚫️")
#         time.sleep(1 / 2)
#         os.system('clear')
#         print("⚫️")
#         print("⚫️")
#         print("⚫️")
#         time.sleep(1 / 2)
#         os.system('clear')






