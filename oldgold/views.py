from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.template import RequestContext, loader

from oldgold.models import GoldPrice, Item, DetailImg

def index(request):
    item_list   = Item.objects.order_by('-pub_date')
    context     = {'item_list': item_list}
    return render(request, 'oldgold/index.html', context)

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'oldgold/detail.html', context)

# class IndexView(generic.ListView):
#     template_name = 'oldgold/index.html'
#     context_object_name = 'item_list'
# 
#     def get_queryset(self):
#         return Item.objects.order_by('-pub_date')
# 
# class DetailView(generic.DetailView):
#     model = Item
#     template_name = 'oldgold/detail.html'
