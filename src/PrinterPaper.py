class PrinterPaper:
    '''
    A class that represents a piece of paper that would have an image printed on it.

    Attributes:
        width (float): Width of paper in inches.
        height (float): Height of paper in inches.
        dpi (tuple): DPI of printer in form (width, height).
    '''

    def __init__(self,width: float, height: float, dpi: tuple):
        """
        PrinterPaper constructor.

        Arguments:
            width (float): Width of paper in inches.
            height (float): Height of paper in inches.
            dpi (tuple): DPI of printer in form (x,y).
        """

        self.width = width
        self.height = height
        self.dpi = dpi

    @property
    def pixel_width(self) -> float:
        '''Return width of paper in pixels.'''
        return self.width * self.dpi[0]

    @property
    def pixel_height(self) -> float:
        '''Return height of paper in pixels.'''
        return self.height * self.dpi[1]

    @property
    def width(self) -> float:
        '''Return width of paper in inches.'''
        return self.__width

    @width.setter
    def width(self,value:float):
        '''Set width of paper in inches.
        
        Arguments:
            value (float): New width in inches.
        '''
        try:
            value = float(value)
        except:
            raise TypeError(f"width should be type float, not type {value.__class__.__name__}.")
        else:
            if value > 0:
                self.__width = value
            else:
                raise ValueError(f"width should be greater than zero, not {value}")

    @property
    def height(self) -> float:
        '''Return height of paper in inches.'''
        return self.__height

    @height.setter
    def height(self,value:float):
        '''Set height of paper in inches.

        Arguments:
            value (float): New height in inches.
        '''
        try:
            value = float(value)
        except:
            raise TypeError(f"height should be type float, not type {value.__class__.__name__}.")
        else:
            if value > 0:
                self.__height = value
            else:
                raise ValueError(f"height should be greater than zero, not {value}")

    @property
    def dpi(self) -> tuple:
        '''Return DPI of printer.'''
        return self.__dpi

    @dpi.setter
    def dpi(self,value:tuple):
        if isinstance(value,tuple):
            if len(value) == 2:
                if (isinstance(value[0],int) or isinstance(value[0],float)) and (isinstance(value[1],int) or isinstance(value[1],float)):
                    self.__dpi = value
                else:
                    raise TypeError(f"dpi should be a tuple of types (float,float), not tuple of types ({value[0].__class__.__name__},{value[1].__class__.__name__}).")
            else:
                raise ValueError(f"Length of dpi should be 2, not {len(value)}")
        else:
            raise TypeError(f"dpi should be type tuple, not type {value.__class__.__name__}.")