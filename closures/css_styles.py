import copy

def css_styles(initial_styles):
    styles_cpy = copy.deepcopy(initial_styles)

    def add_style(selector, property_, value):
        # selector is a dict
        if selector not in styles_cpy:
            styles_cpy[selector] = {}
        # update the selector if already present
        styles_cpy[selector][property_] = value
        
        return styles_cpy

    return add_style