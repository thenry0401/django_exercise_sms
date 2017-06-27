from django.shortcuts import render
import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

# Create your views here.

def sms_send(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        api_key = "NCSGLMHSQ2FTVZUA"
        api_secret = "2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F"

        params = dict()
        params['type'] = 'sms'
        params['to'] = phone_number
        params['from'] = '01029953874'
        params['text'] = message

        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

        sys.exit()
        return redirect('sms_send')
    else:
        context = {}
    return render(request, 'sms.html', context)