from .serializers import FibonacciSerializer
from rest_framework.response import Response
from rest_framework import views
from django.views.generic import TemplateView
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from .models import BinRecord
from .number_generator import generate_number,make_bin_in_db


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class Fibonacci(views.APIView):
    def get(self,request,number):
        result =0
        # first two terms
        first_number=1
        second_number=1
        count=1
        if number in cache:
            data = cache.get(number)
            return Response(data)
        else:
            try:
                #calculating a bin number. bin number is a lot with difference of 100. Example (100,200,300 and so on..)
                b_num = number//100
                b_num = (b_num + 1) * 100
                data = BinRecord.objects.get(pk=b_num)
                result,v=generate_number(data,number)
            except BinRecord.DoesNotExist:
                data = None

            if data is None:
                bin_number_dictionary={}
                #getting the list of all bin numbers from database
                response =BinRecord.objects.values_list('bin_number', flat=True).order_by('bin_number')

                if response:
                    #finding the closest bin number for the created bin number by the received number as input
                    for x in response:
                        difference = abs(x-number)
                        bin_number_dictionary.update({difference:x})
                    bin_number_sorted_list = sorted(bin_number_dictionary.keys())
                    data = BinRecord.objects.get(pk=bin_number_dictionary[bin_number_sorted_list[0]])

                    if(b_num>bin_number_dictionary[bin_number_sorted_list[0]]):
                        result,bin_data= generate_number(data, number)
                        bin_data.update({'bin_number':b_num})
                        bin_data.update({'number': number})
                        make_bin_in_db(bin_data)
                    else:
                        result, bin_data = generate_number(data, number)
                else:
                    if number == 1 or number==2:
                        result = first_number
                    else:
                        while count < number:
                            nth = first_number+second_number
                            first_number = second_number
                            second_number = nth
                            count+=1
                            if count==number-1:
                                result = nth

                                #Creating the bin_number entery in the database
                                q = BinRecord(bin_number=b_num, saved_number=number, last_number=str(nth), second_last_number=str(first_number))
                                q.save()
                                break
        result = str(result)
        print(result)
        data ={'nth_number':result}
        data = FibonacciSerializer(data).data
        cache.set(number, data, timeout=60*60)
        print("Reached to end")
        return Response(data)

class HomeView(TemplateView):
    template_name = 'fibonacci/index.html'



