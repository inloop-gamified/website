from django.views.generic import View
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404


from .models import Umfrage


class UmfrageView(View):
    def get(self, request, umfrage_key):
        umfrage = get_object_or_404(Umfrage, key=umfrage_key)
        steps = umfrage.umfragestep_set.order_by('number')
        return TemplateResponse(request, 'umfrage/umfrage.html', {
            'umfrage': umfrage,
            'steps': steps,
        })

    def post(self, request, umfrage_key):
        umfrage = get_object_or_404(Umfrage, key=umfrage_key)

        response = TemplateResponse(request, 'umfrage/umfrage.html', {
            'umfrage': umfrage,
        })

        if umfrage.is_completed:
            return response

        steps = umfrage.umfragestep_set.order_by('number')
        for step in steps:
            if not hasattr(step, 'umfragerating'):
                continue
            rating = request.POST.get(f'{step.number}')
            if not rating:
                # drop step
                continue
            step.umfragerating.value = rating
            step.umfragerating.is_completed = True
            step.umfragerating.save()
        umfrage.is_completed = True
        umfrage.save()

        return response
