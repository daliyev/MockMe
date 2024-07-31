def validate_image_extension(file):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.svg', '.psd')
    if not ext.lower() in valid_extensions:
        raise ValidationError('Iltimos foto fayl tanlang.')