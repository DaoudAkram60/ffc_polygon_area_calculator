class Rectangle :

    #when the class object is created.

    def __init__(self,width,height) :
        self.width = width
        self.height = height
        area = width*height
        self.area = area

    #set_width method.

    def set_width(self,width) :
        self.width = width
        self.area = width*self.height

    #set_height method.

    def set_height(self,height) :
        self.height = height
        self.area = self.width*height
  
    #get_area method.

    def get_area(self) :
        area = self.width * self.height
        self.area += area
        return(area)

    #get_perimeter method.

    def get_perimeter(self) :
        perimeter = (self.width * 2) + (self.height * 2)
        return(perimeter)
    
    #get_diagnol method.
    
    def get_diagonal(self) :
        diagnol = ((self.width ** 2 + self.height ** 2) ** .5)
        return(diagnol)
    
    #get_picture method.

    def get_picture(self) :
        string = ""
        if self.width > 50 or self.height > 50 :
            string = "Too big for picture."
            return(string)
        else :
            for i in range(self.height) :
                string += f"{'*' * self.width}\n"
            return(string)
    
    #get_amount_inside method.
    
    def get_amount_inside(self,shape) :
        times = self.area / shape.area
        return(int(times))


    #Rectangle string.

    def __str__ (self) :
        return(f"Rectangle(width={self.width}, height={self.height})")

class Square(Rectangle) :

    #when the class object is created.

    def __init__(self, side):
        self.width = side
        self.height = side
        area = side*side
        self.area = area
  
    #Square string.

    def __str__(self) :
        return(f"Square(side={self.width})")
    
    #editing the set_height & set_width.

    def set_width(self,width) :
        self.width = width
        self.height = width

    def set_height(self,height) :
        self.height = height
        self.width = height

    #set_side method.

    def set_side(self,side) :
      self.width = side
      self.height = side
