# c:\Projects\evan-aidan-clothes\clothesshop\context_processors.py
from django.utils import timezone
from .models import Sale

def sale_timer_context(request):
    """
    Provides the end date of the current active sale to all templates.
    """
    now = timezone.now()
    context = {'sale_end_date_iso': None}

    # Find the first active sale that hasn't ended yet, ordered by the soonest end date.
    active_sale = Sale.objects.filter(
        is_active=True,
        start_date__lte=now,
        end_date__gt=now
    ).order_by('end_date').first()

    if active_sale:
        # The date must be in ISO format for JavaScript's new Date() to parse it correctly
        # across all timezones. Django's isoformat() on a timezone-aware datetime
        # object handles this perfectly.
        context['sale_end_date_iso'] = active_sale.end_date.isoformat()

    return context