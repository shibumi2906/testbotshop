# bot/handlers/__init__.py
from .start import register_start_handler
from .catalog import register_catalog_handler
from .cart import register_cart_handler
from .faq import register_faq_handler

def register_handlers(dp):
    register_start_handler(dp)
    register_catalog_handler(dp)
    register_cart_handler(dp)
    register_faq_handler(dp)
