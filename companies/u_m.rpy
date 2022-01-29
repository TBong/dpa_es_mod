label u_m:
    call u_m_prolog
    call u_m_day1
    jump th_demo_wip
    return

label u_m_prolog:
    $ new_chapter(0, u"Пролог: \"Урус-Мартан\"")
    show combat_map
    return

label u_m_day1:
    return