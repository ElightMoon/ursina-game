from ursina import *
window = Ursina()

object_1 =  Entity(model = "cube",color = color.blue)
def update():
	object_1.x	+= held_keys["d"]*0.1
	object_1.x  -= held_keys["a"]*0.1
	object_1.y  += held_keys["w"]*0.1
	object_1.y  -= held_keys["s"]*0.1
	object_1.x	+= held_keys["right arrow"]*0.1
	object_1.x  -= held_keys["left arrow"]*0.1
	object_1.y  += held_keys["up arrow"]*0.1
	object_1.y  -= held_keys["down arrow"]*0.1
window.run()