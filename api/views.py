from django.shortcuts import redirect


def redirect_api(request):
    api_url = request.build_absolute_uri()
    return redirect(api_url + 'posts/')
