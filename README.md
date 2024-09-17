# zoro-ui-test

**web3 frontend development and evaluation**


![image](https://github.com/user-attachments/assets/38a6a653-72e9-4bf3-926f-570941126c78)


1-Build new page with keeping the layouts on our application\
`code here`\
2-Create new button called ‘Connect polygon network\
`from web3 import Web3
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

    return JsonResponse({'error': 'Invalid request method'}, status=400)` \
3-Build simple Django backend that interacts with Polygon network\
`code here`\
4-Implement integration new button with Django backend\
`code here`\
** video   result **


Zoro Run:

    yarn
    yarn dev
