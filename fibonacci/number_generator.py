from .models import BinRecord

def generate_number(data,number):
    bin_data={'new_last_number':0,'new_second_last_number':0}
    result=0
    bin_number = data.bin_number
    first_number = int(data.second_last_number)
    second_number = int(data.last_number)
    saved_number = data.saved_number
    count = saved_number
    if (number == saved_number):
        result = second_number
    elif (number > saved_number):
        while count < number:
            nth = first_number + second_number
            first_number = second_number
            second_number = nth
            count += 1
            if (count == number):
                result = nth
                bin_data['new_last_number']=nth
                bin_data['new_second_last_number']=first_number

    else:
        nth = 0
        while saved_number != number + 1:
            temp = second_number
            temp1 = first_number
            first_number = temp - first_number
            second_number = temp1
            nth = first_number

            saved_number = saved_number - 1
            print(nth)
        result = nth
    return result,bin_data

# This functio creates the bin_number entery in the database
def make_bin_in_db(data):
    q = BinRecord(bin_number=data['bin_number'], saved_number=data['number'], last_number=str(data['new_last_number']), second_last_number=str(data['new_second_last_number']))
    q.save()



