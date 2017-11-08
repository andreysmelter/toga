""" 'DetailedList Test App'
This little program let's you check whether or not your DetailedList implementation is working the right way.
"""
import time
import toga


def build(app):
    def on_select(widget, row):
        print('row ', row, 'of widget ', widget, 'was selected.')

    def on_refresh(widget):
        print('Pull down to refresh was initialised!')

    def on_delete(widget, row):
        print('row ', row, 'of widget ', widget, 'is going to be deleted.')

    dl = toga.DetailedList(
        data=['{}: {}'.format(x['country'], x['string']) for x in bee_translation],
        on_select=on_select,
        on_delete=on_delete,
        on_refresh=on_refresh)

    return dl


def main():
    # This needs to return an object that has a main_loop() method.
    return toga.App('DetailedList Test App', 'org.pybee.example.detailedlist', startup=build)


if __name__ == '__main__':
    main().main_loop()

# Translations of the word bee. !There will be mistakes!
bee_translation = [{"locale": "af", "country": "Afrikaans", "string": "Bee"},
                   {"locale": "ar", "country": "Arabic", "string": "نحلة"},
                   {"locale": "az", "country": "Azerbaijani", "string": "Arı"},
                   {"locale": "be", "country": "Belarusian", "string": "пчала"},
                   {"locale": "bg", "country": "Bulgarian", "string": "пчела"},
                   {"locale": "bn", "country": "Bengali", "string": "মৌমাছি"},
                   {"locale": "bs", "country": "Bosnian", "string": "Bee"},
                   {"locale": "ca", "country": "Catalan", "string": "Abella"},
                   {"locale": "ceb", "country": "Cebuano", "string": "Bee"},
                   {"locale": "cs", "country": "Czech", "string": "Včela"},
                   {"locale": "cy", "country": "Welsh", "string": "Bee"},
                   {"locale": "da", "country": "Danish", "string": "Bi"},
                   {"locale": "de", "country": "German", "string": "Biene"},
                   {"locale": "el", "country": "Greek", "string": "Μέλισσα"},
                   {"locale": "en", "country": "English", "string": "Bee"},
                   {"locale": "eo", "country": "Esperanto", "string": "Bee"},
                   {"locale": "es", "country": "Spanish", "string": "abeja"},
                   {"locale": "et", "country": "Estonian", "string": "Mesilane"},
                   {"locale": "eu", "country": "Basque", "string": "Bee"},
                   {"locale": "fa", "country": "Persian", "string": "زنبور عسل"},
                   {"locale": "fi", "country": "Finnish", "string": "Mehiläinen"},
                   {"locale": "fr", "country": "French", "string": "abeille"},
                   {"locale": "ga", "country": "Irish", "string": "Bee"},
                   {"locale": "gl", "country": "Galician", "string": "Abella"},
                   {"locale": "gu", "country": "Gujarati", "string": "મધમાખી"},
                   {"locale": "ha", "country": "Hausa", "string": "Bee"},
                   {"locale": "hi", "country": "Hindi", "string": "मधुमक्खी"},
                   {"locale": "hmn", "country": "Hmong", "string": "Bee"},
                   {"locale": "hr", "country": "Croatian", "string": "Pčela"},
                   {"locale": "ht", "country": "Haitian Creole", "string": "Bee"},
                   {"locale": "hu", "country": "Hungarian", "string": "Méh"},
                   {"locale": "hy", "country": "Armenian", "string": "Bee"},
                   {"locale": "id", "country": "Indonesian", "string": "Lebah"},
                   {"locale": "ig", "country": "Igbo", "string": "Bee"},
                   {"locale": "is", "country": "Icelandic", "string": "Bí"},
                   {"locale": "it", "country": "Italian", "string": "Ape"},
                   {"locale": "iw", "country": "Hebrew", "string": "דבורה"},
                   {"locale": "ja", "country": "Japanese", "string": "蜂"},
                   {"locale": "jw", "country": "Javanese", "string": "Bee"},
                   {"locale": "ka", "country": "Georgian", "string": "Bee"},
                   {"locale": "kk", "country": "Kazakh", "string": "Аралар"},
                   {"locale": "km", "country": "Khmer", "string": "សត្វឃ្មុំ"},
                   {"locale": "kn", "country": "Kannada", "string": "ಬೀ"},
                   {"locale": "ko", "country": "Korean", "string": "벌"},
                   {"locale": "la", "country": "Latin", "string": "Bee"},
                   {"locale": "lo", "country": "Lao", "string": "Bee"},
                   {"locale": "lt", "country": "Lithuanian", "string": "Bičių"},
                   {"locale": "lv", "country": "Latvian", "string": "Bee"},
                   {"locale": "mg", "country": "Malagasy", "string": "Bee"},
                   {"locale": "mi", "country": "Maori", "string": "Bee"},
                   {"locale": "mk", "country": "Macedonian", "string": "Пчела"},
                   {"locale": "ml", "country": "Malayalam", "string": "തേനീച്ച"},
                   {"locale": "mn", "country": "Mongolian", "string": "Bee"},
                   {"locale": "mr", "country": "Marathi", "string": "मधमाशी"},
                   {"locale": "ms", "country": "Malay", "string": "Lebah"},
                   {"locale": "mt", "country": "Maltese", "string": "Bee"},
                   {"locale": "my", "country": "Myanmar (Burmese)", "string": "ပျား"},
                   {"locale": "ne", "country": "Nepali", "string": "मधुमक्खी"},
                   {"locale": "nl", "country": "Dutch", "string": "Bij"},
                   {"locale": "no", "country": "Norwegian", "string": "Bie"},
                   {"locale": "ny", "country": "Chichewa", "string": "Njuchi"},
                   {"locale": "pa", "country": "Punjabi", "string": "ਬੀ"},
                   {"locale": "pl", "country": "Polish", "string": "pszczoła"},
                   {"locale": "pt", "country": "Portuguese", "string": "Abelha"},
                   {"locale": "ro", "country": "Romanian", "string": "albină"},
                   {"locale": "ru", "country": "Russian", "string": "пчелка"},
                   {"locale": "si", "country": "Sinhala", "string": "මී මැසි"},
                   {"locale": "sk", "country": "Slovak", "string": "včela"},
                   {"locale": "sl", "country": "Slovenian", "string": "Bee"},
                   {"locale": "so", "country": "Somali", "string": "Bee"},
                   {"locale": "sq", "country": "Albanian", "string": "bletë"},
                   {"locale": "sr", "country": "Serbian", "string": "Бее"},
                   {"locale": "st", "country": "Sesotho", "string": "Linotsi"},
                   {"locale": "su", "country": "Sundanese", "string": "nyiruan"},
                   {"locale": "sv", "country": "Swedish", "string": "Bi"},
                   {"locale": "sw", "country": "Swahili", "string": "Nyuki"},
                   {"locale": "ta", "country": "Tamil", "string": "தேனீ"},
                   {"locale": "te", "country": "Telugu", "string": "బీ"},
                   {"locale": "tg", "country": "Tajik", "string": "Хушк"},
                   {"locale": "th", "country": "Thai", "string": "ผึ้ง"},
                   {"locale": "tl", "country": "Filipino", "string": "Bee"},
                   {"locale": "tr", "country": "Turkish", "string": "bal arısı"},
                   {"locale": "uk", "country": "Ukrainian", "string": "Бджола"},
                   {"locale": "ur", "country": "Urdu", "string": "مکھی"},
                   {"locale": "uz", "country": "Uzbek", "string": "Ari"},
                   {"locale": "vi", "country": "Vietnamese", "string": "Con ong"},
                   {"locale": "yi", "country": "Yiddish", "string": "בי"},
                   {"locale": "yo", "country": "Yoruba", "string": "Bee"},
                   {"locale": "zh", "country": "Chinese", "string": "蜜蜂"},
                   {"locale": "zh-CN", "country": "Chinese (Simplified)", "string": "蜜蜂"},
                   {"locale": "zh-TW", "country": "Chinese (Traditional)", "string": "蜜蜂"},
                   {"locale": "zu", "country": "Zulu", "string": "Izinyosi"}]
