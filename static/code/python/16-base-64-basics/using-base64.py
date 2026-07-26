"""
The base64 module is Python's standard library for encoding binary data into ASCII text and decoding it back.

Base64 is not encryption. It is just an encoding format. Anyone can decode it.

we want to encode a binary data like a image as text string, we use this.

"""

import base64
from pathlib import Path


def main() -> None:

    myText = "hello world"  # normal string (python object)

    mytext_encoded = myText.encode()  #  convert to bytes object, utf-8 default

    mytext_b64Encoded = base64.b64encode(  # Encode the byte string with base64, This is plain text so we can transmit over text only protocols
        mytext_encoded
    )

    my_text_encoded = base64.b64decode(  # decode the base64 string to bytes object
        mytext_b64Encoded
    )

    my_text = my_text_encoded.decode()  #  convert back to string object

    print(my_text)

    # encoding images

    img_path = Path("~/Projects/soymadip.github.io/.cache/base64.png").expanduser()

    try:
        with open(img_path, "rb") as file:
            data = file.read()
    except Exception as e:
        print(f"Error: {e}")
        import sys

        sys.exit(1)

    if not data:
        return

    image = base64.b64encode(data)

    print(image)  # encoded base64 chars


if __name__ == "__main__":
    main()
