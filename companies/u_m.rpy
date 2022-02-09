label u_m:
    call u_m_prolog
    call u_m_day1
    jump th_demo_wip
    return

label u_m_prolog:
    "Урус-Мартан"
    $ dpaNewChapter(0, "Пролог: \"Урус-Мартан\"")
    stop music fadeout 2
    show palatka with dissolve
    return

label u_m_day1:
    return