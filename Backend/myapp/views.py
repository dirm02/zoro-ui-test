# views.py

from web3 import Web3
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def connect_polygon(request):
    if request.method == 'GET':
        # Connect to the Polygon network using Infura or Alchemy
        infura_url = "https://polygon-mainnet.infura.io/v3/834cec7f01b84b05be1baea6d799fbd1"
        web3 = Web3(Web3.HTTPProvider(infura_url))
        if web3.is_connected:
            return JsonResponse({'status': "true", 'network': 'Polygon Mainnet'})
        else:
            return JsonResponse({'status': 'false', 'network': 'Polygon Mainnet'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
