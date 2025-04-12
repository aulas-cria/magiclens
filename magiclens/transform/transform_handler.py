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
        
        if width is None:
            width = original_width
        if height is None:
            height = original_height
        
        image.resize((width, height))
        
        image_byte_arr = BytesIO()
        image.save(image_byte_arr, format="JPEG")
        image_byte_arr.seek(0)

        return image_byte_arr.getvalue()