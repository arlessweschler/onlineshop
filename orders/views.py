from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .filter import OrderFilter
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Rating


@login_required()
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order(buyer=request.user, **form.cleaned_data)
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                product = item['product']
                quantity = item['quantity']
                product.stock -= quantity
                product.save()
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm(initial={'phone': request.user.profile.phone,
                                        'city': request.user.profile.city,
                                        'postal_code': request.user.profile.postal_code,
                                        'street': request.user.profile.street,
                                        'house': request.user.profile.house,
                                        'building': request.user.profile.building,
                                        'apartment': request.user.profile.apartment,
                                        'email': request.user.email
                                        })
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


# все заказы с сайта для персонала
# еще один способ для разграничения доступа  @user_passes_test(lambda u: u.is_staff)
@staff_member_required
def  all_orders(request):
    orders = Order.objects.all()
    filter = OrderFilter(request.GET, queryset=orders)
    paginator = Paginator(filter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'orders': page_obj.object_list, 'page_obj': page_obj, 'paginator': paginator, 'filter': filter}
    return render(request, 'orders/all_orders.html', context)


# заказы покупателя
@login_required()
def  my_orders(request):
    orders = Order.objects.filter(buyer=request.user)
    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'orders': page_obj.object_list, 'page_obj': page_obj, 'paginator': paginator}
    return render(request, 'orders/my_orders.html', context)


@login_required()
def detail_order(request, id):
    order = get_object_or_404(Order, id=id)
    items = OrderItem.objects.filter(order_id=order)
    rating = Rating.objects.filter(user=request.user)
    rating = [x.product for x in rating]
    if request.method == 'POST':
        if request.POST.get('status'):
            order.status = request.POST['status']
            if request.POST['status'] == 'Отменен':
                for item in items:
                    product = item.product
                    product.stock += item.quantity
                    product.save()
        if request.POST.get('paid'):
            order.paid = request.POST['paid']
        order.save()
    context = {'order': order, 'items': items, 'rating': rating}
    return render(request, 'orders/order/detail_order.html', context)


@receiver(post_save, sender=Order)
def mail_make_order(sender, **kwargs):
    subject = 'Оформление заказа в магазине'
    html_message = render_to_string('orders/order/message_order.html', {'order': kwargs.get('instance')})
    plain_message = strip_tags(html_message)
    from_email = 'micromagic.by@yandex.by'
    instance = kwargs.get('instance')
    to_mail = instance.buyer.email
    # send_mail(subject, plain_message, from_email, [to_mail], html_message=html_message)





