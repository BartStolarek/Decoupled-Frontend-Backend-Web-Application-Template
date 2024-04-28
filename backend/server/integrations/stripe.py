import os
import stripe
from flask import jsonify
from loguru import logger


class StripeIntegration:
    def __init__(self):
        """
        Initialize the Stripe API with the secret key from environment variables.
        """
        self.api_key = os.getenv("STRIPE_SECRET_KEY")
        if not self.api_key:
            raise ValueError("Stripe API key (STRIPE_SECRET_KEY) is not set in environment variables.")
        stripe.api_key = self.api_key

    def fetch_products(self, limit=10000):
        """
        Fetches a list of products from Stripe, limited by the specified number.
        :param limit: Number of products to fetch.
        :return: JSON response containing product data.
        """
        try:
            products = stripe.Product.list(limit=limit)
            product_data = [product for product in products.auto_paging_iter()]
            logger.info(f"Fetched {len(product_data)} products from Stripe.")
            return True, "successfully obtained products", product_data
        except stripe.error.StripeError as e:
            logger.error(f"Stripe error: {e}")
            return False, "Stripe error occurred", []
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            return False, "Unexpected error occurred", []
        
    def fetch_price(self, price_id):
        """
        Fetches the price details from Stripe using the given price ID.
        :param price_id: The ID of the price to fetch.
        :return: Price object if found, otherwise None.
        """
        try:
            price = stripe.Price.retrieve(price_id)
            logger.info(f"Fetched price details for {price_id} = {price}")
            return price
        except stripe.error.InvalidRequestError:
            return None
        
    def fetch_session_by_id(self, session_id):
        """
        Fetches the session details from Stripe using the given session ID.
        :param session_id: The ID of the session to fetch.
        :return: Session object if found, otherwise None.
        """
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            logger.info(f"Fetched session details for {session_id}")
            return session
        except stripe.error.InvalidRequestError:
            return None
