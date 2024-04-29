import React, { useState, useEffect } from 'react';
import { loadStripe, Stripe } from '@stripe/stripe-js';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { useFetchData } from '@/services/serverAPI';
import { useAuth } from '@/contexts/AuthContext';
import { User } from '@/types/user';
import { formatPrice, handleFetchItems, handleItemAction } from '@/utils/stripe';

const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!);

const API_URL = process.env.NEXT_PUBLIC_WEBSITE_URL;

const ProductsPage: React.FC = () => {
    const [products, setProducts] = useState<any[]>([]);
    const fetchData = useFetchData();
    const { user: userAuth, isAuthenticated } = useAuth();

    const handleFetchProducts = async () => {
        try {
            const response = await fetchData(`/api/v1/stripe/product/all`, 'GET');
            if (response.status !== 200) {
                return console.error('TODO: Add in error message.');
            }
            const result = await response.json();
            if (result.data) {
                console.log(result.data);
                setProducts(result.data.products);
            } else {
                throw new Error('Unexpected data format');
            }
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    };

    useEffect(() => {
        handleFetchProducts();
    }, []);

    const formatPrice = (price: any) => {
        if (price && price.unit_amount) {
            return `$${(price.unit_amount / 100).toFixed(2)}`;
        }
        return 'Price not available';
    };

    const handleBuyNow = async (priceId: string, productId: string) => {
        const stripe = await stripePromise;

        // Check user is not logged in and redirect to login page
        const isUserAuthenticated = await isAuthenticated('User');
        let userData: User | null = null;
        if (!isUserAuthenticated || !userAuth) {
            console.error('User not authenticated');
            console.error('TODO: Add in error message pop up.');
            window.location.assign('/login');
        } else {
            try {
                const response = await fetchData(`/api/v1/user/${userAuth.user_id}`, 'GET');
                if (response.status !== 200) {
                    console.error('Error fetching user data');
                    console.error('TODO: Add in error message pop up.');
                    return;
                }

                const result = await response.json();
                userData = result.data.user as User;

                if (stripe) {
                    const { error } = await stripe.redirectToCheckout({
                        lineItems: [{ price: priceId, quantity: 1 }],
                        mode: 'payment',
                        successUrl: `${API_URL}/success?session_id={CHECKOUT_SESSION_ID}&product_id=${productId}`,
                        cancelUrl: `${API_URL}/products`,
                        customerEmail: userData!.email,
                        clientReferenceId: 'your_reference_id',
                    });
                    if (error) {
                        console.error('Error redirecting to Stripe Checkout:', error);
                        console.error('TODO: Add in error message pop up.');
                    }
                }


            } catch (error) {
                console.error("Error fetching user data: ", error);
                return;
            }
        }

        
    };

    return (
        <>
            <Navbar />
            <div className="container mx-auto p-4">
                {products.map(product => (
                    <div key={product.id} className="card w-96 glass my-4">
                        <figure>
                            <img src={product.images[0]} alt={product.name} className="w-full h-48 object-cover" />
                        </figure>
                        <div className="card-body">
                            <h2 className="card-title">{product.name}</h2>
                            <p>{product.description}</p>
                            <div className="card-actions justify-between items-center">
                                <div className="text-lg font-bold">
                                    {product.display_price ? formatPrice(product.display_price) : formatPrice(product.default_price)}
                                </div>
                                <button
                                    className="btn btn-primary"
                                    onClick={() => handleBuyNow(product.display_price.id, product.id)}
                                >
                                    Buy now
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
            <Footer />
        </>
    );
};

export default ProductsPage;