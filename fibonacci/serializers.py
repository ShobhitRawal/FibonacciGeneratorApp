from rest_framework import serializers

class FibonacciSerializer(serializers.Serializer):
   nth_number = serializers.CharField()
