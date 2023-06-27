# task 1 
# Foydalanuvchidan matn qabul qiling , unda "gaz" , "svet", "yo'q" kabi so'zlar ishtirok etganmi yoki yo'qmi aniqlang va ular sonini har birini alohida hisoblab boring so'zlar register turi yoki boshqa qoshimchalar bilan kelishi mumkin bularni ham inobatga oling

# Gaz yo'q ekan lekin svet bor svetamuzika

# gaz = 1
# svet = 2
# text = "Gaz yo'q ekan lekin svet bor svetamuzika gazini bos"
# gaz = 0
# svet = 0
# no = 0
# for t in text.split(" "):
#     if t.lower() == "gaz" or "gaz" in t.lower():
#         gaz += 1
#     if t.lower() == "svet" or "svet" in t.lower():
#         svet += 1
#     if t.lower() == "yo'q":
#         no += 1
# print(f"\ngaz={gaz}\nsvet={svet}\nno={no}")

# task 2 
# quyidagi shartlarni tekshirib parol togri yoki notogriligini aniqlaydigan dastur tuzing
# password:
#     - minimum 6 ta belgi 
#     - kamida bitta katta harf 
#     - kamida bitta maxsus belgi (/,\,@,/,_,-)

# v = "Salom#Qalesan#Alik#"
# l = len(v)
# card = "8600 1600 2530 1535"
# c = 0
# result = ""

# for n in card.split(" "):
#     if c == 3:
#         result += n 
#     else:
#         result += "**** "
#         c += 1
# print(result)

# task 3 
# n soni berilgan (30 > n > 0) 0 dan n gacha bo'lgan sonlarni orasida probellar bilan chiqaring agar son toq bo'lsa bitta probel bilan uni keyingi son orasini belgilaysiz agar juft bo'lsa 2 ta probel bilan. misol : 0  1 2  3 4  5