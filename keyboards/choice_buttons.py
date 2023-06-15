from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from keyboards.callback_datas import select_callback

select = InlineKeyboardMarkup(
    inline_keyboard = [
        [
#             InlineKeyboardButton(text="Mercedes", callback_data=select_callback.new(item_name="mercedes")),
#             InlineKeyboardButton(text="BMW", callback_data=select_callback.new(item_name="bmw")),
#             InlineKeyboardButton(text="KIA", callback_data=select_callback.new(item_name="kia")),
            InlineKeyboardButton(text="Mercedes", callback_data="select:Mercedes"),
            InlineKeyboardButton(text="BMW", callback_data="select:BMW"),
            InlineKeyboardButton(text="Kia", callback_data="select:Kia"),
        ],
        [
            InlineKeyboardButton(text="Hyundai", callback_data="select:Hyundai"),
            InlineKeyboardButton(text="Toyota", callback_data="select:Toyota"),
            InlineKeyboardButton(text="Chevrolet", callback_data="select:Chevrolet"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)

mercedes = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="A Class", callback_data="select:Mercedes A"),
            InlineKeyboardButton(text="B Class", callback_data="select:Mercedes B"),
            InlineKeyboardButton(text="C Class", callback_data="select:Mercedes C"),
        ],
        [
            InlineKeyboardButton(text="E Class", callback_data="select:Mercedes E"),
            InlineKeyboardButton(text="S Class", callback_data="select:Mercedes S"),
            InlineKeyboardButton(text="ML Class", callback_data="select:Mercedes ML" ),
            InlineKeyboardButton(text="Vito", callback_data="select:Mercedes Vito" ),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)

bmw = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="BMW M3", callback_data="select:BMW M3"),
            InlineKeyboardButton(text="BMW M5", callback_data="select:BMW M5"),
            InlineKeyboardButton(text="BMW M6", callback_data="select:BMW M6"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
kia = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Rio", callback_data="select:Kia Rio"),
            InlineKeyboardButton(text="Cerato", callback_data="select:Kia Cerato"),
            InlineKeyboardButton(text="Optima", callback_data="select:Kia Optima"),
        ],
        [
            InlineKeyboardButton(text="Sportage", callback_data="select:Kia Sportage"),
            InlineKeyboardButton(text="Picanto", callback_data="select:Kia Picanto"),
            InlineKeyboardButton(text="Sorento", callback_data="select:Kia Sorento"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
hyundai = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Accent", callback_data="select:Hyundai Accent"),
            InlineKeyboardButton(text="Azera", callback_data="select:Hyundai Azera"),
            InlineKeyboardButton(text="Santa Fe", callback_data="select:Hyundai Santa Fe"),
            InlineKeyboardButton(text="Solaris", callback_data="select:Hyundai Solaris"),
        ],
        [
            InlineKeyboardButton(text="Elantra", callback_data="select:Hyundai Elantra"),
            InlineKeyboardButton(text="Turcson", callback_data="select:Hyundai Turcson"),
            InlineKeyboardButton(text="Grandeur", callback_data="select:Hyundai Grandeur"),
            InlineKeyboardButton(text="i20", callback_data="select:Hyundai i20"),
        ],
        [
            InlineKeyboardButton(text="i30", callback_data="select:Hyundai i30"),
            InlineKeyboardButton(text="i40", callback_data="select:Hyundai i40"),
            InlineKeyboardButton(text="ix35", callback_data="select:Hyundai ix35"),
            InlineKeyboardButton(text="ix55", callback_data="select:Hyundai ix55"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
toyota = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Camry", callback_data="select:Toyota Camry"),
            InlineKeyboardButton(text="Corolla", callback_data="select:Toyota Corolla"),
            InlineKeyboardButton(text="Prado", callback_data="select:Toyota Prado"),
        ],
        [
            InlineKeyboardButton(text="Land Cruiser", callback_data="select:Toyota Land Cruiser"),
            InlineKeyboardButton(text="Prius", callback_data="select:Toyota Prius"),
            InlineKeyboardButton(text="RAV 4", callback_data="select:Toyota RAV 4"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
chevrolet = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Aveo", callback_data="select:Chevrolet Aveo"),
            InlineKeyboardButton(text="Captiva", callback_data="select:Chevrolet Captiva"),
            InlineKeyboardButton(text="Cobalt", callback_data="select:Chevrolet Cobalt"),
        ],
        [
            InlineKeyboardButton(text="Cruze", callback_data="select:Chevrolet Cruze"),
            InlineKeyboardButton(text="Malibu", callback_data="select:Chevrolet Malibu"),
            InlineKeyboardButton(text="Orlando", callback_data="select:Chevrolet Orlando"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
mercedes_a = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="140", callback_data="select:Mercedes A 140"),
            InlineKeyboardButton(text="160", callback_data="select:Mercedes A 160"),
            InlineKeyboardButton(text="170", callback_data="select:Mercedes A 170"),
            InlineKeyboardButton(text="180", callback_data="select:Mercedes A 180"),
            InlineKeyboardButton(text="200", callback_data="select:Mercedes A 200"),
            InlineKeyboardButton(text="220", callback_data="select:Mercedes A 220"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
mercedes_b = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="170", callback_data="select:Mercedes B 170"),
            InlineKeyboardButton(text="180", callback_data="select:Mercedes B 180"),
            InlineKeyboardButton(text="200", callback_data="select:Mercedes B 200"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
mercedes_c = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="180", callback_data="select:Mercedes C 180"),
            InlineKeyboardButton(text="200", callback_data="select:Mercedes C 200"),
            InlineKeyboardButton(text="220", callback_data="select:Mercedes C 220"),
            InlineKeyboardButton(text="240", callback_data="select:Mercedes C 240"),
            InlineKeyboardButton(text="270", callback_data="select:Mercedes C 270"),
            InlineKeyboardButton(text="280", callback_data="select:Mercedes C 280" ),
            InlineKeyboardButton(text="300", callback_data="select:Mercedes C 300" ),
            InlineKeyboardButton(text="320", callback_data="select:Mercedes C 320" ),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
mercedes_e = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="180", callback_data="select:Mercedes E 180"),
            InlineKeyboardButton(text="200", callback_data="select:Mercedes E 200"),
            InlineKeyboardButton(text="220", callback_data="select:Mercedes E 220"),
            InlineKeyboardButton(text="240", callback_data="select:Mercedes E 240"),
            InlineKeyboardButton(text="270", callback_data="select:Mercedes E 270"),
            InlineKeyboardButton(text="280", callback_data="select:Mercedes E 280" ),
            InlineKeyboardButton(text="300", callback_data="select:Mercedes E 300" ),
            InlineKeyboardButton(text="320", callback_data="select:Mercedes E 320" ),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
mercedes_s = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="250", callback_data="select:Mercedes S 250"),
            InlineKeyboardButton(text="280", callback_data="select:Mercedes S 280"),
            InlineKeyboardButton(text="300", callback_data="select:Mercedes S 300"),
            InlineKeyboardButton(text="320", callback_data="select:Mercedes S 320"),
            InlineKeyboardButton(text="350", callback_data="select:Mercedes S 350"),
            InlineKeyboardButton(text="400", callback_data="select:Mercedes S 400" ),
            InlineKeyboardButton(text="500", callback_data="select:Mercedes S 500" ),
            InlineKeyboardButton(text="600", callback_data="select:Mercedes S 600" ),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
mercedes_ml = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="180", callback_data="select:Mercedes ML 250"),
            InlineKeyboardButton(text="200", callback_data="select:Mercedes ML 270"),
            InlineKeyboardButton(text="220", callback_data="select:Mercedes ML 300"),
            InlineKeyboardButton(text="240", callback_data="select:Mercedes ML 320"),
            InlineKeyboardButton(text="270", callback_data="select:Mercedes ML 350"),
            InlineKeyboardButton(text="280", callback_data="select:Mercedes ML 400" ),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
mercedes_vita = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="108", callback_data="select:Mercedes Vito 108"),
            InlineKeyboardButton(text="109", callback_data="select:Mercedes Vito 109"),
            InlineKeyboardButton(text="110", callback_data="select:Mercedes Vito 110"),
            InlineKeyboardButton(text="111", callback_data="select:Mercedes Vito 111"),
            InlineKeyboardButton(text="112", callback_data="select:Mercedes Vito 112"),
            InlineKeyboardButton(text="113", callback_data="select:Mercedes Vito 113" ),
            InlineKeyboardButton(text="114", callback_data="select:Mercedes Vito 114" ),
            InlineKeyboardButton(text="115", callback_data="select:Mercedes Vito 115" ),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
car_date = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="1996", callback_data="select:1996"),
            InlineKeyboardButton(text="1997", callback_data="select:1997"),
            InlineKeyboardButton(text="1998", callback_data="select:1998"),
            InlineKeyboardButton(text="1999", callback_data="select:1999"),
            InlineKeyboardButton(text="2000", callback_data="select:2000"),
            InlineKeyboardButton(text="2001", callback_data="select:2001"),
        ],
        [
            InlineKeyboardButton(text="2002", callback_data="select:2002"),
            InlineKeyboardButton(text="2003", callback_data="select:2003"),
            InlineKeyboardButton(text="2004", callback_data="select:2004"),
            InlineKeyboardButton(text="2005", callback_data="select:2005"),
            InlineKeyboardButton(text="2006", callback_data="select:2006"),
            InlineKeyboardButton(text="2007", callback_data="select:2007"),
        ],
        [
            InlineKeyboardButton(text="2008", callback_data="select:2008"),
            InlineKeyboardButton(text="2009", callback_data="select:2009"),
            InlineKeyboardButton(text="2010", callback_data="select:2010"),
            InlineKeyboardButton(text="2011", callback_data="select:2011"),
            InlineKeyboardButton(text="2012", callback_data="select:2012"),
            InlineKeyboardButton(text="2013", callback_data="select:2013"),
        ],
        [
            InlineKeyboardButton(text="2014", callback_data="select:2014"),
            InlineKeyboardButton(text="2015", callback_data="select:2015"),
            InlineKeyboardButton(text="2016", callback_data="select:2016"),
            InlineKeyboardButton(text="2017", callback_data="select:2017"),
            InlineKeyboardButton(text="2018", callback_data="select:2018"),
            InlineKeyboardButton(text="2018", callback_data="select:2019"),
        ],
        [
            InlineKeyboardButton(text="Finish", callback_data="cancel")
        ],
    ]
)
