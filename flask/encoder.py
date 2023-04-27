#2. encoder

from PIL import Image
import io

# Open the cover image and convert it to grayscale
def encode(cover_image, data):
    cover_image = Image.open(cover_image).convert('L')
    width, height = cover_image.size

    # create a multiline string
    plaintext_string = data

    # convert the string to a binary stream using the io.BytesIO class
    plaintext_stream = io.BytesIO(plaintext_string.encode('utf-8'))

    # read the binary stream into a bytes object
    data = plaintext_stream.read()

    # print the bytes object
    print(data)

    # Append the length of the data to the beginning of the data
    data_len = len(data)
    data = bytes([data_len]) + data

    # Check if the data can fit in the cover image
    if len(data) * 8 > width * height:
        print("Error: Data is too large to fit in the cover image!")
        exit()

    # Convert the data to a binary string
    data_bin = ''.join('{:08b}'.format(b) for b in data)

    # Get the pixel data of the cover image
    pixels = cover_image.load()

    # Embed the data in the LSB of the pixel values
    index = 0
    for y in range(height):
        for x in range(width):
            # Get the pixel value and convert it to binary
            pixel_bin = '{:08b}'.format(pixels[x, y])

            # Embed one bit of data in the LSB of the pixel value
            if index < len(data_bin):
                pixel_bin = pixel_bin[:-1] + data_bin[index]
                index += 1

            # Convert the modified pixel value back to an integer
            pixel = int(pixel_bin, 2)

            # Update the pixel value in the image
            pixels[x, y] = pixel

    # Save the stego image
    cover_image.save('static/stego.png')
    print("Stego image created successfully!")
    return 'static/stego.png'

