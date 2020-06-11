from orders.models import Order
from payments.models import Payment, Transaction, TransactionPhone
from payments.services.payments import mobile_payments


def payment_failed(payment: Payment):
    payment.paid = False
    payment.waiting = False
    payment.cancelled = False
    payment.failed = True
    payment.save()


def transaction_failed(transaction: Transaction, error_message=None):
    if error_message:
        if type(error_message) != str:
            try:
                error_message = str(error_message)
            except:
                print(error_message)
                error_message = None
    transaction.paid = False
    transaction.waiting = False
    transaction.failed = True
    transaction.error_message = error_message
    transaction.save()

    payment_failed(transaction.payment)


def save_transaction(transaction: Transaction, transaction_resp):

    if type(transaction_resp) == dict and transaction_resp['status']:

        if transaction_resp['description']:
            transaction.description = transaction_resp['description']

        if transaction_resp['transactionId']:
            transaction.transaction_id = transaction_resp['transactionId']

        if transaction_resp['providerChannel']:
            transaction.provider_channel = transaction_resp['providerChannel']

        if transaction_resp['status'] == 'InvalidRequest':
            transaction.save()
            transaction_failed(transaction=transaction,
                               error_message='InvalidRequest: The request could not be accepted as one of the fields '
                                             'was invalid. The description field will contain more information.')
            raise Exception('Transaction Failed: InvalidRequest')
        #
        elif transaction_resp['status'] == 'NotSupported':
            transaction.save()
            transaction_failed(transaction=transaction,
                               error_message='NotSupported: Checkout to the provided phone number is not supported.')
            raise Exception('Transaction Failed: NotSupported')
        #
        elif transaction_resp['status'] == 'Failed':
            transaction.save()
            transaction_failed(transaction=transaction, error_message='Failed')
            raise Exception('Transaction Failed: Failed')
        #
        elif transaction_resp['status'] == 'PendingConfirmation':
            transaction.save()
            pass
        else:
            transaction.save()
            transaction_failed(transaction=transaction)
    else:
        transaction_failed(transaction=transaction, error_message='No response')
        raise Exception('Transaction Failed')


def make_payment(payment: Payment):
    transaction = Transaction(payment=payment, waiting=True)
    transaction.save()
    response = None

    try:
        if payment.payment_method == 'M':

            # save transaction phone number
            transaction_phone = TransactionPhone(transaction=transaction,
                                                 phone_number=payment.order.billing_address.phone_number)
            transaction_phone.save()

            response = mobile_payments(
                phone_number=transaction_phone.phone_number,
                amount=payment.amount,
                transaction_id=str(transaction.id))

        elif payment.payment_method == 'C':
            # TODO
            pass
        else:
            raise Exception('Incorrect payment method')
    except Exception as e:
        transaction_failed(transaction, e)
        raise Exception(e)
    else:
        return save_transaction(transaction=transaction, transaction_resp=response)


def checkout(order: Order, payment_method: str):
    # Checkout order/create Payment
    payment = Payment(order=order,
                      payment_method=payment_method,
                      amount=order.get_total(),
                      paid=False,
                      waiting=True,
                      cancelled=False,
                      failed=False)

    try:
        payment.save()
    except Exception as e:
        payment_failed(payment)
        raise Exception(e)
    else:
        return make_payment(payment)
