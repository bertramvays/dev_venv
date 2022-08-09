import simple_draw as sd
import draw_wall
from draw_figures import triangle
import draw_smile
import draw_tree
import draw_rainbow


sd.resolution = (1000, 800)
draw_rainbow.draw_rainbow()
sd.rectangle(sd.get_point(300, 0), sd.get_point(650, 400), width=1)
draw_wall.draw_wall()
sd.rectangle(sd.get_point(400, 200), sd.get_point(550, 300), color=sd.COLOR_WHITE)
triangle(sd.get_point(250, 400), 0, 450, )
draw_smile.smile(475, 250, sd.COLOR_CYAN)
draw_tree.draw_tree(sd.get_point(800, 500), 90, 50, 1)
draw_tree.draw_tree(sd.get_point(800, 35), 90, 60, 1)
draw_tree.draw_tree(sd.get_point(80, 60), 85, 45, 1)
sd.pause()
