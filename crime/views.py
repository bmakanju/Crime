from django.shortcuts import render

#Custom 404 Errr
def page_not_found_view(request, exception):
    return render(request, 'Errors/404.htm', status=404)
 
 #Custom 500 Errors
def page_not_found(request, exception):
    return render(request, "Errors/500.htm", status=500)