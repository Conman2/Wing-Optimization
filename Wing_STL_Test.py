import machupX
import json 

input_file = 'Wings/Wing_Setup.json'

scene = machupX.Scene(input_file)

scene.export_stl(filename="Wing.stl")