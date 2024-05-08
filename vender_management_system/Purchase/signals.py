import datetime
from django.db.models.signals import post_save
from django.db.models import Avg, F
from django.dispatch import receiver
from Purchase.models import Purchase, HistoryPerfoemence, PurchaseStatusLog




@receiver(post_save, sender = PurchaseStatusLog)
def save_performence(sender, instance, created, **kwargs):
    if created:
        order_instance = instance.prchase_id
        vender = order_instance.vendor
        historical_performancce_instance = HistoryPerfoemence()
        historical_performancce_instance.vendor = vender
        historical_performancce_instance.date = datetime.datetime.now()

        # Calculation of fulfilment rate
        if instance.status != 'Aknowledged':
            all_purchases = Purchase.objects.all()
            completed_purchases = all_purchases.filter(status = 'Completed')

            fulfilment_rate = completed_purchases.count() / all_purchases.count()
            historical_performancce_instance.fulfillment_rate = fulfilment_rate 
            vender.fulfillment_rate = fulfilment_rate

        if instance.status == 'Aknowledged':
            avg_response_time = instance.acknowledgment_date.date() - order_instance.issue_date.date()
            historical_performancce_instance.average_response_time = avg_response_time.days()

            historical_performancce_instance.save()

            # Update the venders average response time
            all_order_avevrage = PurchaseStatusLog.objects.filter(prchase_id__vendor = vender).aaggregate(Avg('average_response_time'))

            vender.average_response_time = all_order_avevrage['average_response_time__avg']

        elif instance.status == 'Completed':
            order_instance.completed_date = datetime.datetime.now()
            order_instance.save()

            all_orders = vender.vender_purchase.filter(status = 'Completed')

            order_delivereed_on_time = all_orders.filter(completed_date__lte = F('delivery_date'))

            on_time_delivery_rate = order_delivereed_on_time.count() / all_orders.count()
            vender.on_time_delivery_rate = on_time_delivery_rate

            historical_performancce_instance.on_time_delivery_rate = on_time_delivery_rate
            historical_performancce_instance.save()

        







            

        
