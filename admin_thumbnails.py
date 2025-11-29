def thumbnail(field_name):
    """Minimal stub decorator to mimic `admin_thumbnails.thumbnail`.

    This avoids requiring the external `django-admin-thumbnails` package
    and prevents import-time access to Django settings. It simply returns
    the class unchanged. If you want full thumbnail rendering in the
    admin list view later, install a compatible package or extend this stub.
    """
    def decorator(cls):
        return cls

    return decorator
