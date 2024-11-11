import random
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

bot = telebot.TeleBot('8191049181:AAGpqs9BQ_BJVa8oeNhsvPFDNxbfcc9BtrI')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "اهلا, استخدم `ابدا` أو `الشخصيات` لبدء تشغيل البوت", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "الشخصيات" or message.text == "ابدا")
def send_welcome(message):
    username = message.from_user.username if message.from_user.username else "لا يوجد اسم مستخدم"
    bot.send_message(
        message.chat.id, 
        f":عذرا[{message.from_user.first_name}](https://t.me/{username})"
        f" يرجى الانتظار ثلاث ثواني بعد الضغطة، البوت يتأخر قليلاً لأغراض الأمان.\n",
        parse_mode="Markdown"
    )
    time.sleep(2)
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

    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    bot.send_message(message.chat.id, "اختر شخصية🌚", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    time.sleep(2)

    if call.from_user.id == call.message.chat.id:

        if call.data == "button1":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1188", caption="[ابن هاشم](https://t.me/K_4x1)\nمبرمج مصمم طالب مدرسي يشتغل بالعطور ويلعب جيم \n دائما مشغول لان يشتغل 33 ساعة باليوم", parse_mode="Markdown")
        elif call.data == "button2":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1189", caption="[لبن](https://t.me/qgojj)\nشخص من الموصل متوحد منبوذ \n غثيث غالبا بس متواضع اكثر من ابن هاشم", parse_mode="Markdown")
        elif call.data == "button3":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1190", caption="[هاكس](https://t.me/c7cce)\nمتسلط عنصري ضد الرجال ودائما هوه حق ما يحب يتحايز للخطأ \n شخصية قيادية", parse_mode="Markdown")
        elif call.data == "button4":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1202", caption="[ياسر الواع](https://t.me/pxjpx)قائد قوات الشتبوست ومؤسس الجيل الذهبي \n انعرف فتره ب عداوته وي ابو علوش ومساعد", parse_mode="Markdown")  
        elif call.data == "button5":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1191", caption="[الولائي](https://t.me/x1_ri)خوش شخص وبنفس الوقت مو خوش \n عنده سيارات ويحب يشارك صورهن بالكروب وهذا السبب الي يخلي العالم تشوفه غثيث \n جان اسمه محمد وصار مرتضئ راسب بالسادس 5 سنوات", parse_mode="Markdown")
        elif call.data == "button6":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1200", caption="[مقتدئ](https://t.me/hiz8s)\nانسان نظيف ادمي \n مشكلتة الوحيده ماعنده مؤنث كله مذكر \n مره يحجي وي وعد يكول الها شبيك غبي", parse_mode="Markdown")
        elif call.data == "button7":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1193", caption="[زيد](https://t.me/myzaiid)\nخوش انسان بس اذا ما تتعارك وياه اول علاقتكم مراح يكون صديقك \n علاقته بكروب ياسر 4 سنوات ومحد يعرفه لهسه", parse_mode="Markdown")
        elif call.data == "button8":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1199", caption="[باترك](https://t.me/MePatrick)\nغامض واغلب المرات اعتقد راح يختلف علينة لان ماعدنه عليه معلومه حقيقية \n الاساطير تكول صوتة بس الله يعرفه وصورته كذلك \n مرات يسوي انتحال ل امير البصراوي ويطلع للشارع", parse_mode="Markdown")
        elif call.data == "button9":
            bot.send_photo(call.message.chat.id, "https://t.me/VIPABH/1201", caption="[امير البصراوي](https://t.me/xcxx1x)\nالكشاخ مال الكروب \n مشكلتة ميعرف ياخذ صور \n من بداية فجر التاريخ ليومك هاذ مدير وماعتقد يصعد", parse_mode="Markdown")
    else:
        bot.send_message(call.message.chat.id, "لا يمكنك التفاعل مع هذا الزر.")

while True:
    try:
        bot.polling(none_stop=True)  # إذا حدث خطأ، سيستمر البوت في العمل
    except Exception as e:
        print(f"حدث خطأ: {e}")
        time.sleep(15)  # الانتظار لفترة قصيرة قبل محاولة إعادة التشغيل
