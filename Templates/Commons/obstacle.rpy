#################################################################################################################################
#                                                                                                                               #
#          If you want to sell your MOD in Steam with the form of DLC, please contact to yggdrasilgamestudio@gmail.com.         #
#          We welcome Photographers, Illustrators, Musicians, and all INDIE creators who wish to collaborate with us.           #
#                                                                                                                               #
#################################################################################################################################

########## Replace all >>> sample <<< to your special name that start with english. ##########
########## Replace all >>> MOD name <<< to your real MOD name. ##########
########## Replace >>> MOD description <<< to your real MOD description. ##########
########## Replace all >>> your_url <<< to your real web URL that can represent you. ##########
########## Scroll down and look for starting with '#', then follow the text. ##########
########## After all, find >>> Your Name <<< and write credits, find >>> Your licenses <<< and write MOD license. ##########
init -1 python:
    mod_name.append("MOD name")
    mod_desc.append("MOD description")
    mod_image.append("sample")
    if persistent.obsplay == "sample":
        obs_src = "sample_obs"
    ########## Remove this lines below if you don't use set of obstacles. ##########
    if persistent.obsex == "sample":
        obs1 = "sample_obs1"
        obs2 = "sample_obs2"
        obs3 = "sample_obs3"
    ################################################################################
    ########## Remove this lines below if you don't use any sound effect for your obstacles. ##########
    if persistent.obsse == 1:
        obsse0 = "sample_sfx_0.opus"
        obsse1 = "sample_sfx_1.opus"
        obsse2 = "sample_sfx_2.opus"
        obsse3 = "sample_sfx_3.opus"
    ###################################################################################################
    ########## Remove this lines below if you don't use sound effect for 3, 2, 1 countdown. ##########
    if persistent.obsseex == "sample":
        obsse4 = "sample_sfx_4.opus"
        obsse5 = "sample_sfx_5.opus"
        obsse6 = "sample_sfx_6.opus"
    ##################################################################################################
define sample_scr = 0
image sample = "sample_header.webp"
########## Replace this image defines below to your Obstacle images. ##########
image sample_obs = SnowBlossom("sample_obstacle.webp", count=50, yspeed=(100, 200))
image sample_obs1 = SnowBlossom("sample_obstacle1.webp", count=50, yspeed=(100, 200))
image sample_obs2 = SnowBlossom("sample_obstacle2.webp", count=50, yspeed=(100, 200))
image sample_obs3 = SnowBlossom("sample_obstacle3.webp", count=50, yspeed=(100, 200))
###############################################################################
screen sample():
    $ mods = None
    tag menu
    use game_menu(_("MOD name"), scroll="viewport"):
        vbox:
            hbox:
                textbutton _("Theme") action SetVariable("sample_scr", 0)
                textbutton _("Credits") action SetVariable("sample_scr", 1)
                textbutton _("License") action SetVariable("sample_scr", 2)
            null height (2 * gui.pref_spacing)
        if sample_scr == 0:
            vbox:
                add "sample_theme.webp"
                ########## Use this lines below when you use one Obstacle image only. ##########
                label _("Obstacle")
                style_prefix "radio"
                textbutton _("On") action [SetField(persistent, "obsplay", "sample"), renpy.reload_script]
                textbutton _("Off") action [SetField(persistent, "obsplay", None), renpy.reload_script]
                ################################################################################
                ########## Use this lines below when you use Obstacle image set, or delete if you don't use. ##########
                label _("Obstacle Set")
                style_prefix "radio"
                textbutton _("On") action [SetField(persistent, "obsplay", "sample"), SetField(persistent, "obsex", "sample"), renpy.reload_script]
                textbutton _("Off") action [SetField(persistent, "obsplay", None), SetField(persistent, "obsex", None), renpy.reload_script]
                #######################################################################################################
                ########## Use this lines below when you use some Sound effects with Obstacle image set, or delete if you don't use. ##########
                label _("Obstacles with SFX")
                style_prefix "radio"
                textbutton _("On") action [SetField(persistent, "obsplay", "sample"), SetField(persistent, "obsex", "sample"), SetField(persistent, "obsse", 1), renpy.reload_script]
                textbutton _("Off") action [SetField(persistent, "obsplay", None), SetField(persistent, "obsex", None), SetField(persistent, "obsse", 0), renpy.reload_script]
                ###############################################################################################################################
                ########## Use this lines below when you use full Sound effects with Obstacle image set, or delete if you don't use. ##########
                label _("Full Set")
                style_prefix "radio"
                textbutton _("On") action [SetField(persistent, "obsplay", "sample"), SetField(persistent, "obsex", "sample"), SetField(persistent, "obsse", 1), SetField(persistent, "obsseex", "sample"), renpy.reload_script]
                textbutton _("Off") action [SetField(persistent, "obsplay", None), SetField(persistent, "obsex", None), SetField(persistent, "obsse", 0), SetField(persistent, "obsseex", None), renpy.reload_script]
                ###############################################################################################################################
                null height gui.pref_spacing
                text _([theme_set])
        if sample_scr == 1:
            text _p("""
            {a="your_url"}Your Name{/color} - Your part in credits

{color=#99ccff}Contributor Name(no link url){/color} - Part in credits

{a=""}Contributor Name{/a} - Part in credits
""")
        if sample_scr == 2:
            text _p("""
            Your licenses goes here.
""")