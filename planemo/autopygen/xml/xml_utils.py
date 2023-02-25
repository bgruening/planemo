from typing import Optional, List
from lxml import etree
from planemo.autopygen.param_info import ParamInfo


def options(param_info: ParamInfo) -> etree._Element:
    if param_info.choices is None:
        return param(param_info)

    opts = []
    for option in param_info.choices:
        opts.append(
            formatted_xml_elem("option", {"value": option}, text=option.capitalize()))

    return param(param_info, body=opts)


def repeat(param_info: ParamInfo) -> etree._Element:
    attributes = {
        "name": param_info.name + "_repeat",
        "title": param_info.name + "_repeat",
        "min": param_info.custom_attributes.get("min", None),
        "max": param_info.custom_attributes.get("max", None),
        "default": param_info.custom_attributes.get("default", None),
    }

    names = list(attributes.keys())
    for name in names:
        if attributes[name] is None:
            attributes.pop(name)

    if param_info.param_type.is_selection:
        inner = options(param_info)
    else:
        inner = param(param_info)

    return formatted_xml_elem("repeat", attributes, body=[inner])


def param(param_info: ParamInfo, body: Optional[List[etree._Element]] = None):
    attributes = {
        "argument": param_info.argument,
        "type": param_info.type,
        "format": param_info.format,
    }

    if param_info.param_type.is_flag:
        attributes["truevalue"] = param_info.argument
        attributes["falsevalue"] = ""
        attributes["checked"] = "false"

    attributes["optional"] = str(param_info.optional).lower()
    attributes["label"] = param_info.label

    if param_info.help is not None:
        attributes["help"] = param_info.help
    # this might seem weird, but it is done like this for correct order
    # of attributes
    if param_info.format is None:
        attributes.pop("format")

    return formatted_xml_elem("param", attributes, body=body)


def formatted_xml_elem(name, attributes, text: Optional[str] = None,
                       body: Optional[List[etree._Element]] = None) -> etree._Element:
    element = etree.Element(name, attributes)
    element.text = text
    if body is not None:
        element.extend(body)

    return element
