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
    stop music
    pause (2)
    scene angar with dissolve
    "Этой ночью один из экипажей сбили над перевалом, и еще неизвестно, кто выжил."
    "По этому случаю летуны были ужасно злы и желали нам поскорее добраться до чеченцев, чтобы вырезать их всех до единого и поголовно:{w} и мирных и немирных."
    "Посидев еще пол часа я отправился спать."
    stop music fadeout 1
    pause (1)
    scene gruz200_memories
    $ g2_memories = "g2"
    "И снились мне ребята, которых выгружали из вертушки."
    "Ведь только школу окончили, а уже на войне погибли."
    return

label argun_day1:
    $ dpaNewChapter(0, "Аргун день 1:\"Вылет\"")
    scene mi8 with dissolve
    pause (2)
    "Утром мы уже грузились на «Борт»."
    "Он оказался таким крохотным, что мы все едва смогли в нем поместиться."
    play music mi8_1
    scene mi8_in1 with dissolve
    "Мы погрузили все вещи и спустя 15 минут взлетели."
    call random_alert_call 
    "Пролетая Аргунское ущелье меня начало клонить в сон, не смотря на гул внутри вертолета..."
    scene black with dissolve2
    if canEventPlay(20):
        "Как вдруг пилот закричал:"
        scene mi8_in2
        pil "{b} БЛЯТЬ! {/b}"
        "Вертолёт начал резко менять свой курс."
        play sound hit
        "Как вдруг я услышал незнакомый мне звук."
        scene mi8_in2 at fall
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
        "Я не понимал что делать. Уши будто заложило."
        "Практически никаких звуков не было слышно."
        "Я начал чувствовать слабость по всему телу,{w} всё вокруг начало терять краски,{w} сознание затуманивалось."
        $ renpy.movie_cutscene(getFile("movie/movie2.webm"))
        $ dpaNewChapter(0, "Аргун эпилог:\"Конец?\"")
        scene anim prolog_1 with dissolve
        th "И это всё?"
        th "Я заканчиваю на этом? Прямо сейчас?"
        th "Так скоропостижно и бесславно?"
        #qte
        th "А хотя...{w} Что я могу с этим поделать, что могу изменить?"
        th "Правильно, Н И Ч Е Г О, от слова совсем."
        th "Придеться смириться."
        th "Конец так конец..."
        #титры xD
    else:
        "Не судьба"
    return
    

    