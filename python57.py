picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_picture():    
    for row in picture:
        for pixel in row:
            if (pixel == 1):
                print('*', end='')
            else:
                print(' ', end='')
        print('')

show_picture()

print("This will display memory location of function :", show_picture)