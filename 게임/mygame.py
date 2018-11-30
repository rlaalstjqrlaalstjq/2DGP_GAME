import game_framework
import pico2d

import title_stage

pico2d.open_canvas(1565, 700,sync=True)
game_framework.run(title_stage)
pico2d.close_canvas()