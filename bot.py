import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot('8191049181:AAGpqs9BQ_BJVa8oeNhsvPFDNxbfcc9BtrI')
@bot.message_handler(func=lambda message: message.text == "الشخصيات")
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("ابن هاشم", callback_data="button1")
    button2 = InlineKeyboardButton("لبن", callback_data="button2")
    button3 = InlineKeyboardButton("هاكس", callback_data="button3")
    button4 = InlineKeyboardButton("ياسر الواع", callback_data="button4")
    button5 = InlineKeyboardButton("الولائي", callback_data="button5")
    button6 = InlineKeyboardButton("مقتدئ(cos)", callback_data="button6")
    button7 = InlineKeyboardButton("زيد", callback_data="button7")
    button8 = InlineKeyboardButton("باترك", callback_data="button8")
    button9 = InlineKeyboardButton("امير البصراوي ", callback_data="button9")

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, )
    bot.send_message(message.chat.id, "اختر شخصية🌚", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "button1":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1188", caption="[ابن هاشم](t.me/K_4x1)مبرمج مصمم طالب مدرسي يشتغل بالعطور ويلعب جيم \n دائما مشغول لان يشتغل 33 ساعة باليوم")
    elif call.data == "button2":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1189", caption="[لبن](t.me/qgojj )شخص من الموصل متوحد منبوذ \n غثيث غالبا بس متواضع اكثر من ابن هاشم ")
    elif call.data == "button3":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1190", caption="[هاكس](t.me/c7cce) \n متسلط عنصري ضد الرجال ودائما هوه حق ما يحب يتحايز للخطأ \n شخصية قيادية")
    elif call.data == "button4":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1192", caption="[ياسر الواع](t.me/pxjpx)ياسر \n قائد قوات الشتبوست ومؤسس الجيل الذهبي \n انعرف فتره ب عداوته وي ابو علوش ومساعد")  
    elif call.data == "button5":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1191", caption="[الولائي](t.me/x1_ri) الولائي خوش شخص وبنفس الوقت مو خوش \n عنده سيارات ويحب يشارك صورهن بالكروب وهذا السبب الي يخلي العالم تشوفه غثيث \n جان اسمه محمد وصار مرتضئ راسب بالسادس 5 سنوات")
    elif call.data == "button6":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1200", caption="[مقتدئ](t.me/hiz8s)انسان نظيف ادمي \n مشكلتة الوحيده ماعنده مؤنث كله مذكر \n مره يحجي وي وعد يكول الها شبيك غبي")
    elif call.data == "button7":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1193", caption="[زيد](t.me/myzaiid) \n خوش انسان بس اذا ما تتعارك وياه اول علاقتكم مراح يكون صديقك \n علاقته بكروب ياسر 4 سنوات ومحد يعرفه لهسه")
    elif call.data == "button8":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1199", caption="[باترك](t.me/MePatrick)غامض واغللب المرات اعتقد راح يختلف علينة لان ماعدنه عليه معلومه حقيقية \n الاساطير تكول صوتة بس الله يعرفه وصورته كذلك \n مرات يسوي انتحال ل امير البصراوي ويطلع للشارع")
    elif call.data == "button9":
        bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1201", caption="[امير البصراوي](t.me/xcxx1x) الكشاخ مال الكروب \n مشكلتة ميعرف ياخذ صور \n من بداية فجر التاريخ ليومك هاذ مدير وماعتقد يصعد")



bot.polling()
