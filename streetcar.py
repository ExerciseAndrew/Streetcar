class Square():
    def __init__(self):
        self.spot = ['.']*256
        def make_road(self, x, y):
        def set_row(y, value):
            for x in range(16):
                self.set(x,y,value)
        def set_column(x, value):
            for y in range(16):
                self.set( x,y,value)
        
class Board():
    def __init__(self):
        self.spot = ['.']*256
        def set_row(y, value):
            for x in range(16):
                self.set(x,y,value)
        def set_column(x, value):
            for y in range(16):
                self.set( x,y,value)

        for x in [0, 1]:
            set_column(x, '|')
        for y in [4, 6]:
            set_row(y, '_')

   def get(self, x, y):
        return self.spot[x + y * 16]

    def set(self, x, y, value):
        self.spot[x + y * 16] = value

    def show(self):
        print("  ")
        for y in range(16):
            s = ""
            for x in range(16):
                s = s + " " + self.get(x, y)
            print(s)
    def is_intersection()

    def move(self, old_x, old_y, new_x, new_y):
        if not self.is_valid_move(old_x, old_y, new_x, new_y):
            print("Not Valid Move")
            return
        value = self.get(old_x, old_y)
        self.set(new_x, new_y, value)
        self.set(old_x, old_y, '.') 


    def is_valid_move(self, old_x, old_y, new_x, new_y):
        if False == self.is_within_bounds(old_x, old_y):
            print("Old not in bounds")
            return False
        if False == self.is_within_bounds(new_x, new_y):
            print("New no boundy")
            return False   
             
        
        if self.get(new_x, new_y) !=  '.':
            print (".")
            return False

        value = self.get(old_x, old_y)
        if value == '.':
            print ("its a dot.")
            return False

        if abs(old_x - new_x) != 1:
            print("too much or too little")
            return False
        print ("This time. . . This time.")
        return True

    def is_within_bounds(self, x, y):
        return (0 <= x and x < 16 and 0 <= y and y < 16)
            
        
        
 
    
b = Board()
b.show()       

### put in capture mechanics    
## b.move(5, 5, 6, 4)

b.show()
    
