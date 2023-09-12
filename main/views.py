from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Karambit Blue Gem',
        'type': 'Knife',
        'price' : 'Rp500.000.000,00',
        'amount' : '1',
        'description' : 'The rarest skin in CSGO, effect on using this skin is as follows:\n+25% aim\n +50 damage '
    }

    return render(request, "main.html", context)