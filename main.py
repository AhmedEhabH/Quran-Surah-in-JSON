import os

path = '/{your}/{path}/{to}/{files}' #Path
path = '/media/ahmed/New Volume/World/Quran/Naser El Qatami'

names = [
    '001 - الفاتحة',
'002 - البقرة',
'003 - آل عمران',
'004 - النساء',
'005 - المائدة',
'006 - الأنعام',
'007 - الأعراف',
'008 - الأنفال',
'009 - التوبة',
'010 - يونس',
'011 - هود',
'012 - يوسف',
'013 - الرعد',
'014 - ابراهيم',
'015 - الحجر',
'016 - النحل',
'017 - الإسراء',
'018 - الكهف',
'019 - مريم',
'020 - طه',
'021 - الأنبياء',
'022 - الحج',
'023 - المؤمنون',
'024 - النور',
'025 - الفرقان',
'026 - الشعراء',
'027 - النمل',
'028 - القصص',
'029 - العنكبوت',
'030 - الروم',
'031 - لقمان',
'032 - السجدة',
'033 - الأحزاب',
'034 - سبإ',
'035 - فاطر',
'036 - يس',
'037 - الصافات',
'038 - ص',
'039 - الزمر',
'040 - غافر',
'041 - فصلت',
'042 - الشورى',
'043 - الزخرف',
'044 - الدخان',
'045 - الجاثية',
'046 - الأحقاف',
'047 - محمد',
'048 - الفتح',
'049 - الحجرات',
'050 - ق',
'051 - الذاريات',
'052 - الطور',
'053 - النجم',
'054 - القمر',
'055 - الرحمن',
'056 - الواقعة',
'057 - الحديد',
'058 - المجادلة',
'059 - الحشر',
'060 - الممتحنة',
'061 - الصف',
'062 - الجمعة',
'063 - المنافقون',
'064 - التغابن',
'065 - الطلاق',
'066 - التحريم',
'067 - الملك',
'068 - القلم',
'069 - الحاقة',
'070 - المعارج',
'071 - نوح',
'072 - الجن',
'073 - المزمل',
'074 - المدثر',
'075 - القيامة',
'076 - الانسان',
'077 - المرسلات',
'078 - النبإ',
'079 - النازعات',
'080 - عبس',
'081 - التكوير',
'082 - الإنفطار',
'083 - المطففين',
'084 - الإنشقاق',
'085 - البروج',
'086 - الطارق',
'087 - الأعلى',
'088 - الغاشية',
'089 - الفجر',
'090 - البلد',
'091 - الشمس',
'092 - الليل',
'093 - الضحى',
'094 - الشرح',
'095 - التين',
'096 - العلق',
'097 - القدر',
'098 - البينة',
'099 - الزلزلة',
'100 - العاديات',
'101 - القارعة',
'102 - التكاثر',
'103 - العصر',
'104 - الهمزة',
'105 - الفيل',
'106 - قريش',
'107 - الماعون',
'108 - الكوثر',
'109 - الكافرون',
'110 - النصر',
'111 - المسد',
'112 - الإخلاص',
'113 - الفلق',
'114 - الناس',
]

for filename in os.listdir(path):
    index = int(filename.split('.')[0]) - 1
    os.rename(path + '/' + filename, path + '/' + names[index] + '.mp3')
    # print(filename)
