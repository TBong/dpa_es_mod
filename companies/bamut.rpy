label bamut:
    call bamut_prolog
    call bamut_day1
    jump th_demo_wip

label bamut_prolog:
    $ new_chapter(0, u"Пролог: \"Бамут\"")
    show combat_map
    return

label bamut_day1:
    return