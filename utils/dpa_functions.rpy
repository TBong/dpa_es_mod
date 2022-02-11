
init -1 python:
    class WrapperFunctionCallback(Action):
        def __init__(self,function,*arguments):
                self.function=function
                self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)
    
    def saveOldVisual():
        renpy.display.screen.screens[("dpa_say_gui_old",None)] = renpy.display.screen.screens[("say",None)]
        renpy.display.screen.screens[("dpa_game_menu_selector_old",None)] = renpy.display.screen.screens[("game_menu_selector",None)]
        renpy.display.screen.screens[("dpa_nvl_old",None)] = renpy.display.screen.screens[("nvl",None)]
        renpy.display.screen.screens[("dpa_choice_old",None)] = renpy.display.screen.screens[("choice",None)]

    def updVisual():
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui_reborn",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("dpa_menu_selector",None)]
        renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice",None)]
        renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl",None)]
    
    def rollbackVisual(*arg):
        renpy.display.screen.screens[("say",None)] = renpy.display.screen.screens[("dpa_say_gui_old",None)]
        renpy.display.screen.screens[("game_menu_selector",None)] = renpy.display.screen.screens[("dpa_game_menu_selector_old",None)]
        renpy.display.screen.screens[("choice",None)] = renpy.display.screen.screens[("dpa_choice_old",None)]
        renpy.display.screen.screens[("nvl",None)] = renpy.display.screen.screens[("dpa_nvl_old",None)]

    def toDefaultSettings(*arg):
        Call("initVars")
        rollbackVisual()
    
    def dpaNewChapter(dayNum, chapterName):
        dpaSetChapter(dayNum, chapterName)
        updVisual()

#Базовые функции
init -99 python:
    def getFile(file):
        return default_dpa_path + file

    def getLabelWIP(name):
        if to_steam == True:
            return "th_demo_wip"
        return name
    
    def canEventPlay(probability):
        rolled = renpy.random.randint(1, 100)
        return rolled <= probability

    def getRandomItem(items):
        num = renpy.random.randint(0, len(items)-1)
        return items[num]

    def getRandomButton():
        return getRandomItem(['1','2','3','4','5','6','7','8','9','0','z','x','c','j','i','o','b','t','h'])
    
    def dpaSetChapter(dayNum, chapterName):
        global save_name
        save_name = (u"DPA v%s: День %s %s") % (dpa_version, dayNum, chapterName)
    
    def bakeSpriteDefaultSizeSold(sizeX, sizeY, posX, posY, character, emo, special="null.png"):
        return ConditionSwitch(
        "persistent.sprite_time=='day'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='sunset'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.63, 0.78, 0.82)))

    def bakeSpriteDefaultPlusSizeSold(sizeX, sizeY, posX, posY, character, emo, special="null.png"):
        return ConditionSwitch(
        "persistent.sprite_time=='day'",
        im.MatrixColor( 
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_ps_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt_ps.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.83, 0.88, 0.92)),
        "persistent.sprite_time=='sunset'",
        im.MatrixColor(  
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_ps_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt_ps.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'",
        im.MatrixColor(  
            im.Composite((sizeX,sizeY), 
            (posX,posY), getFile("image/sprites/form_v2_ps_bottom.png"),
            (posX,posY), getFile("image/sprites/form_v2_ps_top.png"),
            (posX,posY), getFile("image/sprites/"+character),
            (posX,posY), getFile("image/sprites/form_v2_ps_middle.png"),
            (posX,posY), getFile("image/sprites/"+emo),
            (posX,posY), getFile("image/sprites/belt_ps.png"),
            (posX,posY), getFile("image/sprites/"+special)),
            im.matrix.tint(0.63, 0.78, 0.82)))
