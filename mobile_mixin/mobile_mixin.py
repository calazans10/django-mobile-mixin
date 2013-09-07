# -*- coding: utf-8 -*-


class MobileTemplateMixin(object):
    template_source = None
    template_name = None

    def get_template_names(self, *args, **kwargs):
        if self.request.is_mobile:
            self.template_source = "mobile/"
        else:
            self.template_source = "desktop/"

        self.template_name = self.template_source + self.template_name

        return self.template_name
