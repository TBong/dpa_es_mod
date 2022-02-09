label gudermes:
    call gudermes_prolog
    call gudermes_day1
    jump th_demo_wip
    return

label gudermes_prolog:
    "Гудермес."
    $ dpaNewChapter(0, "Пролог: \"Гудермес\"")
    stop music fadeout 2
    show palatka with dissolve
    kp "Считай тебе крупно \"повезло\", тебя там не должно быть, но обстоятельсва сложились так."
    gg "А что нужно делать?"
    kp "На месте все скажут."
    kp "Готовься, твой путь завтра начнется."
    gg "Понял."
    "Меня малех насторожили его слова{w}, хотя если так надо, значит будет."
    "Но все же я уже здесь, давать заднюю нет смысла{w}. Хотя даже если бы дал, то сам себе не простил."
    hide palatka with dissolve
    scene childhood_memories
    "Послушав командира я отправился «домой» в ангар."
    "Идя до места в моей голове начали всплывать воспоминания о детстве."
    $ ch_memories = "fish"
    show prologue_dream with dissolve2
    "Как я, будучи 8 летним парнишкой, ходил ловить рыбу с друзьями, у бабушки в деревне."
    "Андрюха выловил тогда огромного карася, зажарили его прям там же, на костре."
    "Какой же он был сочный и вкусный, с шикарной корочкой. Эх хотелось бы ещё раз вкусить эту рыбку прямиком из тех времен."
    play music song_liric fadein 2
    $ ch_memories = "futbol1"
    "Как играл в футбол, как мы обыгрывали пацанов старше нас на года 2-3, хоть и с малым перевесом в один гол."
    "Как целеустремленно бежал к воротам что бы забить гол."
    "Но гребаные шнурки не дали мне это сделать, камнем обрушив меня на траву.{w} Вымозался же я тогда, даже от матери выслушивал, но за то гордый своей{w}, нет{w}, нашей победой."
    $ ch_memories = "grib"
    "Как ходил с дедом в лес за грибами."
    "Хах, у меня дно корзинки ели закрывалось, а он каким то волшебным образом умудрялся найти на две.{w} Вертуоз тихой охоты, что ещё сказать."
    $ ch_memories = "forest"
    "Потом я смотрел как бабуля закатывала эти лисички и опята в банки. Хоть душа к грибам не особо распологает, но именно её заготовки я уплетал за обе щёки всегда."
    $ ch_memories = "stadion"
    "Как впервые ездил на футбольный матч Уралмаш - Днепр. Было столько эмоций, ведь клуб родного края выиграл со счетом 4:1."
    "Отец меня в тот день на спине катал."
    "..."
    "Хорошо быть ребёнком весь мир яркий и насыщенный, все вещи кажуться каким то невероятным чудом, никаких забот, никакой ответственности..."
    stop music fadeout 2
    $ renpy.pause(1)
    $ ch_memories = "defolt"
    "С удовольствием вернулся бы в те времена, на один денек...{w=1} Хотя нет, не стал бы, воспоминания всегда лучше, чем переживать тоже самое несколько раз."

    hide prologue_dream with dissolve
    scene angar with dissolve
    "За то время пока на меня нахлынули воспоминания я дошел до ангара, как раз уже смеркалось, да и силы куда то вдруг иссякли."
    "Видимо размяк под давлением столь приятных чувств."
    scene black with dissolve
    $ dpaNewChapter(0, "Гудермес день 0: \"Сон\"")
    "Только я прилег и меня окутали чары Морфея."
    $ set_mode_nvl()
    play music song_liric2 fadein 1
    "На волне памяти о детсве мне вспомнился дед."
    "Его седые волосы, пышные, но акуратные усы..."
    "Но с ним было что то не то{w}, не было той жизнерадостной улыбки, не было того огня в глазах, который мог расжечь других{w}, ни разу таким его не видел."
    "Его лицо было озабоченно чем то тягостным, в нем читались нотки жалости и сожиления, в глаза было страшно смотреть, они будто тебя пожирали изнутри, в зрачках непросветная тьма."
    "Я попытался с ним заговорить."
    ggnvl "Дедуш, что с тобой?"
    "В ответ тишина...{w} Он зыркнул на меня и я провалился в пустоту"
    "Я попытался проснуться{w}, не получилось, сон не хотел отпускать меня. Но мириться я с этим не собирался, пытался снова и снова, снова и снова, но четно..."
    $ set_mode_adv()
    nvl clear
    return

label gudermes_day1:
    stop music fadeout 2
    $ renpy.pause(3)
    $ dpaNewChapter(0, "Гудермес день 1: \"Начало\"")
    scene angar with dissolve
    "Получилось только под утро. После подобных кошмаров на утро чувствуешь себя не ладно во всех смыслах, но сегодняшним утром единсвенным последствием было какая то липкая тягота в разуме."
    play music song_rising_sun volume 0.8 fadein 2
    "От того что бы начать переваривать всю эту странную ситуацию меня отвлек хлопок по плечу."
    sol_gen "Что хмурной такой?"
    "Я обернулся и увидел перед собой сбитого и коренастого молодого парня, с огромной лыбой на перевес, наверное года на два младьше."
    show gen normal smile with dissolve
    # Нужен спрайт для Гены
    gg "Невыспался малех."
    sol_gen "Верю, такая же бодяга. Как зовут то хоть?"
    gg "Саша."
    sol_gen "Меня Гена, приятно."
    $ gen_fp += 1
    gen "Что тебя сюда привело то?"
    gg "Решил глазами своими глянуть, что тут да как. А сам то как мотивирован?"
    gen "Да примерно тоже самое... Тебя к слову куда направили?"
    gg "Гудермес."
    gen "О, ну значит не я один такой \"счастливчик\". Сам до недопер с чего туда то."
    gg "А что там такого?"
    gen "Да хрен его знает, у кого не спрашивал, все что то кривятся, но ничего, ни точ что дельного, а вообще не говорят. Мутная тема."
    gg "Понял."
    "Малех бесячий парень, но пойдет, да и дружелюбный."
    gen "К слову, не хочешь партейку перекинуть?"
    menu:
        "А почему бы и нет.":
            $ humanity += 1
            $ gen_fp += 1
            gen "Отлично, сейчас все организуем."
            "Из-за пазухи он достал колоду карт, я взял табурет, это был наш импровизированный стол. Гена перетусовал карты, раздал по 6 штук, козырем были буби."
            gen "Подкидной?"
            gg "Давай."
            gg "У меня девять буби."
            gen "Восемь, я хожу."
            "Игра началась."
            "На столе появились шестерки черви и пики, я отбился. Откинув три восьмерки я потихоньку начал улыбаться{w}, как тут он выкидывает козырь"
            gen "Бейся."
            gg "Э, мы ведь без переводного."
            gen "Затроил малех, извеняюсь."
            "Он улыбнулся и забрал карту обратно..."
            "..."
            "..."
            "Гена выиграл."
            stop music fadeout 4
            "Час за игрой прошел будто 5 минут, я абсолютно абстрогировался от своих мыслей, за это время."
            gen "Во малорик, терь не с такой кислой рожей ходить будешь."
            gg "Ага, а ты хорош. Частень поигрывал?"
            gen "Да так, переодически перекидылася с друзьями."
        "Не особо.":
            gen "Как знаешь."
            "Упав на спальное место, я погрузился в свои думы."
            "Пытаясь обварить все что мне приснилось, к чему вообще это произошло."
            "Такими темпами я закимарил, примерно на час. Но все же я отпустил эту ситуацию."
    "Минут 5 спустя, нас начали собирать для отправления в Гудермес."
    ofic "Ну что готовы, хлопцы?"
    "Никто ничего не успел ответить, как он выдал."
    ofic "Правильно, раз приехали сюда, значит готовы изначально."
    scene train with dissolve
    ofic "Загружайтесь."
    play sound hitting_iron
    scene train_open at zoom_to(4,0.20,0.34,2) with dissolve
    "Мы с Геной и ещё тремя парнями прыгнули в грузовой вагон. Странный выбор транспорта, ну наверно так надо.{w} Возможно я единственный заметил что с губ офицера сорвался шепот..."
    # Сделать зум к центру
    scene train_inside_pic with dissolve2
    ofic "{color=#666}С Богом...{/color}"
    "Состав тронулся."
    play music train_inside_music volume 0.5 fadein 2
    "Напротив меня сидел Гена."
    gen "Тоже это увидел?"
    gg "Что \"это\"?"
    gen "Шепот офицера."
    gg "Да. Напрягают такие фразы."
    gen "Как раз таки нет, пока веришь, все тебя обойдет стороной, главное от души."
    gg "Приму к сведенью."
    scene train_inside_pic at zoom_to(3,0.10,0.13,1.5)
    "Я оторвал залипнувший взгляд от пола и глянул на открывающийся вид."
    scene goriScetch with dissolve
    "Это было прекрасное зрелище, величественные горы с редким , голубое небо с пушистыми облаками."
    sol "Ну что, есть у кого нибудь карты?"
    gen "А тож. Партейку?"
    sol "Подключайтесь."
    "Все начали играть в карты, что бы скоротать часок другой. А я только и смотрел на живую картину."
    gen "Сань, погнали с нами."
    gg "Успею ещё с вами наиграться."
    sol "Не лови менжу, погнали разок. Все равно без интереса играем."
    gg "Не могу, картина через чур завораживающая."
    sol "А, так ты залепон словил, больше не беспокою."
    "Поля орашались солнечным светом, блестали, играли золтом. Давно я такого не видел, но все же красоты родного Урала мне больше по душе."
    "Так прошел час."
    gg "Играете до сих пор?"
    gen "Атож. С нами хочешь?"
    gg "Глупый вопрос, Ген."
    gen "Да ладно, что ты так сразу, я же в шутку."
    sol "Сейчас партейку добъем и можешь."
    scene train_inside_pic with dissolve
    "Я встал и наблюдал как доигрывается колода, Гена тип везучий, вся рука в козырях, от туза до десятки. По итогу вечно улыбающийся выиграл."
    show gen normal smile
    gen "Оп и все."
    sol "Да как так то, уже третий раз. Фартовый ты тип."
    gg "На меня раздать не забудьте."
    gen "Обязательно забудем."
    "Карты раскидали на троих, остальным надоело играть. Ну а как ту не надоест, когда тебя в дураках оставляют."
    #Сюда бы сделать анимацию игры в карты, это самое изи так то
    # Хочется спрайт для Гены да и пикчи с ним
    "Меня ни как не мог оставить вопрос почему этот солдат так разговаривает. Я решил спросить, за игрой будет проще начать диалог."
    menu:
        "Узнать":
            gg "Слушай, а почему так жаргон используешь, сидел что-ли?"
            sol "Судьба так сыграла, вырос я в таком месте, где все так общаются, если не все то большинство. Как ты понял, на кичи я не чалился."
            sol "Не умею по другому. А тебе это как то давит?"
            $ humanity += 1
            gg "Да нет, просто услышал, любопытсво возникло."
            gen "Не доводит любопытсво до хорошего."
            gg "Возможно, хотя те же великие ученые, не любопытсво случаем их привело к такому?"
            gen "Это исключения, а я смониваюсь что все мы тут такие исключительные..."
            show gen mournful
            "Веселое лицо Гены куда то испарилось, вместо него теперь был Генадий, серьёзный от мозга костей, по крайней мере по его лицу можно было только это сказать."
            "Партия подходила к концу, остались только мы с Геной."
            gg "А вдруг, может быть мы исключения."
            gen "Не знаю как ты, но я точно мимо этого прохожу.."
            gg "Эй, с тобой все нормально?"
            "В этот момент я кинул пикового вальта. У меня осталась одна карта."
            gen "Да проебал я, впервые за три года. Беру."
            show gen laught
            "И вдруг огонек опять зажёгся, лико превратилось в моську, Гена \"вернулся обратно\". Почему то я абсолютно уверен, что дело не в проигрыше."
            gg "Ну держи последнюю, шестерочку."
            show gen normal smile
        "Промолчать":
            "Игра продолжилась, я не решил испытывать удачу, хрен его знает что у этого парня на уме."
            "В партии остались только я с Геной. В колоде ничего не осталось, на руках остались последнии карты."
            "Я выкинул вальта пики. Гена поморщился, но взял."
    gen "Хах, вот и все. Как раз карты надоели, а то пять тут кругов тут и ещё три до отправки - это гемор."
    "Я отправился смотреть на пейзаж."
    hide gen normal smile
    hide train_inside_pic with dissolve
    show goriScetch with dissolve
    "Таким образом прошло три часа, оставалось ехать где то минут тридцать."
    "Я вернулся к своему привычному делу, смотреть на пейзаж. С детсва не мог воспринимать информацию на слух, только зрение, благо оно у меня отменное."
    "..."
    # Тут можно скрол рызных пейзажиков
    "Прибыли. Один паренек даже закимарил."
    "Состав начал сбовлять ход, видимо мы практически на месте."
    hide goriScetch with dissolve
    scene train_inside_pic with dissolve
    "Я прилег, прекрыв глаза..."
    "Мой отдых прирвал возглыс."
    sol "О вот и вокзал."
    "Взяв все что у нас было мы вывалились из вагона, перед нами предстал какой то тип."
    hide train_inside_pic with dissolve
    scene train_open with dissolve
    show rs furious
    show rs furious blik
    show rs furious
    sol_rs "КАКОГО ХЕРА?!{w} Вы как сюда попали, блять?!{w} Каки блядским образом?!"
    "Мы опешили, непонимая что делать"
    sol_rs "Ало, вы в уши долбитесь? Ответ где."
    "Гена решил срезать углы."
    gen "Нас с Маздока отправили. Посадили в вагон и мы поехали."
    sol_rs "Ебаные разгельдяи, нихера не могут сделать нормально. В любом случае, за мной дуйте, сейчас с вами разберемся."
    $ dpaNewChapter(0, "Гудермес день 1: \"Вокзал\"")
    return