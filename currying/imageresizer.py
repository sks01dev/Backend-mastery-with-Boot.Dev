def new_resizer(max_width, max_height):
    
    def set_min_size(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resize_image(width, height):
            # resize 
            if width > max_width:
                new_width = max_width
            elif width < min_width:
                new_width = min_width
            else:
                new_width = width
            
            if height > max_height:
                new_height = max_height
            elif height < min_height:
                new_height = min_height
            else:
                new_height = height

            return new_width, new_height
        
        return resize_image
    
    return set_min_size

