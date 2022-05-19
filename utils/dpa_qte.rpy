#qte
screen qte_start(pressed_key, time):
    add "qte_anim_button" xalign 0.5 yalign 0.5
    key pressed_key action [ Hide("qte_start"), Return() ] 
    text "{font=[furore]}[pressed_key]" xalign 0.5 yalign 0.5 size 380 color "#c51d1d"
    text "{font=[furore]}Жми [pressed_key] что бы вернуться!" align(0.5, 0.85) size 60
    timer time action [ Hide("qte_start"), SetVariable("qte_loose", True), Return() ]

# Трансформы для рации (считай легаси, юзаються только в дисклеймере) 
transform ra_disclaimer:
    zoom 0.9 pos (545, 0)
    pause (2)
    linear 1.5 zoom 0.1 pos (0, 7)

transform random_alert_transform:
    zoom 0.1 pos (0, 7)

# Лейбл qte, чекает фин иль луз
label qte_label(count=1, time=2):
    $ qte_count = count
    while qte_count > 0:
        if qte_loose:
            pass
        else:
            call screen qte_start(dpa_get_random_button(),time)
        $ qte_count -= 1
    return

python early:
    random_alert_visible = False
    need_play_sound_for_random_event = False

    # Вызов и скрытие виджета
    def call_random_event_widghet():
        SetVariable("random_alert_visible",True)

    def hide_random_event_widghet():
        SetVariable("random_alert_visible",False)
    
    # Прокрутка шанса вызова рандом ивента
    def canEventPlay(probability):
        rolled = renpy.random.randint(1, 100)
        hide_random_event_widghet()
        return rolled <= probability

    # Проигрывает пип епт
    def play_ra_sound():
        if not need_play_sound_for_random_event:
            return
        renpy.play(ra_sound,channel="sound")
        SetVariable("need_play_sound_for_random_event", False)

    # Сам виджет оповеда о рандом ивенте
    def random_alert_widghet():
        if not random_alert_visible:
            if not need_play_sound_for_random_event:
                ui.timer(0.1, SetVariable("need_play_sound_for_random_event", True))
            return
        else:
            ui.imagebutton("random_alert_for_widget", clicked=None, xpos=0, ypos=7)
            ui.timer(0.1,play_ra_sound())
    
    config.overlay_functions.append(random_alert_widghet)