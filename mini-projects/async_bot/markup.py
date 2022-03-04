from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMenu = KeyboardButton("Bosh menyu")
btnOther = KeyboardButton("Boshqa")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMenu,btnOther)

# Other Menu

pyblogBtn = KeyboardButton("Pyblog dasturlash blogi")
fullstackHelp = KeyboardButton("Full-Stack yordam guruhi")
authorBtn = KeyboardButton("Abdurahmon Rashidov - Github")

otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(pyblogBtn,authorBtn)


getContact = KeyboardButton("Raqamingizni yuboring",request_contact=True,callback_data='phone')
getContactBtn = ReplyKeyboardMarkup(resize_keyboard=True).add(getContact)