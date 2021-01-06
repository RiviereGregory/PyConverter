import os

from PIL import Image


class CustomImage:
    def __init__(self, path, folder="reduced"):
        self.image = Image.open(path)
        self.width, self.height = self.image.size
        self.path = path
        self.reduced_path = os.path.join(os.path.dirname(self.path),
                                         folder,
                                         os.path.basename(self.path))


if __name__ == "__main__":
    i = CustomImage("D:\_PythonProjets\SourceQtForPython\_sample_images\dog.jpg")
