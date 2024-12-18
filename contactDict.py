addContactList = [] 

def menu():
    print("Amallardan  birini tanlang: ")
    print()
    print("1.Yangi kontakt qo'shish.")
    print("2.Kontaktni yangilash.")
    print("3.Kontaktni o'chirish.")
    print("4.Kontakt qidirish.")
    print("5.Barcha kontaktlarni ko'rsatish.")
    print("6.Chiqish")


def ShowAllcontact(contacts):
   print("\n\n")
   for contact in contacts:
      for key, valu in contact.items():
         print(f"{key}:{valu}")
      print()
   print("\n\n")
while True:
    menu()
    userValue = int(input("Amalni kiriting: "))

    def addcontact():
        name = input("Kontakt ismini kiritng: ")
        number = input("Telefon raqaminni kiritng: ")
        email = input("emailni kiritng: ")
        adress = input("manzilni kiritng: ")
        contacts = {
            "name": name,
            "number": number,
            "email": email,
            "adress": adress
        }
        addContactList.append(contacts)
        print("Kontakt saqlandi")

    def refresh():
        refreshName = input("Qaysi kontaktning malumotini yangilamoqchisiz? (ismni kiriting) ")
        for contact in addContactList:
            if contact["name"] == refreshName:  
                print(f"{refreshName} kontakt topildi!")
                print(f"Eski ma'lumotlar: {contact}")
                field = input("Qaysi ma'lumotni yangilamoqchisiz? (name, number, email, adress): ")
                if field in contact:
                    newValue = input(f"Yangi {field} ni kiriting: ")
                    contact[field] = newValue 
                    print(f"{field} yangilandi: {contact}")
                else:
                    print("Noto'g'ri maydon.")
                break

        else:
            print(f"{refreshName} kontakt topilmadi.")
    def removeContact():
      removeName = input("Qaysi kontaktning malumotini o'chirmoqchisiz? (ismni kiriting) ")
      for contacts in addContactList:
             if contacts["name"] == removeName:  
                  print(f"{removeName} kontakt topildi!")
                  print(f"Eski ma'lumotlar: {contacts}")
                  field = input("Qaysi ma'lumotni o'chirmoqchisiz? (name, number, email, adress): ")
                  if field in contacts:
                     contacts.pop(field)
                     
                     
                     print(f"{field} ochirildi: {contacts}")
                  else:
                     print("Noto'g'ri maydon.")
                  break

             else:
               print(f"{removeName} kontakt topilmadi.")          
    def search(addContactList, serach):
      returningContacts = []
      for i in addContactList:
         for v in i.values():
            if v == serach or serach in v:
               returningContacts.append(i)

      return (returningContacts)




    if userValue == 1:
        addcontact()
    elif userValue == 2:
        refresh()
    elif userValue == 3:
         removeContact()
    elif userValue == 4:
      searchpattern = input("qidiruvmatni: ")
      data = search(addContactList, searchpattern)
      if data != []:
         ShowAllcontact(data)
    elif userValue == 5:
        print("Barcha kontaktlar:")
        ShowAllcontact(addContactList)
    elif userValue == 6:
        print("Dastur yakunlandi...")
        break  

