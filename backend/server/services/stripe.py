from loguru import logger

from server.integrations.stripe import StripeIntegration


def get_products() -> tuple[bool, str, list]:
    try:
        stripe = StripeIntegration()
        success, message, products = stripe.fetch_products() 
        for product in products:
            product['display_price'] = stripe.fetch_price(product['default_price'])
        
        # Removing recurring payment type products (those are services)
        filtered_products = []
        for product in products:
            if product['display_price']['type'] == 'one_time' and product['active'] is True:
                filtered_products.append(product)
        return success, message, filtered_products
    except Exception as e:
        logger.error(f"Unexpected Error trying to find products: {e}")
        return False, 'Unexpected error occurred', []


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
    

def get_session_by_id(session_id) -> tuple[bool, str, dict]:
    try:
        stripe = StripeIntegration()
        session = stripe.fetch_session_by_id(session_id)
        if session:
            return True, "Successfully fetched session", session
        else:
            return False, "Session not found", {}
    except Exception as e:
        logger.error(f"Unexpected Error trying to get a checkout session: {e}")
        return False, 'Unexpected error occurred', {}
