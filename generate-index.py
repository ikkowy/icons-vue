#!/usr/bin/env python3

import json
import os

template = open("./lib/index.js.template", "r").read()

icons_json = json.loads(open("./node_modules/@ikkowy/icons/icons.json").read())

def get_component_name(name):
    return "".join(map(lambda s: s.capitalize(), name.split("-")))

imports = ""
installs = ""

for name in icons_json:
    icon = icons_json[name]
    for look in icon["look"]:
        module = f"@ikkowy/icons/{look}/SVG/{name}.svg?component"
        component = "IwyIcon" + get_component_name(name) + look.capitalize() + "Svg"
        imports += f"import {component} from \"{module}\";\n"
        installs += f"    app.component(\"{component}\", {component});\n"

template = template.replace("$[IMPORTS];\n", imports).replace("$[INSTALLS];\n", installs)

open("./lib/index.js", "w").write(template)
