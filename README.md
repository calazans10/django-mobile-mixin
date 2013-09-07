# django-mobile-mixin

## USAGE

### SETTINGS

In your settings.py add:

    MOBILE_TEMPLATE_DIRS = (PROJECT_DIR.child('templates', 'mobile'),)
    DESKTOP_TEMPLATE_DIRS = (PROJECT_DIR.child('templates', 'desktop'),)

### MIXIN

In your view.py add:

    from .mobile_mixin import MobileTemplateMixin
    class YourView(MobileTemplateMixin):
        template_name = "app/template.html"
