import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Assistant

@csrf_exempt
def create_assistant(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Only POST allowed')
    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid JSON')

    name = data.get('name')
    instructions = data.get('instructions', '')
    if not name:
        return HttpResponseBadRequest('Name required')

    assistant = Assistant.objects.create(name=name, instructions=instructions)
    return JsonResponse({'id': assistant.id, 'name': assistant.name, 'instructions': assistant.instructions})
