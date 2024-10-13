from django import forms

from djangoapp.estimates.utils import convert_floats_to_ints_if_whole


class EstimateForm(forms.Form):
    base_attrs = {'class': 'form-control', 'step': '1'}
    lat_and_lon_attrs = base_attrs.copy()
    lat_and_lon_attrs['step'] = '0.0001'
    latitude = forms.FloatField(min_value=-90, max_value=90, widget=forms.NumberInput(attrs=lat_and_lon_attrs))
    longitude = forms.FloatField(min_value=-180, max_value=180, widget=forms.NumberInput(attrs=lat_and_lon_attrs))
    declination = forms.IntegerField(min_value=0, max_value=90, widget=forms.NumberInput(attrs=base_attrs))
    azimuth = forms.IntegerField(min_value=-180, max_value=180, widget=forms.NumberInput(attrs=base_attrs))
    kwp_attrs = base_attrs.copy()
    kwp_attrs['step'] = '0.01'
    kwp = forms.FloatField(widget=forms.NumberInput(attrs=kwp_attrs))

    def clean(self):
        cleaned_data = super().clean()

        for field in cleaned_data:
            value = cleaned_data[field]
            value = convert_floats_to_ints_if_whole(value)
            cleaned_data[field] = value
        return cleaned_data