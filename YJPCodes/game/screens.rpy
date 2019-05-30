init offset = -1
style default:
    properties gui.text_properties()
    language gui.language
style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False
style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
style gui_text:
    properties gui.text_properties("interface")
style button:
    properties gui.button_properties("button")
style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
style prompt_text is gui_text:
    properties gui.text_properties("prompt")
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"
style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"
style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)
screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
init python:
    config.character_id_prefixes.append('namebox')
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue
style namebox is default
style namebox_label is say_label
style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)
style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding
style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos
            text prompt style "input_prompt"
            input id "input"
style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action
define config.narrator_menu = True
style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_vbox:
    xalign .5 yalign .85 spacing gui.choice_spacing
style choice_button is default:
    properties gui.button_properties("choice_button")
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        textbutton _("Start") action Start()
        textbutton _("Gallery") action ShowMenu("gallery")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)
style navigation_button is gui_button
style navigation_button_text is gui_button_text
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
screen main_menu():
    tag menu
    style_prefix "main_menu"
    add gui.main_menu_background
    add "main_bottom" size(1920,240) ypos 840
    frame:
        pass
    use navigation
    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"
            text "[build_date] - V[config.version]\n© YGGDRASIL STUDIO":
                style "main_menu_version"
    hbox align(.027,.957):
        textbutton _("Original photo by\nrawpixel on Pixabay") action OpenURL("https://pixabay.com/photos/typewriter-alphabet-vintage-2306479/")
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_frame:
    xsize 420
    yfill True
    background "gui/overlay/main_menu.webp"
style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30
style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
style main_menu_title:
    properties gui.text_properties("title")
style main_menu_version:
    properties gui.text_properties("version")
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude
    use navigation
    textbutton _("Return"):
        style "return_button"
        action Return()
    label title
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text
style return_button is navigation_button
style return_button_text is navigation_button_text
style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background "gui/overlay/game_menu.webp"
style game_menu_navigation_frame:
    xsize 420
    yfill True
style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15
style game_menu_viewport:
    xsize 1380
style game_menu_vscrollbar:
    unscrollable gui.unscrollable
style game_menu_side:
    spacing 15
style game_menu_label:
    xpos 75
    ysize 180
style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
screen jigsaw():
    key "rollback" action [[]]
    key "rollforward" action [[]]
    default thumb = None
    $ preview_scale = .563
    $ preview = im.FactorScale(current_file, preview_scale)
    $ number_of_pieces = (grid_width*grid_height)
    if chosen_img == 'together_0001.webp':
        $ photographer = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/achievement-agreement-asian-3390228/"
    if chosen_img == "together_0002.webp":
        $ photographer = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/achievement-agreement-business-3481967/"
    if chosen_img == "together_0003.webp":
        $ photographer = "Original by Pexels on Pixabay"
        $ photourl = "https://pixabay.com/photos/adult-couple-walking-boots-1867702/"
    if chosen_img == "together_0004.webp":
        $ photographer = "Original by nukul2533_0 on Pixabay"
        $ photourl = "https://pixabay.com/photos/adult-couple-walking-boots-3764571/"
    if chosen_img == "together_0005.webp":
        $ photographer = "Original by Pexels on Pixabay"
        $ photourl = "https://pixabay.com/photos/adventure-mountain-lake-alps-couple-2179256/"
    if chosen_img == "together_0006.webp":
        $ photographer = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/aerial-view-art-colorful-craft-2264407/"
    if chosen_img == "together_0007.webp":
        $ photographer = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/analyzing-brainstorming-business-3385076/"
    if chosen_img == "together_0008.webp":
        $ photographer = "Original by LUM3N on Pixabay"
        $ photourl = "https://pixabay.com/photos/arts-crafts-group-wood-craft-1578128/"
    if chosen_img == "together_0009.webp":
        $ photographer = "Original by 2429905 on Pixabay"
        $ photourl = "https://pixabay.com/photos/asian-wedding-party-people-friends-1341650/"
    if chosen_img == "together_0010.webp":
        $ photographer = "Original by 5477687 on Pixabay"
        $ photourl = "https://pixabay.com/photos/asian-women-culture-costume-adult-2392281/"
    if chosen_img == "together_0011.webp":
        $ photographer = "Original by PublicDomainPictures on Pixabay"
        $ photourl = "https://pixabay.com/photos/baby-child-cute-dad-daddy-family-22194/"
    if chosen_img == "together_0012.webp":
        $ photographer = "Original by SarahRichterArt on Pixabay"
        $ photourl = "https://pixabay.com/photos/baby-dog-animal-cute-pet-puppies-3858285/"
    if chosen_img == "together_0013.webp":
        $ photographer = "Original by Olichel on Pixabay"
        $ photourl = "https://pixabay.com/photos/best-friends-childhood-girls-young-914826/"
    if chosen_img == "together_0014.webp":
        $ photographer = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/blanket-cheerful-cup-embracing-2642601/"
    if chosen_img == "together_0015.webp":
        $ photographer = "Original by skeeze on Pixabay"
        $ photourl = "https://pixabay.com/photos/boat-teamwork-training-exercise-606187/"
    if chosen_img == "together_0016.webp":
        $ photographer = "Original by JimboChan on Pixabay"
        $ photourl = "https://pixabay.com/photos/caravan-camels-adventure-sahara-1146133/"
    add "#ffffff7f" size(img_width,img_height) pos(190,190)
    add "dim"
    add "frame" pos(20,30)
    add "puzzle_bottom" size(1920,140) ypos 940
    draggroup:
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s%s"%(i,j)
                $ my_x = i*int(active_area_size*x_scale_index)+puzzle_field_offset
                $ my_y = j*int(active_area_size*y_scale_index)+puzzle_field_offset
                drag:
                    drag_name name
                    child im.Scale("gui/_blank_space.webp", int(active_area_size*x_scale_index), int(active_area_size*y_scale_index) )
                    draggable False
                    xpos my_x ypos my_y
        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s%s piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]
    if thumb == True:
        add preview pos(1350,700)
        if photographer is not None:
            textbutton photographer action OpenURL([photourl]) align(.98,.99)
    hbox xpos .02 yalign .957 spacing 10:
        textbutton _("Return") action If(replay_j == True, true=[SetVariable("replay_j", None), SetVariable("gview", None), SetVariable("chosen_img", None), ShowMenu("gallery")], false=If(gview == None, true=If(retry_r == None, false=[SetVariable("retry_r", None), MainMenu(confirm=False)], true=MainMenu(confirm=False)), false=[SetVariable("gview", None), SetVariable("chosen_img", None), ShowMenu("gallery")]))
        textbutton _("Preview") action If(thumb == None, true=SetScreenVariable("thumb", True), false=SetScreenVariable("thumb", None))
    if persistent.count_set == 1:
        hbox align(.5,.942):
            timer 1.0 repeat True action If(count_time > 0, true=SetVariable('count_time', count_time - 1), false=[Hide("countdown"), Jump("game_over")])
            if count_time <=9:
                text str(count_time) size 72 color "#FF0000" at count_time_hurryup
            elif count_time <=29:
                text str(count_time) size 48 at count_time_hurry
            else:
                text str(count_time) size 48 at count_time_normal
screen gallery():
    tag menu
    use game_menu(_("Gallery"), scroll="viewport"):
        grid g_r g_c:
            xfill True
            yspacing 25
            for g_i in j_i:
                if renpy.seen_image(g_i):
                    imagebutton idle "images_small/"+g_i hover_background "#99ccff" action [SetVariable("gview", g_i), g.Action(name=g_i)] xsize 324 ysize 184
                else:
                    imagebutton idle im.Grayscale("images_small/"+g_i) hover_background "#99ccff" action [SetVariable("gview", g_i), Jump("start")] xsize 324 ysize 184
screen gallery_navigation():
    style_prefix "main_menu"
    add "gall_bottom" size(1920,216) ypos 864
    if gview == 'together_0001.webp':
        $ gphoto = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/achievement-agreement-asian-3390228/"
    if gview == "together_0002.webp":
        $ gphoto = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/achievement-agreement-business-3481967/"
    if gview == "together_0003.webp":
        $ gphoto = "Original by Pexels on Pixabay"
        $ photourl = "https://pixabay.com/photos/adult-couple-walking-boots-1867702/"
    if gview == "together_0004.webp":
        $ gphoto = "Original by nukul2533_0 on Pixabay"
        $ photourl = "https://pixabay.com/photos/adult-couple-walking-boots-3764571/"
    if gview == "together_0005.webp":
        $ gphoto = "Original by Pexels on Pixabay"
        $ photourl = "https://pixabay.com/photos/adventure-mountain-lake-alps-couple-2179256/"
    if gview == "together_0006.webp":
        $ gphoto = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/aerial-view-art-colorful-craft-2264407/"
    if gview == "together_0007.webp":
        $ gphoto = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/analyzing-brainstorming-business-3385076/"
    if gview == "together_0008.webp":
        $ gphoto = "Original by LUM3N on Pixabay"
        $ photourl = "https://pixabay.com/photos/arts-crafts-group-wood-craft-1578128/"
    if gview == "together_0009.webp":
        $ gphoto = "Original by 2429905 on Pixabay"
        $ photourl = "https://pixabay.com/photos/asian-wedding-party-people-friends-1341650/"
    if gview == "together_0010.webp":
        $ gphoto = "Original by 5477687 on Pixabay"
        $ photourl = "https://pixabay.com/photos/asian-women-culture-costume-adult-2392281/"
    if gview == "together_0011.webp":
        $ gphoto = "Original by PublicDomainPictures on Pixabay"
        $ photourl = "https://pixabay.com/photos/baby-child-cute-dad-daddy-family-22194/"
    if gview == "together_0012.webp":
        $ gphoto = "Original by SarahRichterArt on Pixabay"
        $ photourl = "https://pixabay.com/photos/baby-dog-animal-cute-pet-puppies-3858285/"
    if gview == "together_0013.webp":
        $ gphoto = "Original by Olichel on Pixabay"
        $ photourl = "https://pixabay.com/photos/best-friends-childhood-girls-young-914826/"
    if gview == "together_0014.webp":
        $ gphoto = "Original by rawpixel on Pixabay"
        $ photourl = "https://pixabay.com/photos/blanket-cheerful-cup-embracing-2642601/"
    if gview == "together_0015.webp":
        $ gphoto = "Original by skeeze on Pixabay"
        $ photourl = "https://pixabay.com/photos/boat-teamwork-training-exercise-606187/"
    if gview == "together_0016.webp":
        $ gphoto = "Original by JimboChan on Pixabay"
        $ photourl = "https://pixabay.com/photos/caravan-camels-adventure-sahara-1146133/"
    vbox:
        if gview is not None:
            button action OpenURL(photourl):
                text gphoto:
                    style "main_menu_title" size 48
        text "[config.name!t]\n© YGGDRASIL STUDIO":
            style "main_menu_version"
    hbox align(.03,.957):
        textbutton _("Return") action g.Return()
        textbutton _("Replay") action [SetVariable("chosen_img", gview), SetVariable("replay_j", True), Jump("start")]
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            hbox:
                textbutton _("About") action SetVariable("licenses", 0)
                textbutton _("Credits") action SetVariable("licenses", 1)
                textbutton _("{color=#99ccff}Licenses:{/color}") action None
                textbutton _("Code") action SetVariable("licenses", 2)
                textbutton _("Ren'Py") action SetVariable("licenses", 3)
                textbutton _("Assets") action SetVariable("licenses", 4)
            null height (2 * gui.pref_spacing)
            if licenses == 0:
                label "[config.name!t]"
                text _("Version [config.version!t]\n")
                text _("Created with {a=https://www.renpy.org}Ren'Py{/a} [renpy.version_only]\n\n[gui.ren_license!t]\n")
                text "[gui.about!t]"
            if licenses == 1:
                text "[gui.credits!t]"
            if licenses == 2:
                text "[gui.code_license!t]"
            if licenses == 3:
                text "[gui.renpy_license!t]"
            if licenses == 4:
                text "[gui.assets!t]"
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size
style about_bar:
    xmaximum 512
screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("Pieces")
                    grid 4 2:
                        textbutton ("9") action [SetField(persistent, "pieces_set", 3), SetField(persistent, "count_timer_range", 30)]
                        textbutton ("16") action [SetField(persistent, "pieces_set", 4), SetField(persistent, "count_timer_range", 60)]
                        textbutton ("25") action [SetField(persistent, "pieces_set", 5), SetField(persistent, "count_timer_range", 100)]
                        textbutton ("36") action [SetField(persistent, "pieces_set", 6), SetField(persistent, "count_timer_range", 180)]
                        textbutton ("49") action [SetField(persistent, "pieces_set", 7), SetField(persistent, "count_timer_range", 300)]
                        textbutton ("64") action [SetField(persistent, "pieces_set", 8), SetField(persistent, "count_timer_range", 420)]
                        textbutton ("72") action [SetField(persistent, "pieces_set", 9), SetField(persistent, "count_timer_range", 600)]
                        textbutton ("100") action [SetField(persistent, "pieces_set", 10), SetField(persistent, "count_timer_range", 1200)]
                vbox:
                    style_prefix "radio"
                    label _("Time Attack")
                    textbutton _("On") action SetField(persistent, "count_set", 1)
                    textbutton _("Off") action SetField(persistent, "count_set", 0)
            null height (4 * gui.pref_spacing)
            hbox:
                box_wrap True
                vbox:
                    style_prefix "slider"
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", "pat.opus")
                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox
style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox
style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox
style mute_all_button is check_button
style mute_all_button_text is check_button_text
style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
style pref_label_text:
    yalign 1.0
style pref_vbox:
    xsize 338
style radio_vbox:
    spacing gui.pref_button_spacing
style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.webp"
style radio_button_text:
    properties gui.button_text_properties("radio_button")
style check_vbox:
    spacing gui.pref_button_spacing
style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.webp"
style check_button_text:
    properties gui.button_text_properties("check_button")
style slider_slider:
    xsize 525
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
style slider_button_text:
    properties gui.button_text_properties("slider_button")
style slider_vbox:
    xsize 675
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.webp"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 150
                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
    key "game_menu" action no_action
style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text
style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
style confirm_button:
    properties gui.button_properties("confirm_button")
style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
screen notify(message):
    zorder 100
    style_prefix "notify"
    frame at notify_appear:
        text "[message!tq]"
    timer 3.25 action Hide('notify')
transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0
style notify_frame is empty
style notify_text is gui_text
style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding
style notify_text:
    properties gui.text_properties("notify")
style pref_vbox:
    variant "medium"
    xsize 675
style window:
    variant "small"
    background "gui/phone/textbox.webp"
style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"
style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"
style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"
style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"
style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"
style game_menu_navigation_frame:
    variant "small"
    xsize 510
style game_menu_content_frame:
    variant "small"
    top_margin 0
style pref_vbox:
    variant "small"
    xsize 600
style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)
style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)
style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"
style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"
style slider_pref_vbox:
    variant "small"
    xsize None
style slider_pref_slider:
    variant "small"
    xsize 900
