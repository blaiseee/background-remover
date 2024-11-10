from rembg import remove
from PIL import Image

input_path = '301615793_3390179301251989_5158727221668717762_n.jpg'
output_path = '301615793_3390179301251989_5158727221668717762_n.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
Image.open(output_path)