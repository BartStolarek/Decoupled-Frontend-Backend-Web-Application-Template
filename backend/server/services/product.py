from loguru import logger

from server.integrations.stripe import StripeIntegration


def get_products() -> tuple[bool, str, list]:
    try:
        success, message, products = StripeIntegration().fetch_products()
        print(f"PRINTING HERE, Type: {type(products[0])} Products: {products}")
        return success, message, products
    except Exception as e:
        logger.error(f"Unexpected Error trying to find products: {e}")
        return False, 'Unexpected error occurred', []
