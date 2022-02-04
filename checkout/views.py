from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """Check out """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KPSR5EToswm7mcx1oRZgsKg6qeTdHhT2SDvEtQPMIek9dnaZGS0QPvHDtW3Fv6h8CbpYTpvXDHQxIzcMzgFjQ1u00ZinqFlML',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)