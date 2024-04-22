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
