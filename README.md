# django-mobile-mixin

This project is inspired on these posts about Django working with mobile:

[Django Mobile Browser Detection Middleware](http://sullerton.com/2011/03/django-mobile-browser-detection-middleware)

[Mobile Template Mixin for Django Class Based Views](http://oluwaseunladeinde.wordpress.com/2013/02/22/mobile-template-mixin-for-django-class-based-views/)

## USAGE

### SETTINGS

In your settings.py add:

    MOBILE_TEMPLATE_DIRS = (PROJECT_DIR.child('templates', 'mobile'),)
    DESKTOP_TEMPLATE_DIRS = (PROJECT_DIR.child('templates', 'desktop'),)

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        #add middleware to support mobile detection
        'myapp.middleware.RequestDetectionMiddleware',
    )

### MIXIN

In your view.py add:

    from .mobile_mixin import MobileTemplateMixin
    class YourView(MobileTemplateMixin):
        template_name = "app/template.html"
