from rest_framework import serializers
from .models import *

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = student
        # field = ('fname', 'lname', 'standard', 'address')
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = payment
        #fields = ('student_id', 'payment', 'Date',)
        fields='__all__'


