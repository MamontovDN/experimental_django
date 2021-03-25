from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'text', 'img']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control',},),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


# def thumbnail(image_path, width, height):
#     absolute_url = posixpath.join(settings.MEDIA_URL, image_path)
#     return ('<img src="%s" alt="%s" class="widget-img" />' %
#            (absolute_url, image_path))
#
#
# class ImageWidget(forms.ClearableFileInput):
#     template = '<div>%(image)s</div>' \
#                '<div>%(clear_template)s</div>' \
#                '<div>%(input)s</div>'
#
#     def __init__(self, attrs=None, template=None, width=200, height=200):
#         if template is not None:
#             self.template = template
#         self.width = width
#         self.height = height
#         super(ImageWidget, self).__init__(attrs)
#
#     def render(self, name, value, attrs=None):
#         substitutions = {
#             'initial_text': self.initial_text,
#             'input_text': self.input_text,
#             'clear_template': '',
#             'clear_checkbox_label': self.clear_checkbox_label,
#         }
#         if not self.is_required:
#             checkbox_name = self.clear_checkbox_name(name)
#             checkbox_id = self.clear_checkbox_id(checkbox_name)
#             substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
#             substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
#             substitutions['clear'] = forms.CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
#
#         input_html = super(forms.ClearableFileInput, self).render(name, value, attrs)
#         if value and hasattr(value, 'width') and hasattr(value, 'height'):
#             image_html = thumbnail(value.name, self.width, self.height)
#             output = self.template % {'input': input_html,
#                                       'image': image_html,
#                                       'clear_template': self.template_with_clear % substitutions}
#         else:
#             output = input_html
#         return mark_safe(output)