import struct

def what(file, h=None):
    if h is None:
        if isinstance(file, (str, bytes)):
            with open(file, 'rb') as f:
                h = f.read(32)
        else:
            h = file.read(32)

    # JPEG
    if h[0:3] == b'\xff\xd8\xff':
        return 'jpeg'
    # PNG
    if h[0:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    # GIF
    if h[:6] in (b'GIF87a', b'GIF89a'):
        return 'gif'
    # BMP
    if h[:2] == b'BM':
        return 'bmp'
    return None
