from PIL import Image
from io import BytesIO
from math import ceil, floor

class ImageSplitter:

    def __init__(self,data,dpi=72.0,paper_w=8.5,paper_h=11):
        self.image = Image.open(BytesIO(data))
        self.cells = []
        self.dpi = (dpi,dpi)
        self.pwpx = self.dpi[0]*paper_w # Paper Width in Pixels
        self.phpx = self.dpi[1]*paper_h
    
    @property
    def width(self):
        return self.image.size[0]

    @property
    def height(self):
        return self.image.size[1]

    def split(self,cols,rows,scale=True):
        if cols > self.width or cols < 1:
            raise ValueError(f"Invalid column value {cols}. Value must be 1 <= n < {self.width} (Image Width).")
        elif rows > self.height or rows < 1:
            raise ValueError(f"Invalid row value {rows}. Value must be 1 <= n < {self.height} (Image Height).")
        else:
            dx = ceil(self.width / cols)
            dy = ceil(self.height / rows)
            for y in range(0,self.height,dy):
                for x in range(0,self.width,dx):
                    base = Image.new('RGB', (dx, dy), (255, 255, 255))
                    crop = self.image.crop((x,y,max(x+dx-1,self.width),max(y+dy-1,self.height))) # If the border isn't perfect, paste it onto a
                    base.paste(crop)                                                             # blank image so we retain the same size
                    if scale:
                        if dx >= dy:
                            ratio = self.pwpx / dx
                        else:
                            ratio = self.phpx / dy
                        base = base.resize( (floor(dx*ratio),floor(dy*ratio)) )

                    self.cells.append(base)

    def export(self):
        contents = None
        with BytesIO() as output:
            self.cells[0].save(output,"PDF",resolution=100.0, dpi=self.dpi, save_all=True, append_images=self.cells[1:])
            contents = output.getvalue()
        return contents
