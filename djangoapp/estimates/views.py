from datetime import datetime

from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
import requests

from djangoapp.estimates.forms import EstimateForm


class HomeView(FormView):
    template_name = 'estimates/home.html'
    form_class = EstimateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        results = form.cleaned_data
        request_string =  f"https://api.forecast.solar/estimate/{results['latitude']}/{results['longitude']}/{results['declination']}/{results['azimuth']}/{results['kwp']}"
        solar_response = requests.get(request_string)

        if solar_response.status_code == 200:
            solar_data = solar_response.json()

            context = self.get_context_data()
            context['solar_data'] = True
            context['place'] = solar_data['message']['info']['place']
            estimate_timestamp = datetime.fromisoformat(solar_data['message']['info']['time_utc'])
            context['utc_estimate_timestamp'] = estimate_timestamp.strftime('%I:%M%p %d %B %Y')

            watt_days = solar_data['result']['watt_hours_day']
            watt_days_amended = {}
            for timestamp in watt_days.keys():
                date = datetime.strptime(timestamp, '%Y-%m-%d')
                new_key = date.strftime('%d %B %Y')
                watt_days_amended[new_key] = watt_days[timestamp]
            context['watt_days'] = watt_days_amended

            watt_hours = solar_data['result']['watt_hours']
            watt_hours_amended = {}
            for timestamp in watt_hours.keys():
                date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                new_key = date.strftime('%I:%M%p %d %B %Y')
                watt_hours_amended[new_key] = watt_hours[timestamp]
            context['watt_hours'] = watt_hours_amended
            
            return self.render_to_response(context)
        else:
            return self.form_invalid(form)