from django.shortcuts import render, redirect, get_object_or_404
from django.db.models  import Sum
from .forms import transactionForm, addPayForm
from .models import Transaction

# Create your views here.
def home(request):
    recent_transactions = Transaction.objects.order_by('-date')[:10]
    category_sums = Transaction.objects.values('category__name').annotate(total_price=Sum('price'))
    context = {'recent_transactions': recent_transactions, 'category_sums': category_sums}
    return render(request, 'home.html', context)

# Find a way to subtract amount from the specified Account in the drop down menu
def createTrans(request):
    form = transactionForm()
    if request.method == "POST":
        form = transactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'trans_form.html', context)

def deleteTrans(request, pk):
    transaction = Transaction.objects.get(id=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('home')
    return render(request, 'delete_trans.html', {'obj': transaction})

# Find a way to add the payment amount to a specified account rather than adding another bank
def add_pay(request):
    pay_form = addPayForm()
    if request.method == "POST":
        pay_form = addPayForm(request.POST)
        if pay_form.is_valid():
            pay_form.save()
            return redirect('home')
    context = {'pay_form': pay_form}
    return render(request, 'add_pay.html', context)
