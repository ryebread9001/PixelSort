from PIL import Image

def sort_row(row):
    min = 255*3
    min_index = 0

    for i in range(len(row)):
        
        temp = row[i][0] + row[i][1] + row[i][2]
        if temp < min:
            min = temp
            min_index = i

    sorted_row = row[:min_index]
    sorted_row.sort(reverse=True)
    return sorted_row + row[min_index:]

img = Image.open("desert.jpg")
pixels = img.load()
width, height = img.size

for y in range(height):
    row = []
    for x in range(width):
        row.append(pixels[x,y])
    row = sort_row(row)
    
    for x in range(width):
        pixels[x,y] = row[x]

new_img = Image.new('RGB',(width, height))
sorted_pixels = []
for y in range(height):
    for x in range(width):
        sorted_pixels.append(pixels[x,y])
new_img.putdata(sorted_pixels)
new_img.show()
new_img.save("earthglitch.jpg")
