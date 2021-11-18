#!/usr/bin/env python3

'''
Make a holder for food processor blades
'''

import solid
import math

inf = 1000

XX = 26  # width
YY = 40  # depth
ZZ = 15  # height

ridge = 1
lower_scale = .8
fin_count = 24

lower_base = solid.cube([lower_scale*XX, lower_scale*YY, ridge], center=True)
lower_base = solid.translate([0,0,.5*ridge])(lower_base)

upper_base = solid.cube([XX, YY, ridge], center=True)
upper_base = solid.translate([0,0,ZZ-ridge/2])(upper_base)

base = solid.hull()(lower_base, upper_base)

# Cut out a rays from a center depth
fin = solid.linear_extrude(height=YY, scale=.01)(solid.square(YY))
fin = solid.cube(YY)
fin = solid.rotate([0,0,-45])(fin)
fin = solid.rotate([0,-90,0])(fin)
fin = solid.translate([YY,0,0])(fin)
fin = solid.rotate([0,-10,0])(fin)

fins = solid.union()([solid.rotate([0,0,360.0*i/fin_count])(fin) for i in range(fin_count)])
fins = solid.translate([0,0,ZZ*.6])(fins)

head = solid.sphere(d=.25*XX)
head = solid.scale([1,1,.7])(head)
head = solid.translate([0,.20*YY, .15*ZZ])(head)

jesus = solid.sphere(d=1)
# jesus = solid.scale([.5*XX, .7*YY, .5*ZZ])(jesus) # v1
jesus = solid.scale([10, 20, 5])(jesus) # v2
jesus = solid.minkowski()(solid.cube([2,8,1], center=True), jesus) # v2

swaddle = solid.cube(inf, center=True)
swaddle = solid.translate([inf/2-2.5, 0, 0])(swaddle)
swaddle = solid.rotate([0,45,-45])(swaddle)
swaddle_r = solid.intersection()(swaddle, solid.scale(1)(jesus))
swaddle_r = solid.rotate([0,-5,0])(swaddle_r)
swaddle_r = solid.translate([0,0,1])(swaddle_r)
swaddle = solid.rotate([0,0,-90])(swaddle)
swaddle_l = solid.intersection()(swaddle, solid.scale(1)(jesus))
swaddle_l = solid.rotate([0,10,0])(swaddle_l)
# swaddle_l = solid.translate([0,0,.5])(swaddle_l)

jesus += swaddle_l 
jesus += swaddle_r
jesus = jesus + head
jesus = solid.scale([1.2,1.2,1.2])(jesus)
jesus = solid.rotate([4,0,0])(jesus)
jesus = solid.translate([0,0,ZZ*.79])(jesus)


final = base - fins
final = final + jesus

print(solid.scad_render(final, file_header="$fn=256;"))
