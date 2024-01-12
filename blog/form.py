from django.forms import ModelForm
from . models import *

class newpost(ModelForm):
    class Meta:
        model=post
        fields=('title','content','image','category')

class profilepage(ModelForm):
    class Meta:
        model=UserProfile
        fields=('bio','picture','facebook','twitter','instagram')


class commet(ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','text')