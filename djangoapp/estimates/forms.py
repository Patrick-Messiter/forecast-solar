from django import forms

from djangoapp.estimates.utils import convert_floats_to_ints_if_whole


class EstimateForm(forms.Form):
    latitude = forms.FloatField(min_value=-90, max_value=90)
    longitude = forms.FloatField(min_value=-180, max_value=180)
    declination = forms.IntegerField(min_value=0, max_value=90)
    azimuth = forms.IntegerField(min_value=-180, max_value=180)
    kwp = forms.FloatField()

    def clean(self):
        cleaned_data = super().clean()

        for field in cleaned_data:
            value = cleaned_data[field]
            value = convert_floats_to_ints_if_whole(value)
            cleaned_data[field] = value
        return cleaned_data