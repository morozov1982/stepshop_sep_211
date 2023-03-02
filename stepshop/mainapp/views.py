from django.shortcuts import render


def products(request):
    title = "продукты/каталог"

    context = {
        'title': title,
    }

    # return render(request=request, template_name='products.html', context=context)
    return render(request, 'products.html', context)
