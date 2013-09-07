# django-mobile-mixin

## USAGE

### MIXIN

In your view.py add:

    from .mobile_mixin import MobileTemplateMixin
    class YourView(MobileTemplateMixin):
        template_name = "app/template.html"
