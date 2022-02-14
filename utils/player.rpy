init 10 python:
    selected_track = -1
    loop_track = False
    track_name = "Null"
    renpy.music.register_channel("dpa_music_player", "music")
    renpy.music.set_pause(True, "dpa_music_player")
    
    def getSelectedTrackPath():
        return dpa_music_list[list(dpa_music_list)[selected_track]]

    def setTrackName():
        tmpSel = list(dpa_music_list)[selected_track]
        global track_name
        track_name = dpa_music_names[str(tmpSel)]
    
    def getTrackName():
        return track_name

    def getNextTrack():
        if selected_track == -1:
            return
        if not loop_track: 
            selected_track += 1
            if selected_track >= len(dpa_music_list):
                global selected_track
                selected_track = 0
        renpy.music.queue(getSelectedTrackPath(),channel='dpa_music_player', loop=loop_track, clear_queue=True)
        setTrackName()
    
    def toTrackBA(num):
        selected_track += num
        global selected_track
        if selected_track >= len(dpa_music_list):
            selected_track = 0
        elif selected_track < 0:
            selected_track = len(dpa_music_list) - 1
        renpy.music.stop("dpa_music_player")
        renpy.music.queue(getSelectedTrackPath(), channel='dpa_music_player', loop=loop_track, clear_queue=True)
        setTrackName()
    
    def isNonePlaying():
        if renpy.music.get_playing("dpa_music_player") == None:
            getNextTrack()

    def nextTrack():
        toTrackBA(1)
    
    def prevTrack():
        toTrackBA(-1)

    def dpaPlLoop():
        global loop_track
        loop_track = not loop_track
    
    def randomFirst():
        if selected_track == -1:
            toTrackBA(renpy.random.randint(1, len(dpa_music_list)))
    
    def resetDPAPlayer():
        global selected_track
        selected_track = -1
        global loop_track
        loop_track = False
        renpy.music.stop("dpa_music_player")

screen dpa_player:
    imagebutton xalign 0.42 ypos 150:
        auto getFile("image/screens/player/player_back_%s.png")
        action [Function(prevTrack)]
    imagebutton xalign 0.5 ypos 150:
        auto getFile("image/screens/player/player_play_%s.png")
        selected not renpy.music.get_pause("dpa_music_player")
        action [Function(randomFirst), PauseAudio("dpa_music_player", value="toggle")]
    imagebutton xalign 0.58 ypos 150:
        auto getFile("image/screens/player/player_next_%s.png")
        action [Function(nextTrack)]
    text getTrackName():
        xalign 0.5 
        ypos 120
        size 30
    timer 0.1 repeat True action [Function(setTrackName), Function(isNonePlaying)]


# 
# из 7 дл
# screen music_7dl(engine=sdl_mus_engine, default_music):
    # modal True

    # add "sdl_mus_screen_main"

    # # Плеер
    # add get_image_7dl("gui/music/mus_player.png") xalign 0.5 ypos 126
    # imagebutton xpos 980 ypos 199:
    #     auto get_image_7dl("gui/music/buttons/mus_prev_%s.png")
    #     activate_sound sdl_achv_click
    #     action [sdl_mus_room.Previous(), Function(engine.update_cur_track)]
    # imagebutton xpos 1046 ypos 199:
    #     auto get_image_7dl("gui/music/buttons/mus_play_%s.png")
    #     activate_sound sdl_achv_click
    #     selected not renpy.music.get_pause()
    #     action [PauseAudio("music", value="toggle")]
    # imagebutton xpos 1112 ypos 199:
    #     auto get_image_7dl("gui/music/buttons/mus_next_%s.png")
    #     activate_sound sdl_achv_click
    #     action [sdl_mus_room.Next(), Function(engine.update_cur_track)]
    # imagebutton xpos 1046 ypos 265:
    #     auto get_image_7dl("gui/music/buttons/mus_shuffle_%s.png")
    #     activate_sound sdl_achv_click
    #     action [sdl_mus_room.ToggleShuffle()]
    # imagebutton xpos 1046 ypos 133:
    #     auto get_image_7dl("gui/music/buttons/mus_loop_%s.png")
    #     activate_sound sdl_achv_click
    #     selected sdl_mus_room.single_track
    #     action [If(sdl_mus_room.loop, true=If(sdl_mus_room.single_track, true=[sdl_mus_room.SetLoop(False), sdl_mus_room.SetSingleTrack(False)], false=sdl_mus_room.SetSingleTrack(True)), false=sdl_mus_room.SetLoop(True))]
    # if sdl_mus_room.shuffle:
    #     add get_image_7dl("gui/music/indicators/mus_ind_shuffle.png") xpos 908 ypos 207
    # if sdl_mus_room.loop:
    #     if sdl_mus_room.single_track:
    #         add get_image_7dl("gui/music/indicators/mus_ind_loop_one.png") xpos 884 ypos 207
    #     else:
    #         add get_image_7dl("gui/music/indicators/mus_ind_loop_all.png") xpos 884 ypos 207

    # # Свернуть
    # imagebutton xpos 1145 ypos 128:
    #     auto get_image_7dl("gui/music/buttons/mus_min_%s.png")
    #     activate_sound sdl_achv_click
    #     action [Hide("music_7dl", transition=Dissolve(0.2))]

    # # Выключение
    # imagebutton xpos 1191 ypos 186:
    #     auto get_image_7dl("gui/music/buttons/mus_off_%s.png")
    #     activate_sound sdl_achv_click
    #     action [sdl_mus_room.Stop(), Hide("music_7dl", transition=Dissolve(0.2)), SetField(engine, "is_active", False), Play('music', default_music, fadein=3)]

    # # Название текущего трека
    # viewport id "vp_track" area (702, 174, 227, 35):
    #     xadjustment engine.cur_file_adj
    #     text engine.cur_file_name style "sdl_mus_current_font"
    # text engine.get_cur_file_pos() style "sdl_mus_current_font" xpos 702 ypos 205
    # # Таймер для обновления текущей позиции в треке и бегущей строки
    # timer 0.1 repeat True action [Function(engine.update_cur_file_pos), Function(engine.update_ticker)]

    # # Прогресс бар текущего трека
    # bar xpos 667 ypos 254:
    #     if renpy.version(tuple=False) == "Ren'Py 7.3.5.606":
    #         value FieldValue(engine, "cur_file_pos", engine.cur_file_len, action=Function(engine.set_cur_file_pos))
    #     else:
    #         value FieldValue(engine, "cur_file_pos", engine.cur_file_len)
    #     left_bar  Frame(get_image_7dl("gui/music/bars/mus_bar_full.png"), 12, 12)
    #     right_bar Frame(get_image_7dl("gui/music/bars/mus_bar_null.png"), 12, 12)
    #     thumb       get_image_7dl("gui/music/bars/mus_bar_thumb_idle.png")
    #     hover_thumb get_image_7dl("gui/music/bars/mus_bar_thumb_hover.png")
    #     xmaximum 280
    #     ymaximum 12

    # # Плейлист
    # add get_image_7dl("gui/music/frames/mus_frame_playlist.png") xalign 0.5 ypos 301

    # side "c r":
    #     xpos 664
    #     ypos 327
    #     xysize (599, 585)

    #     default sdl_mus_bar_value = ui.adjustment()
    #     viewport id "vp_playlist":
    #         mousewheel True
    #         yadjustment sdl_mus_bar_value

    #         has vbox spacing 2

    #         for name, file in sorted(music_list_7dl.iteritems())[engine.page_cur * SDL_MUS_PAGE_SIZE : (engine.page_cur + 1) * SDL_MUS_PAGE_SIZE]:
    #             if renpy.seen_audio(file):
    #                 button style "sdl_mus_playlist_button":
    #                     viewport xsize 561:
    #                         text name style "sdl_mus_playlist_font"
    #                     action [sdl_mus_room.Play(file), Function(sdl_mus_engine.update_cur_track)]
    #             else:
    #                 text " ?????" style "sdl_mus_playlist_font"

    #     vbar:
    #         value YScrollValue("vp_playlist")
    #         top_bar    Frame(get_image_7dl("gui/music/bars/mus_vbar_full.png"), 12, 12)
    #         bottom_bar Frame(get_image_7dl("gui/music/bars/mus_vbar_null.png"), 12, 12)
    #         thumb       get_image_7dl("gui/music/bars/mus_bar_thumb_idle.png")
    #         hover_thumb get_image_7dl("gui/music/bars/mus_bar_thumb_hover.png")
    #         unscrollable "hide"

    # # Стрелки
    # if engine.page_cur > 0:
    #     imagebutton:
    #         auto get_image_7dl("gui/music/buttons/mus_arrow_left_%s.png") xcenter 860 ypos 927
    #         activate_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
    #         action [Function(engine.cur_page_dec), Function(sdl_mus_bar_value.change, 0)]
    # if len(music_list_7dl) > ((engine.page_cur + 1) * SDL_MUS_PAGE_SIZE):
    #     imagebutton:
    #         auto get_image_7dl("gui/music/buttons/mus_arrow_right_%s.png") xcenter 1060 ypos 927
    #         activate_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
    #         action [Function(engine.cur_page_inc), Function(sdl_mus_bar_value.change, 0)]
    # text engine.get_cur_page() style "sdl_mus_page_font" xcenter 0.5 ypos 923

    # on "show" action [SetField(engine, "is_active", True), Function(engine.update_cur_track)]


        

    