import os
from lxml import etree
import cairosvg


def update_svg_position(input_svg, output_svg, dx, dy):
    tree = etree.parse(input_svg)
    root = tree.getroot()
    for element in root.findall('.//{http://www.w3.org/2000/svg}g'):
        if 'transform' in element.attrib:
            transform = element.attrib['transform']
            new_transform = transform.replace("translate(0, 0)", f"translate({dx}, {dy})")
            element.attrib['transform'] = new_transform
    tree.write(output_svg)

def make_gif(seconds, frame_dir):
    pass

input_svg = "inkscape_svg/drawing.svg"
frames = 10
output_dir = "frames"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(frames):
    dx = i * 10
    dy = i * 10
    output_svg = os.path.join(output_dir, f"frame_{i}.svg")
    update_svg_position(input_svg, output_svg, dx, dy)
    cairosvg.svg2png(url=output_svg, write_to=os.path.join(output_dir, f"frame_{i}.png"))
