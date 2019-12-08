from PIL import Image


class ImageDecoder:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data

    @property
    def layer_length(self):
        return self.width * self.height

    def split_layers(self):
        return [self.data[i:i+self.layer_length] for i in range(0, len(self.data), self.layer_length)]

    def get_signature(self):
        layers = self.split_layers()
        min_0_count, layer = min([(layer.count("0"), layer) for layer in layers])
        return layer.count("1") * layer.count("2")

    def get_pixels(self):
        return [
            "".join([self.data[i+j] for i in range(0, len(self.data), self.layer_length)])
            for j in range(self.layer_length)
        ]

    def decode_pixels(self):
        pixels = self.get_pixels()
        decoded_pixels = [pixel.replace("2", "")[0] for pixel in pixels]

        return [self.BLACK if pixel == "0" else self.WHITE for pixel in decoded_pixels]

    def get_image(self, image_path):
        pixels = self.decode_pixels()
        image = Image.new("RGB", (self.width, self.height))
        image.putdata(pixels)
        image.save(image_path)


if __name__ == "__main__":
    WIDTH = 25
    HEIGHT = 6

    with open("input.txt") as f:
        data = f.read().strip()

    decoder = ImageDecoder(WIDTH, HEIGHT, data)

    #  Part 1
    check = decoder.get_signature()
    assert check == 1330

    #  Part 2
    decoder.get_image("message.png")
