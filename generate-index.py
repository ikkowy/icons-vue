#!/usr/bin/env python3

from glob import glob
import os

template = open("./lib/index.js.template", "r").read()

svg_paths = sorted(glob("./node_modules/@ikkowy/icons/**/*.svg", recursive=True))

def get_component_name(name):
    return "".join(map(lambda s: s.capitalize(), name.split("-")))

imports = ""
installs = ""

for svg_path in svg_paths:
    module = svg_path.removeprefix("./node_modules/")
    name = os.path.basename(svg_path).removesuffix(".svg")
    look = svg_path.removeprefix("./node_modules/@ikkowy/icons/").split("/")[0]
    component = "IwyIcon" + get_component_name(name) + look.capitalize() + "Svg"

    imports += f"import {component} from \"{module}?component\";\n"
    installs += f"    app.component(\"{component}\", {component});\n"

template = template.replace("$[IMPORTS];\n", imports).replace("$[INSTALLS];\n", installs)

open("./lib/index.js", "w").write(template)
