# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests, json
# Create your views here.

def index(request) :
    user_home = "WELCOME PAGE"
    return render (request, 'home/index.html',{"title":user_home,"error":""})


def verify(request):
    mess = ""
    if request.method == "POST" :

        private_key = 'test_pr_fde6b4ac51ea4a868606097e63791344' # put here your private key
        # Retrieve data returned in payment gateway callback
        token = request.POST["sp_token"]
        amount = request.POST["sp_amount"]
        amount_currency = request.POST["sp_currency"]
        sp_status = request.POST["sp_status"]
        transaction_id = request.POST["transaction_id"] # we don't really need this here, is just an example
        data = {'token': token, 'amount': amount, 'amount_currency': amount_currency}
        data_string = json.dumps(data)

        url = "https://checkout.simplepay.ng/v2/payments/card/charge/"
        # create request object, set url and post data
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data_string, auth=(private_key, ''), headers=headers, verify=False)

        print(r.json())
        return HttpResponse(r.json(),content_type='application/json')
