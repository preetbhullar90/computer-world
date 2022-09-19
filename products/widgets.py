from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInputImage(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = ('products/custom_widget_templates/'
                     'custom_clearable_file_input_img.html')


class CustomClearableFileInputImage1(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = ('products/custom_widget_templates/'
                     'custom_clearable_file_input_img1.html')


class CustomClearableFileInputImage2(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = ('products/custom_widget_templates/'
                     'custom_clearable_file_input_img2.html')
