from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'chart.html')

from django.http import HttpResponse
from django.views.generic import View
import datetime

from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Luis V',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('invoice.html')
#         context = {
#             "invoice_id": 123,
#             "customer_name": "John Cena",
#             "amount": 1399.99,
#             "today": "Today",
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('invoice.html', context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")