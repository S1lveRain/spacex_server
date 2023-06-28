from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Block

def get_blocks(request):
    blocks = Block.objects.all()
    data = []
    for block in blocks:
        data.append({
            'head': block.head,
            'center': block.center,
            'bottom': block.bottom
        })
    return JsonResponse(data, safe=False)

def create_block(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        head = data.get('head', '')
        center = data.get('center', '')
        bottom = data.get('bottom', '')
        
        block = Block.objects.create(
            head=head,
            center=center,
            bottom=bottom
        )
        
        response_data = {
            'id': block.id,
            'head': block.head,
            'center': block.center,
            'bottom': block.bottom
        }
        
        return JsonResponse(response_data, status=201)
