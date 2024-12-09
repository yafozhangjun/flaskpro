from django.shortcuts import render, redirect
from rest_framework import settings
import os
from django.http import HttpResponse, Http404
from .forms import DocumentForm
from .models import Document
from openpyxl import Workbook


def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploaded_successfully')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})


def download_document(request, document_id):
    try:
        document = Document.objects.get(id=document_id)
        file_path = os.path.join(settings.MEDIA_ROOT, document.upload.name)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(file_path))
            return response
    except Exception as e:
        raise Http404('File not found')


# 下载模板
def download_template(column_array, filename):
    # Create a new workbook
    wb = Workbook()

    # Get the active worksheet
    ws = wb.active

    # Add headers to the worksheet
    ws.append(column_array)

    # Auto-fit the width of the columns
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Get the column name
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    # Set the filename for the download
    # filename = 'template.xlsx'

    # Create the HTTP response with the file attachment
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    # Save the workbook to the response content
    wb.save(response)
    return response

