label prolog:
    $ new_chapter(0, u"Пролог: \"Речь президента\"")
    stop music fadeout 2
    play music fon1
    show eltsin1 with dissolve2
    elt "Дорогие сограждане!"
    elt "Сегодня 11 декабря 1994 г. на территории Чеченской Республики введены подразделения войск Министерства внутренних дел и Министерства обороны Российской Федерации."
    elt "Действия Правительства вызваны угрозой целостности России, безопасности ее граждан как в Чечне так и за ее пределами, возможностью дестабилизации политической и экономической ситуации."
    elt "Наша цель состоит в том, чтобы найти политическое решение проблем одного из субъектов Российской Федерации{w} - Чеченской Республики,{w} защитить ее граждан от вооруженного экстремизма."
    elt "Но сейчас мирным переговорам, свободному волеизъявлению чеченского народа препятствует нависшая опасность полномасштабной гражданской войны в Чеченской Республике."
    elt "На 12 декабря 1994 г. намечены переговоры между представителями России и Чечни. Мы должны предотвратить их срыв."
    elt "Чтобы наладить в Чечне нормальную жизнь, необходимы конструктивное сотрудничество всех ветвей власти и отечественных политических сил России, взвешенность и точность оценок."
    elt "Намерен завтра обратится в Федеральному Собранию с предложением совместно уточнить рамочные условия для проведения переговоров."
    elt "Правительству поручено действовать в соответствии с Конституцией и законами Российской Федерации, с учетом сложившейся обстановки.{w} Как Президент буду следить за соблюдением Конституции и Закона."
    elt "Обязываю всех должностных лиц, ответственных за проведение мероприятий по восстановлению в Чеченской Республике конституционного порядка,{w} не применять насилия против мирного населения, взять его под свою защиту."
    elt "Напоминаю, что до 15 декабря 1994 г. в соответствии с моим Указом действует амнистия для всех добровольно сдавших оружие."
    elt "Обращаюсь к гражданам России чеченской национальности. Уверен, что вскоре вы сможете сами, в мирных условиях, решить судьбу своего народа. Рассчитываю на вашу мудрость."
    elt "Воины России!{w} Знайте, что выполняя свой долг, защищая целостность нашей страны и спокойствие ее граждан, вы находитесь под защитой российского государства, его Конституции и законов."
    elt "В восстановлении мира на территории Чечни заинтересован весь народ республики, все россияне.{w} Уверен, что только на этой основе могут быть решены проблемы, которые сегодня кажутся неразрешенными."
    
    hide eltsin1 with dissolve2 
    show gazeta1 with dissolve2
    "Любые войны выворачивают наизнанку и наши представления о действительности, и саму нашу речь.{w} Но война, которую Россия вела в Чечне, отличалась особой гротескностью."
    "В 1994 г. президент Борис Ельцин из чисто конъюнктурных соображений направил российские войска, чтобы силой свергнуть сепаратистское правительство в Чеченской республике на юге страны."
    "Официально в задачу военных входило 'восстановление конституционного порядка' и 'разоружение бандформирований'."
    "Однако корреспондентам, освещающим этот конфликт, было ясно:{w} Ельцинское решение приведет к катастрофе - прежде всего потому, что российские вооруженные силы представляли собой пугающее скопище недисциплинированных людей."
    stop music fadeout 2
    hide gazeta1 with dissolve2
    $ set_mode_nvl()
    "Я – студент истфака МГУ. Вырос в военной семье: отец, дед, прадеды – офицеры. Отслужив срочную и желая доказать свою независимость, поступил в гражданский вуз, однако скоро понял, что карьера ученого меня не прельщает."
    "Захотелось послужить еще годик, чтобы решить окончательно, продолжить мне семейную династию или не стоит."
    "Так осенью 1994 года, уже на IV курсе, взял академотпуск и завербовался на контрактную службу в Российскую армию.\n"
    "Команда состоит в основном из ребят лет 30–40, но одному, самому старшему, – 47. Почти все – с боевым опытом."
    "Главным образом, конечно, афганцы. Но есть и другие: абхазцы, карабахцы, ошцы."
    "У некоторых это не вторая, а третья, четвертая или даже пятая война.\n"
    "Мне же – всего 23, я молод и беззаботен, и это мое боевое крещение."
    
    
    $ set_mode_adv()
    nvl clear
    
    $ renpy.movie_cutscene(getFile("movie/movie1.webm"))
    
    $ new_chapter(0, u"Пролог: \"Начло пути\"")
    play sound mi8
    play music song1 volume 0.3
    show airport with dissolve
    "С нами прилетели спецы из Асбеста, а также группа офицеров, как и мы, присланных для пополнения {font=[brokenFont]}D78{/font}-го полка."
    "Офицеры скучковались в сторонке.{w} В основном это были пиджаки: лейтенанты-срочники, призванные на 2 года после гражданских вузов для замещения должностей командиров взводов, которые до них занимали кадровые офицеры."
    "Можно понять, что именно взводные составили подавляющую долю в потерях среди офицерского состава в боях за Грозный."
    "Бедолаги переминались с ноги на ногу и у всех было одинаковое выражение в глазах: Как это я дошел до жизни такой?.."
    hide airport with dissolve
    show cabina with dissolve
    "Пока они озирались, спецы куда-то дружно убыли организованной толпой, а контрактники принялись разгружать гуманитарку, которой был набит до отказа наш Ан-12."
    "Мы передавали по цепочке ящики и складывали их штабелями у трапа."
    "Последним выгрузили готового в стельку немолодого капитана-доктора."
    "Отставник, афганец, взыграла у него в душе обида за державу, записался добровольцем – воевать Чечню.{w} Доктора бережно уложили на штабель гуманитарки и оставили отдыхать."
    hide cabina with dissolve
    show airport with dissolve
    play sound uaz fadein 2
    "Через минуту подкатил замызганный уазик, из него высыпала могучая кучка полковников и подполковников весьма бравого вида."
    "Нас построили, и один из них задвинул речь, из которой мы узнали, что прибыли в Моздок (а мы думали – в Сан-Франциско!), и сегодня же первой вертушкой нас доставят в Грозный."
    "Также нам сообщили, что Чечня – это зона вооруженного конфликта, где запросто могут убить, и что еще не поздно передумать."
    "Те из контрактников, кто не уверен, что сделал правильный выбор, пусть лучше прямо сейчас выйдут из строя, и они будут немедленно, этим же бортом, доставлены обратно в Екатеринбург, где смогут подать рапорта об увольнении."
    "Естественно, строй даже не шелохнулся."
    "Не для того мы столько дней через все бюрократические преграды сюда прорывались, чтобы спектакль устраивать."
    "Да и грех нам, волкам стреляным, псам войны, за спинами 18-летних срочников дома отсиживаться."
    "Чечню надо как следует наказать, чтобы другим неповадно было.{w} И нам не терпится этим заняться."
    "Из строя вдруг бухнула разнузданная реплика:"
    sol "Нахуй надо! Нам и здесь заебись!"
    "Бравый полковник ничуть не рассердился, а отечески нам заулыбался."
    "Он рассказал, что {font=[brokenFont]}D78{/font}-му здорово досталось, но что это замечательный – лучший в группировке!{w} – полк, разведрота которого брала дудаевский дворец…"
    hide airport with dissolve
    stop music fadeout 1
    "Надо ли говорить, что ни в этот день, ни на следующий мы в свою часть так и не попали."
    show anim prolog_1 with dissolve
    play sound an12 fadein 2
    "… И снилось мне, что опять летим это мы на Ан-12, иллюминаторы все разбиты и по салону разносится холодная мокрая дрянь со снегом, набивается в глаза, в уши, за шиворот."
    stop sound fadeout 2
    hide anim prolog_1 with dissolve
    play sound veter
    show angar with dissolve
    "Выбивая зубами марш, я проснулся и вспомнил, что лежу на расстеленной на бетонном полу плащ-палатке в гигантском, продуваемом всеми ветрами ангаре без окон и дверей."
    "Крыша ангара похожа на шахматное поле, сквозь белые клетки которого прямо на рожу мне сыплется та самая мокрая дрянь со снегом."
    "Горло болит, голова болит, нос не дышит, глаза слезятся…{w} Простудился чудо-богатырь."
    "Кряхтя и превозмогая немочь, лезу в вещмешок."
    "Сожрал сразу две таблетки – аспирина и бисептола, – отхлебнул из фляги ледяной водки и, откинувшись на спину, замер, тяжело дыша…"
    "Отдохнув немного, причастился еще раз, закурил и принялся обозревать вверенные мне войска."
    "Братва в муках пробуждалась, ворча и громыхая под сводами стылого ангара сердитым матом. "
    "Быстро развели костер и сварили в большом ведре суп из сухпая."
    hide angar with dissolve
    stop sound fadeout 1
    play music song2 volume 0.5 fadein 1
    show airport with dissolve
    "Позавтракав, я отправился на поиски командира полка, для того чтобы узнать куда меня отправят."
    hide airport with dissolve
    show palatka with dissolve
    "Примерно через 15 минут я нашёл его возле командирской палатки."
    "Немного поговорив с ним он пригласил меня зайти в неё."
    "Войдя я увидел офицеров сидящих перед картой."
    "Командир подошел к карте и указал на ней:"
    hide palatka with dissolve
    stop music fadeout 2
    jump dpa_combat_map
    stop music