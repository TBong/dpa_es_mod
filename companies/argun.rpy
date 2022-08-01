label argun:
    call argun_prolog
    call argun_day1
    jump th_demo_wip
    return

label argun_prolog:
    "Аргун."
    $ dpaNewChapter(0, "Пролог: \"Аргун\"")
    kp "Готовься, твой “борт” вылетает завтра."
    scene gruz200 with dissolve
    play music song_na_mozdok volume 0.5 fadein 2
    "Послушав командира я отправился «домой» в ангар."
    "Подходя, увидел, что мои бойцы разгружают вертолет с грузом-200."
    "Не знаю, кто придумал красивую сказку о цинковых гробах."
    "Убитые были завернуты в шинели, плащ-палатки, одеяла и просто куски брезента.{w} Многие изуродованы ужасно, а некоторые – как будто уснули."
    "Это были первые увиденные мною трупы, и меня слегка затрясло."
    "Контрактники укладывали тела в КамАЗ и спорили, полетят они на этом вертолете или на другом, который стоял на соседнем пятачке и из которого вылезали какие-то русские бабушки и дедушки – беженцы."
    "Последним вылез худющий солдатик в грязной шинели и с рукой на перевязи."
    "Он глядел вокруг безумными глазами и, кажется, не верил своему спасению."
    "Раз сегодня мы никуда не летим, отправляемся в гости к вертолетчикам, пригласившим нас «на четыреста капель»."
    stop music fadeout 2
    pause (2)
    scene angar with dissolve
    "Этой ночью один из экипажей сбили над перевалом, и еще неизвестно, кто выжил."
    "По этому случаю летуны были ужасно злы и желали нам поскорее добраться до чеченцев, чтобы вырезать их всех до единого и поголовно:{w} и мирных и немирных."
    "Посидев еще пол часа я отправился спать."
    stop music fadeout 1
    pause (1)
    $ g2_memories = "g2"
    "И снились мне ребята, которых выгружали из вертушки."
    "Ведь только школу окончили, а уже на войне погибли."
    return

label argun_day1:
    $ dpaNewChapter(1, "Аргун:\"Вылет\"")
    scene mi8 with dissolve
    pause (2)
    "Днем мы уже грузились на «Борт»."
    "Он оказался таким крохотным, что мы все едва смогли в нем поместиться."
    play music mi8_1
    scene mi8_in1 with dissolve
    "Мы погрузили все вещи и спустя 15 минут взлетели."
    call random_alert_call 
    "Пролетая Аргунское ущелье меня начало клонить в сон, не смотря на гул внутри вертолета..."
    scene black with dissolve2
    if canEventPlay(100):
        "Ничего не предвещало беды, как вдруг пилот закричал:"
        scene mi8_in2
        pil "{b} БЛЯТЬ! {/b}"
        "Вертолёт начал резко менять свой курс."
        play sound hit
        "Я услышал приближающийся к нам незнакомый мне звук."
        scene black
        show mi8_in2 at fall
            
        "Вертолёт подпрыгнул и начал крутиться вокруг своей оси."
        "В голове ветала одна мысль."
        th "Какого?!"
        "Тело вцепилось в скамью руками."
        "Сердце отбивало чечетку,{w} будто было готово выпрыгнуть из груди."
        stop sound fadeout 2
        stop music fadeout 2
        "Меня окутал холодный пот."
        "И до меня дошло..."
        th "Ракета."
        "Я не понимал что делать.{w} Уши будто заложило."
        "Практически никаких звуков не было слышно."
        "Я начал чувствовать слабость по всему телу,{w} всё вокруг начало терять краски,{w} сознание затуманивалось."
        hide mi8_in2 with dissolve
        $ renpy.movie_cutscene(getFile("movie/movie2.webm")) 
        $ dpaNewChapter(1, "Аргун:\"Конец?\"")
        scene anim prolog_1 with dissolve
        th "И это всё?"
        th "Я заканчиваю на этом? Прямо сейчас?"
        th "Так скоропостижно и бесславно?"
        call qte_label(1,4)
        if qte_loose:
            $ qte_loose = False
            call argun_epilog
        else:
            call argun_survived
    else:
        "Не судьба"
    return

label argun_epilog:
        th "А хотя...{w} Что я могу с этим поделать, что могу изменить?"
        th "Правильно, Н И Ч Е Г О, от слова совсем."
        th "Придеться смириться."
        th "Конец так конец..."
        #титры xD
        return


label argun_survived:
    $ dpaNewChapter(1, "Аргун:\"Выживший\"")
    pause (2)
    play ambience ring fadein 2
    scene black with dissolve
    "Боль не чувствовалась, сердце стучало с сумасшедшей скоростью."
    "В ушах стоял сильный звон."
    pause (1)
    "Спустя мгновение я осознал, что лежу под обломками вертолета."
    "Я по немногу начал приходить в чувства."
    "Нога сильно болела."
    "Чувствовался запах гари."
    "Что-то тяжелое давило на меня. {w}Я попытался встать, но смог лишь приподняться на локтях."
    th "Черт!"
    "Отодвинув от себя обломки, мешавшие мне двигаться, и сделав пару движений в сторону света я оказался снаружи."
    scene mi8_crash with dissolve
    stop ambience fadeout 4
    play music song_crash fadein 2
    "Шум в ушах потихоньку начал стихать."
    "В глазах все плыло."
    "Вокруг валялись огромные обломки вертолета. Он лежал на боку, всё вокруг было перепахано."
    th "Каким чудом я выжил?"
    "Моя кожа была покрыта толстым слоем пота и грязи. Из ноги торчал большой кусок стекла."
    "Снаряжение, в отличии от тела, было цело.."
    "Превозмогая боль я пополз искать медецину."
    "Оказавшись с другой стороны вертолета моё внимание привлекла оранжевая коробочка."
    "Я подполз к ней и открыл её."
    "На КМБ меня учили как пользоваться индвивидуальной аптечкой, так что отличить обезбол мне не составило проблем."
    "Приняв таблетку кеторола я вытащил жгут из подсумка, и сжав его зубами начал дёргать осколок, торчавший из ноги."
    #красная пульсация и sfx_head_heartbeat
    th "Вылазь, сволочь!"
    "Собравшись сил я вырвал кусок из ноги. {w}Кровь начала хлестать из открытой раны."
    "Разжав зубы, я наложил жгут на рану, а затем изо всех сил затянул."
    "После всех манипуляций, морщась от боли, я начал перевязывать ногу."
    "Боль постепенно пропадала, и я смог подняться на ноги."
    "В поисках рации, дабы связаться хоть с кем нибудь, я доковылял до кабины пилота."
    "Через разбитый илюминатор было видно рацию и искарёженное тело пилота."
    "Ему оторвало обе руки, левая нога была на месте, но на половину отделена от тела."
    #звук рации
    rac "Во..дерь..от...тер...м...св...зь...Повт...ю...тер...м...св...зь"
    "После этого слышны были лишь треск и помехи, затем рация замолкла."
    th "Сука! Как мне теперь со своими связаться?!"
    "Закончив с кабиной пилота, я пошел проверять остальных."
    "Все были мертвы. {w}Глаза закрыты, лица застыли в ужасе. У всех открытые рты."
    "В общем, настоящая картина из ужастиков."
    "На одном из бойцов висел автомат."  
    "Не долго думая, я взял его, проверил магазин и перевёл оружие в одиночный режим."
    "Присев и попытавшись мыслить спокойно, я начал придумывать свой план спасения."
    th "Итак, что мы имеем? Сломанная рация, автомат, плохие знания местности и..."
    "Я прощупал разгрузку."
    th "...Аптечка и граната."
    th "Надеюсь за мной кто-нибудь да прилетит, не оставят же своих умирать тут."
    pause(3)
    th "Нет, за нами никого не пошлют, свою жопу подставлять ради спасения одного экипажа у боевиков под носом никто не будет."
    th "Значит у меня есть только один выход - идти вперёд, и надеяться, что это куда-нибудь меня приведёт."
    play sound shooting_far
    "Уже собираясь уходить, я услышал не по далеку крики и автоматную очередь где то за холмом."
    "Видимо пока я возился с аптечкой, кто-то из выживших попытался уйти. Бедняга."
    play sound ak74_fireselector_down
    "Я перевел оружие в автоматический режим и взабравшись на холм, выглянул из-за него."
    scene helichrash_combat with dissolve
    "Три боевика и лежащий на земле солдат в российской форме."
    "Русский лежал в грязи, пока Чеченцы шли к нему."
    play sound pm_far1
    "Сблизившись с солдатом, Чеченцы смеясь выстрелили ему в голову."
    gg "Уроды!"
    "Сквозь зубы прошипел я."
    "Кулаки сжались от злобы."
    th "Наверное они сейчас пойдут к вертолёту проверять уцелевших."
    "Я снял с разгрузки гранату и разогнул ей усики."
    gg "Это вам суки за пацанов!"
    play sound grenade_throw
    "Прицелевшись в боевиков, прокричал я, и кинул её."
    "Сердце на время застыло."
    "Чеченцы обыскивали убитого, и не успели среагировать на прилетевший \"подарок\"."
    play sound gren_expl1_close
    "Граната прилетела одному из боевиков прямо под ноги. Две фигуры осели на землю, третий попытался убежать, но ему это не удалось."
    play sound ak74_shooting
    "Моя автоматная очередь поразила его."
    "Последний боевик упал, вечным сном."
    pause(1)
    "Я упал спиной на холм и попытался отдышаться."
    "В кровь поступил адреналин."
    "В этот момент я понял, что попал в {font=[furore]}{color=#911010}АД."
    stop music fadeout 4
    scene black with dissolve
    pause(3)

    play ambience ambience_camp_center_night
    scene village_evening with dissolve
    "Идти мне пришлось довольно долго. Несколько раз я останавливался по пути."
    "Наконец вдали показалось небольшое полуразрушенное поселение. К моему счастью на улице никого не было."
    th "Надеюсь смогу здесь на ночь перекантоваться."
    "Подойдя к ближайшему дому я облокотился на его стену, дабы немного отдышаться."
    "Идей особо много не было, так что я надеялся найти подвал в каком либо домике."
    "Я считал, что подвал - это самое безопасное место которое можно было найти в этой глуши."
    "В своей недолгой жизни мне приходилось спать в разных местах, но только не в подвале."
    th "Как же я хочу верить, что вся эта война просто сон и не более,{w} но к сожалению суровая реальность ломает мою надежду."
    "Пройдя пару строений я вышел к небольшому домику, который стоял на окраине."
    pause(1)
    stop ambience
    scene chechen_house with dissolve
    play ambience ambience_medstation_inside_night
    "Зашёл в него и принялся осматривать помещение. Слева от входа находилась кухня, справа зал, который не отличался ничем особенным."
    "Зайдя на кухню я заметил впадину под ковром. Под ним находилась дверь в подвал."
    "Как только я её открыл, то услышал чьи-то шаги в другой комнате.{w} Я быстро отпрыгнул назад и прижавшись к стене нацелил автомат на дверной проём."
    "Кто-то осторожно взялся за ручку двери и стал её открывать."
    #звук открытия двери
    "Это оказался какой-то старик."
    "Он был худой, на его лице красовалась длинная борода."
    "Сто пудов кавказец."
    "Увидев меня, он поднял руки вверх."
    "В руках у старика не было никакого оружия. Но глаза его были полны такой злобы, что по коже у меня поползли мурашки."
    "Старец заговорил - заговорил с чеченским акцентом."
    om "Тише, тише... Опусти автомат."
    "Я не переставал целиться в него."
    "Стрелять я не хотел - все-таки он был пожилым человеком. Хотя и несколько опасным."
    " С каждой секундой я испытывал все большее волнение, а уж когда я почувствовал, что пальцы уже онемели на спусковом крючке, он принялся мне угрожать."
    om "Убери оружие!"
    om "Совсем из ума выжил! Это же Ичкерия, сын шакала! Так что даже и не думай."
    gg "Ну и что ты мне сделаешь? Порубишь на куски? Или перережешь горло?"
    om "Я тебя, сукина сына, на первом же хуторе повешу!"
    om "Как овцу порежу! Потроха вытресу!"

    menu:
        "Убить старца":
            call oldman_dead

        "Не стрелять":
            call oldman_alive

    return


label oldman_alive:
    gg "Закончил? Теперь руки за голову и лицом в пол. {w}Иначе убью!"
    om "Твоя голова будет висеть на столбе!"
    "Проговорил старик опускаясь на пол."
    gg "Вот так и лежи! И только попробуй дёрнуться!"
    om "Бид аудал!"
    play sound sfx_open_door_strong
    scene black
    show village_evening at stepping with dissolve
    play ambience ambience_forest_evening fadein 3
    "Я выскочил из халупы и побежал к концу деревни, надеясь поскорее скрыться."
    "Уже порядком стемнело и я успел несколько раз споткнуться из-за того что не видел дороги."
    scene derevnya_night with dissolve2
    "Двадцать минут спустя я уже не видел увидеть деревню."
    "Старик уже скорее всего сообщил обо мне, и меня ищут."
    play sound_loop sfx_head_heartbeat fadein 2
    "Не в силах продолжать бежать я завалился на спину и прижал автомат к груди."
    "Дышать было тяжело, руки были ватные, сердце стучало как бешенное."
    "В этот день я чуть не погиб, и единственное что мне сейчас хотелось - чтобы он по скорее закончился."
    "В голову полезли воспоминания о прежней жизни."
    scene childhood_memories
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
    $ ch_memories = "forest"
    "Как ходил с дедом в лес за грибами."
    "Хах, у меня дно корзинки ели закрывалось, а он каким то волшебным образом умудрялся найти на две.{w} Вертуоз тихой охоты, что ещё сказать."
    $ ch_memories = "grib"
    "Потом я смотрел как бабуля закатывала эти лисички и опята в банки. Хоть душа к грибам не особо распологает, но именно её заготовки я уплетал за обе щёки всегда."
    $ ch_memories = "stadion"
    "Как впервые ездил на футбольный матч Уралмаш - Днепр. Было столько эмоций, ведь клуб родного края выиграл со счетом 4:1."
    "Отец меня в тот день на спине катал."
    "..."
    "Хорошо быть ребёнком весь мир яркий и насыщенный, все вещи кажуться каким то невероятным чудом, никаких забот, никакой ответственности..."
    stop music fadeout 2
    scene derevnya_night with dissolve2
    $ renpy.pause(1)
    hide prologue_dream with dissolve
    "Спустя пол часа отдыха лёжа на спине мне немного полегчало."
    "Вдруг вдалеке за спиной послышались шаги."
    "С каждой секундой их количество увеличивалось."
    "Я попытался подняться чтобы скрыться, но не смог."
    "Действие адреналина спало и как только я наступил на раненную ногу, то сразу повалился."
    play sound sfx_bodyfall_1
    "Отчаявшись, я начал ползти."
    "Шаги всё приближались, стала слышна чеченская речь."
    play sound body_hit
    scene black
    "Последнее что я почувствовал - удар прикладом по голове."
    stop ambience fadeout 6
    window hide
    stop ambience fadeout 2
    show next_day with dissolve2
    pause (4)
    play music song_muts fadein 4 volume 0.4
    hide next_day with dissolve2
    scene kazn with dissolve2
    "Двое чеченцев волокли меня по площади. {w}Третий шёл спереди."
    "Люди вокруг смотрели на это, некоторые смеялись, некоторые нет."
    "Где-то такие же пойманные ребята пилили дрова, привязанные на цепи к ближайшему столбу, как собаки."
    "Для боевиков пленные - не люди. {w}Рабы, подобные скотине."
    "На гул людей, окруживших меня собирались зеваки."
    "Меня остановили возле пленного, такого же как я."
    "Руки у меня были связаны, все вещи с меня сняли, кроме майки и портков."
    "Один из чеченцов, стоящий к нам ближе всех выхватил нож из кармана и поднёс к моему горлу."
    "Я закрыл глаза и задержал дыхание."
    window hide
    scene black with Dissolve(3.5)
    play sound knife_hit
    pause (2)
    "Первая чеченская война сопровождалась большими людскими жертвами среди военнослужащих федеральной группировки войск."
    "В период Первой чеченской компании было убито около четырёх тысяч молодых российских солдат."
    "Однако, в их число не включены потери в ходе боевых действий в Дагестане, насчитывавшие 280 убитых человек."
    "Война изначально проводилась под лозунгом минимальных потерь, и до штурма Грозного число потерь было относительно невелико."
    jump th_demo_wip

label oldman_dead:
    "Моё терпение лопнуло."
    "Дрожащим, почти онемевшим пальцем я нажал на спусковой крючок."
    play sound ak74m_indoor
    "Старик согнулся, завалился на пол."
    play sound sfx_bodyfall_1
    "Его рот наполнился кровью, из уст доносился хрип."
    play sound sfx_open_door_strong
    stop ambience fadeout 3
    scene black
    show village_evening at stepping with dissolve
    "Я выскочил из халупы и побежал к концу деревни, надеясь поскорее скрыться."
    "Уже порядком стемнело и я успел несколько раз споткнуться из-за того что не видел дороги."
    scene derevnya_night with dissolve
    "Двадцать минут спустя я уже не видел увидеть деревню."
    play sound_loop sfx_head_heartbeat fadein 2
    "Не в силах продолжать бежать я завалился на спину и прижал автомат к груди."
    "Дышать было тяжело, руки были ватные, сердце стучало как бешенное."
    "В этот день я чуть не погиб, и единственное что мне сейчас хотелось - чтобы он по скорее закончился."
    "В голову полезли воспоминания о прежней жизни."
    stop sound_loop fadeout 2
    scene childhood_memories
    play music song_liric fadein 2
    $ ch_memories = "fish"
    show prologue_dream with dissolve2
    "Как я, будучи 8 летним парнишкой, ходил ловить рыбу с друзьями, у бабушки в деревне."
    "Андрюха выловил тогда огромного карася, зажарили его прям там же, на костре."
    "Какой же он был сочный и вкусный, с шикарной корочкой. Эх хотелось бы ещё раз вкусить эту рыбку прямиком из тех времен."
    $ ch_memories = "futbol1"
    "Как играл в футбол, как мы обыгрывали пацанов старше нас на года 2-3, хоть и с малым перевесом в один гол."
    "Как целеустремленно бежал к воротам что бы забить гол."
    "Но гребаные шнурки не дали мне это сделать, камнем обрушив меня на траву.{w} Вымозался же я тогда, даже от матери выслушивал, но за то гордый своей{w}, нет{w}, нашей победой."
    $ ch_memories = "forest"
    "Как ходил с дедом в лес за грибами."
    "Хах, у меня дно корзинки ели закрывалось, а он каким то волшебным образом умудрялся найти на две.{w} Вертуоз тихой охоты, что ещё сказать."
    $ ch_memories = "grib"
    "Потом я смотрел как бабуля закатывала эти лисички и опята в банки. Хоть душа к грибам не особо распологает, но именно её заготовки я уплетал за обе щёки всегда."
    $ ch_memories = "stadion"
    "Как впервые ездил на футбольный матч Уралмаш - Днепр. Было столько эмоций, ведь клуб родного края выиграл со счетом 4:1."
    "Отец меня в тот день на спине катал."
    "..."
    "Хорошо быть ребёнком весь мир яркий и насыщенный, все вещи кажуться каким то невероятным чудом, никаких забот, никакой ответственности..."
    stop music fadeout 2
    scene derevnya_night with dissolve2
    $ renpy.pause(1)
    hide prologue_dream with dissolve
    "Спустя пол часа отдыха лёжа на спине мне немного полегчало."
    play ambience mi8_lopasti fadein 3
    "Вдруг я услышал гулкий рёв где-то с противоположной стороны от деревни."
    "Через пару секунд стал различим звук лопостей приближающегося вертолёта."
    th "Неужели за мной прилетели?"
    stop ambience fadeout 3
    play music grob_song1 fadein 3
    scene rescue with dissolve
    "Я вскочил и залез на холм, откуда начал вглядываться в ночное небо, пытаясь разглядеть своего спасителя."
    "Благо облаков не было и лунный свет хорошо освещал местность."
    "Среди звёзд был виден силуэт вертолёта, который садился метрах в трёх ста от меня, отбрасывая тепловые ловушки где-то за очередным холмом."
    "Нежелая оставаться здесь, я побежал в его сторону, тратя свой последний остаток сил на марш-бросок."
    "Мысли о спасении придавали дополнительный заряд энергии."
    scene rescue1 with dissolve
    "С криками ''Свои!'' я выбежал к вертушке, перепугав бойцов, выстроивших круговую оборону вокруг неё."
    "Из-за всей этой суматохи в деревне, потом из-за эйфории от спасения мой организм вырабатывал столько адреналина, что я совсем забыл что у меня в ноге нехилая дырка."
    "Природа дала нам тело, которое может вынести почти все, самое главное - убедить в этом свой разум"
    scene mi8_flight with dissolve
    "Не дав сказать мне и слова меня запихнули в вертолёт."
    "Через минуту туда же посадили ещё одного бойца."
    "Форма на нём была изорвана, где-то была кровь, оружия у него не было."
    "Я спросил у него что с ним случилось. {w}Оказалось что это был ещё один выживший после крушения."
    "Ему повезло, ведь при нём была карта и рация, а очнулся он раньше меня, поэтому как можно быстрее ушёл с места падения."
    "Возможно как раз и он вызвал подмогу."
    "Все бойцы вернулись в грузовой отсек вертолёта, двери захлопнулись."
    "Мы начали взлетать. {w}В вертолёте некоторе время было молчание."
    "Через несколько минут мы уже летели над горной местностью, и я стал приставать к солдату, из группы спасения с расспросами о том, куда мы летим"
    "Он ответил, что в тыл, где меня и другого уцелевшего положат в военный госпиталь."
    gg "Хорошо всё то, что хорошо кончается."
    sol_rs "Это точно."
    window hide
    scene black with Dissolve(3.5)
    pause (2)
    "Первая чеченская война сопровождалась большими людскими жертвами среди военнослужащих федеральной группировки войск."
    "В период Первой чеченской компании было убито около четырёх тысяч молодых российских солдат."
    "Однако, в их число не включены потери в ходе боевых действий в Дагестане, насчитывавшие 280 убитых человек."
    "Война изначально проводилась под лозунгом минимальных потерь, и до штурма Грозного число потерь было относительно невелико."