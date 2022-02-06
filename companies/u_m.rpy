label u_m:
    call u_m_prolog
    call u_m_day1
    jump th_demo_wip
    return

label u_m_prolog:
    "Урус-Мартан"
    $ new_chapter(0, u"Пролог: \"Урус-Мартан\"")
    stop music fadeout 2
    show palatka with dissolve
    return

label u_m_day1:
    return