def save_picture(picture):
    filename = picture.filename
    file_type = filename.split('.')[-1]

    if file_type not in ('jpeg', 'svg', 'bmp', 'jpg'):
        return

    picture.save(f'./uploads/images/{filename}')
    return f'uploads/images/{filename}'