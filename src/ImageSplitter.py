from PIL import Image
from math import ceil, floor

def split_image(image:Image.Image,cols:int,rows:int) -> list:
    '''
    Split an image into (cols * rows) images, with "cols" columns and "rows" rows.

    Arguments:
        image (PIL.Image.Image): Image to split.
        cols (int): Number of columns to split image into.
        rows (int): Number of rows to split image into.
    
    Returns:
        images (list): List of length (cols*rows) containing the image "splits."
    '''

    if isinstance(image,Image.Image):
        pass
    else:
        raise TypeError(f"image should be type PIL.Image.Image, not type {image.__class__.__name__}.")

    try:
        cols = int(cols)
    except:
        raise TypeError(f"cols should be type int, not type {cols.__class__.__name__}.")

    try:
        rows = int(rows)
    except:
        raise TypeError(f"rows should be type int, not type {rows.__class__.__name__}.")

    w,h = image.size

    if cols > w or cols < 1:
        raise ValueError(f"Invalid column value {cols}. Value must be 1 <= n < {w} (Image Width).")
    elif rows > h or rows < 1:
        raise ValueError(f"Invalid row value {rows}. Value must be 1 <= n < {h} (Image Height).")
    else:
        
        images = []

        dx = ceil(w / cols)
        dy = ceil(h / rows)
        for y in range(0,h,dy):
            for x in range(0,w,dx):
                base = Image.new('RGBA', (dx, dy), (0,0,0,0))
                crop = image.crop((x,y,min(x+dx-1,w),min(y+dy-1,h))) # If the border isn't perfect, paste it onto
                base.paste(crop,(0,0))                               # a blank image so we retain the same size

                images.append(base)
        
        return images
