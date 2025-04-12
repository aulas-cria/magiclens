from io import BytesIO
from PIL import Image

class TransformHandler:
    def change_size(
            self,
            filename: str,
            width: int | None = None,
            height: int | None = None
    ):
        image = Image.open(filename)
        original_width, original_height = image.size
        
        if width is None and height is None:
            width = original_width
            height = original_height
        elif width is None:
            width = int((height / original_height) * original_width)
        elif height is None:
            height = int((width / original_width) * original_height)
        
        image_resized = image.resize((width, height))

        image_byte_arr = BytesIO()
        image_resized.save(image_byte_arr, format="JPEG")
        image_byte_arr.seek(0)

        return image_byte_arr.getvalue()