init -2 python:
    _game_menu_screen = None
    os.environ['SDL_VIDEO_CENTERED'] = '1'
init python:
    import re
    class Shaker(object):
        anchors = {'top' : 0.0, 'center' : 0.5, 'bottom' : 1.0, 'left' : 0.0, 'right' : 1.0,}
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            self.start = [ self.anchors.get(i, i) for i in start ]
            self.dist = dist
            self.child = child
        def __call__(self, t, sizes):
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)
    def file_list(dir=""):
        list = renpy.list_files()
        rv = []
        for f in list:
            if re.match(dir,f):
                rv.append(f[(len(dir)):])
        return rv
    def piece_dragged(drags, drop):
        if not drop:
            return
        p_x = drags[0].drag_name[0]
        p_y = drags[0].drag_name[1]
        t_x = drop.drag_name[0]
        t_y = drop.drag_name[1]
        a = []
        a.append(drop.drag_joined)
        a.append((drags[0], 3, 3))
        drop.drag_joined(a)
        if p_x == t_x and p_y == t_y:
            renpy.play("pat.opus", channel="sound")
            my_x = int(int(p_x)*active_area_size*x_scale_index)-int(grip_size*x_scale_index)+puzzle_field_offset
            my_y = int(int(p_y)*active_area_size*y_scale_index)-int(grip_size*y_scale_index)+puzzle_field_offset
            drags[0].snap(my_x,my_y, delay=0.1)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True
            for i in range(0, grid_width):
                for j in range(0, grid_height):
                    if placedlist[i,j] == False:
                        return
            return True
        return
    g = Gallery()
    j_i = file_list("images/")
    g_r = 4
    g_c = 4
    for g_i in j_i:
        g.button(g_i)
        g.image("images_full/"+g_i)
        g.unlock(g_i)
    g.transition = dissolve
    g.navigation = True
    jigsaw = file_list('images/')
image opening = "gui/opening_0001.webp"
image main_background = "gui/background_0001.webp"
image frame = "gui/frame_0001.webp"
image menu_background = im.Blur("gui/background_0001.webp", 3)
image main_bottom = "#0008"
image puzzle_bottom = "#0008"
image gall_bottom = "#0009"
image renpy_logo = "gui/renpy_logo.webp"
image dim = "#0008"
image white = "#fff"
define grip_size = 75
define img_width = 960
define img_height = 540
define persistent.pieces_set = 4
define persistent.count_set = 0
define persistent.count_timer_range = 60
define count_timer_jump = "game_over"
define shake = renpy.curry(_Shake)
define count_time_giveup = shake((.01, .01, 0, 0), 60, dist=100)
define count_time_hurryup = shake((.01, .01, 0, 0), 60, dist=10)
define count_time_hurry = shake((.01, .01, 0, 0), 60, dist=5)
define count_time_normal = shake((.01, .01, 0, 0), 60, dist=1)
define puzzle_field_size = 960
define puzzle_field_offset = 190
define puzzle_piece_size = 450
define active_area_size = puzzle_piece_size - (grip_size * 2)
define chosen_img = None
define photographer = None
define gview = None
define replay_j = None
define replay_r = None
define retry_r = None
define licenses = 0
label splashscreen:
    scene white
    show renpy_logo at truecenter
    show expression Text("Created with Ren'Py Visual Novel Engine", yalign=.82, size=24, color="#404040")
    $ renpy.transition(Dissolve(1))
    $ renpy.pause(2, hard = True)
    return
label start:
    if replay_j is None and replay_r is None:
        $ chosen_img = None
        $ current_file = None
    scene menu_background
    show dim
    show expression Text("Cutting the image for you...", size=72) at truecenter
    pause .1
    scene main_background
    show dim
    $ grid_width = persistent.pieces_set
    $ grid_height = persistent.pieces_set
    $ count_time = persistent.count_timer_range
    if gview is not None and replay_j is None:
        $ chosen_img = gview
    elif replay_j is None and replay_r is None:
        $ chosen_img = renpy.random.choice(jigsaw)
    $ current_file = chosen_img
    python:
        img_to_play = chosen_img
        g_i = chosen_img
        x_scale_index = round( (1.00 * (img_width/grid_width)/active_area_size), 6)
        y_scale_index = round( (1.00 * (img_height/grid_height)/active_area_size), 6)
        mainimage = im.Composite((int(img_width+(grip_size*2)*x_scale_index), int(img_height+(grip_size*2)*y_scale_index)),(int(grip_size*x_scale_index), int(grip_size*y_scale_index)), img_to_play)
        top_row = []
        for i in range (0, grid_width):
            top_row.append(i)
        bottom_row = []
        for i in range (0, grid_width):
            bottom_row.append(grid_width*(grid_height-1)+i)
        left_column = []
        for i in range (0, grid_height):
            left_column.append(grid_width*i)
        right_column = []
        for i in range (0, grid_height):
            right_column.append(grid_width*i + (grid_width-1) )
        jigsaw_grid = []
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                jigsaw_grid.append([9,9,9,9])
        for i in range(0,grid_height):
            for j in range (0,grid_width):
                if grid_width*i+j not in top_row:
                    if jigsaw_grid[grid_width*(i-1)+j][2] == 1:
                        jigsaw_grid[grid_width*i+j][0] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][0] = 1
                else:
                    jigsaw_grid[grid_width*i+j][0] = 0
                if grid_width*i+j not in right_column:
                    jigsaw_grid[grid_width*i+j][1] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][1] = 0
                if grid_width*i+j not in bottom_row:
                    jigsaw_grid[grid_width*i+j][2] = renpy.random.randint(1,2)
                else:
                    jigsaw_grid[grid_width*i+j][2] = 0
                if grid_width*i+j not in left_column:
                    if jigsaw_grid[grid_width*i+j-1][1] == 1:
                        jigsaw_grid[grid_width*i+j][3] = 2
                    else:
                        jigsaw_grid[grid_width*i+j][3] = 1
                else:
                    jigsaw_grid[grid_width*i+j][3] = 0
        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        testlist = dict()
        for i in range(0,grid_width):
            for j in range (0,grid_height):
                piecelist[i,j] = [int(renpy.random.randint(0, (config.screen_width * 0.9 - puzzle_field_size))+puzzle_field_size), int(renpy.random.randint(0, (config.screen_height * 0.8)))]
                temp_img = im.Crop(mainimage, int(i*active_area_size*x_scale_index), int(j*active_area_size*y_scale_index), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))
                imagelist[i,j] = im.Composite((int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/_00%s.webp"%(jigsaw_grid[grid_width*j+i][0]),0,1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/_00%s.webp"%(jigsaw_grid[grid_width*j+i][1]),270,1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/_00%s.webp"%(jigsaw_grid[grid_width*j+i][2]),180,1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))), (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("gui/_00%s.webp"%(jigsaw_grid[grid_width*j+i][3]),90,1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))))
                placedlist[i,j] = False
    jump puzzle
label puzzle:
    if replay_r is True:
        $ replay_r = None
        $ retry_r = True
    call screen jigsaw
    jump win
label win:
    scene menu_background
    show expression img_to_play:
        truecenter
        pause .5
        linear .5 yalign .3
    with dissolve
    $ renpy.show(img_to_play)
    $ renpy.hide(img_to_play)
    menu:
        "Continue" if replay_j is None and gview is None:
            jump start
        "Play other" if retry_r is True and gview is None:
            $ retry_r = None
            jump start
        "Return":
            if retry_r is True:
                $ retry_r = None
            if replay_j is True:
                $ replay_j = None
                $ chosen_img = None
                $ gview = None
                call screen gallery
            elif gview is not None:
                $ chosen_img = None
                $ gview = None
                call screen gallery
            return
label game_over:
    scene menu_background
    show dim
    show expression Text("Game Over", size=256) at truecenter
    with Dissolve(1)
    menu:
        "Retry" if replay_j is None:
            $ replay_r = True
            jump start
        "Play other" if replay_j is None:
            $ retry_r = None
            jump start
        "Return":
            if retry_r is True:
                $ retry_r = None
            if replay_j is True:
                $ replay_j = None
                $ chosen_img = None
                $ gview = None
                call screen gallery
            elif gview is not None:
                $ chosen_img = None
                $ gview = None
                call screen gallery
            return
label renlicense:
    $ licenses = 3
    call screen about