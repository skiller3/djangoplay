from constraints.models import Constraint, Asset
from constraints.forms import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("Greetings! This is the default response!")

def asset_detail(request, symbol):
    asset = get_object_or_404(Asset, symbol=symbol)
    return render(request, "constraints/asset_detail.html", {"asset": asset, "form": AssetForm()})

def update_asset(request, symbol):
    print("Modifying asset: " + symbol)
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            newSymbol = form.cleaned_data["symbol"]
            newName = form.cleaned_data["name"]
            asset = Asset.objects.get(symbol=symbol)
            asset.symbol = newSymbol
            asset.name = newName
            asset.save()
            return HttpResponseRedirect("/constraints/" + newSymbol)

    asset = get_object_or_404(Asset, symbol=symbol)
    return render(request, "constraints/asset_detail.html", {"asset": asset, "form": AssetForm()})

