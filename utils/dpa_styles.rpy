#Стили
init -98 python:
    style.text_save_load                          = Style(style.default)
    style.text_save_load.font                     = getFile("fonts/Furore.ttf")
    style.text_save_load.size                     = 60
    style.text_save_load.color                    = "#ffffff"
    style.text_save_load.hover_color              = "#808080"
    style.text_save_load.selected_color           = "#ffffff"
    style.text_save_load.selected_idle_color      = "#ffffff"
    style.text_save_load.selected_hover_color     = "#808080"
    style.text_save_load.insensitive_color        = "#ffffff"

    style.button_none = Style(style.button)
    style.button_none.background = None
    style.button_none.hover_background = None
    style.button_none.selected_background = None
    style.button_none.selected_hover_background = None
    style.button_none.selected_idle_background = None

    style.file_load_button = Style(style.button)
    style.file_load_button.background = getFile("image/screens/load_save/load_Button_idle.png")
    style.file_load_button.hover_background = getFile("image/screens/load_save/load_Button_hover.png")
    style.file_load_button.selected_background = getFile("image/screens/load_save/load_Button_selected.png")
    style.file_load_button.selected_hover_background = getFile("image/screens/load_save/load_Button_selected.png")
    style.file_load_button.selected_idle_background = getFile("image/screens/load_save/load_Button_selected.png")

    style.text_select_track = Style(style.default)
    style.text_select_track.color                    = "#c2c2c2"
    style.text_select_track.hover_color              = "#ffffff"
    style.text_select_track.selected_color           = "#ffffff"
    style.text_select_track.selected_idle_color      = "#ffffff"
    style.text_select_track.selected_hover_color     = "#ffffff"
    style.text_select_track.insensitive_color        = "#9e9e9e"
    style.text_select_track.size = 30



#Переменные от функция
init -97 python:
    #Шрифты
    brokenFont = getFile("fonts/old-fax.ttf")
    furore = getFile("fonts/Furore.ttf")