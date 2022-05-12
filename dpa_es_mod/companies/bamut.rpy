label bamut:
    call bamut_prolog
    call bamut_day1
    jump th_demo_wip
    return

label bamut_prolog:
    "Бамут."
    $ dpaNewChapter(0, "Пролог: \"Бамут\"")
    stop music fadeout 2
    show palatka with dissolve
    return

label bamut_day1:
    return