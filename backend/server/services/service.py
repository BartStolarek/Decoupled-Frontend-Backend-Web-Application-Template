from loguru import logger

from server.integrations.stripe import StripeIntegration


def get_services() -> tuple[bool, str, list]:
    try:
        stripe = StripeIntegration()
        success, message, services = stripe.fetch_products() 
        for service in services:
            service['display_price'] = stripe.fetch_price(service['default_price'])
        
        # Removing recurring payment type products (those are services)
        filtered_services = []
        for service in services:
            if service['display_price']['type'] == 'recurring' and service['active'] is True:
                filtered_services.append(service)
        return success, message, filtered_services
    except Exception as e:
        logger.error(f"Unexpected Error trying to find services: {e}")
        return False, 'Unexpected error occurred', []
