from django import forms
from models import Stop

class FromStop(forms.Form):
	from_stop = forms.ChoiceField(choices=list(Stop.objects.all().values_list('id','name',)))