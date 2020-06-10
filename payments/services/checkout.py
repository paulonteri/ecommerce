from orders.models import Order
from payments.models import Payment


def checkout(order: Order, payment_method: str):
    try:
        payment = Payment(order=order,
                          payment_method=payment_method,
                          amount=order.get_total(),
                          paid=False,
                          waiting=True)
        payment.save()
    except Exception as e:
        raise Exception(e)


