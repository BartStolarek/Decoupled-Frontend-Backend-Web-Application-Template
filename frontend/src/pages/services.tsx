import React, { useState, useEffect } from 'react';
import { loadStripe, Stripe } from '@stripe/stripe-js';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { useFetchData } from '@/services/serverAPI';
import { useAuth } from '@/contexts/AuthContext';
import { User } from '@/types/user';

const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!);

const API_URL = process.env.NEXT_PUBLIC_WEBSITE_URL;

const ServicesPage: React.FC = () => {
    const [services, setServices] = useState<any[]>([]);
    const fetchData = useFetchData();
    const { user: userAuth, isAuthenticated } = useAuth();

    const handleFetchServices = async () => {
        try {
            const response = await fetchData(`/api/v1/stripe/service/all`, 'GET');
            if (response.status !== 200) {
                return console.error('TODO: Add in error message.');
            }
            const result = await response.json();
            if (result.data) {
                console.log(result.data);
                const sortedServices = result.data.services.sort((a, b) => {
                    const priceA = a.display_price ? a.display_price.unit_amount : a.default_price.unit_amount;
                    const priceB = b.display_price ? b.display_price.unit_amount : b.default_price.unit_amount;
                    return priceA - priceB;
                });
                setServices(sortedServices);
            } else {
                throw new Error('Unexpected data format');
            }
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    };

    useEffect(() => {
        handleFetchServices();
    }, []);

    const formatPrice = (price: any) => {
        if (price && price.unit_amount) {
            return `$${(price.unit_amount / 100).toFixed(2)}`;
        }
        return 'Price not available';
    };

    const handleSignUp = async (priceId: string, serviceId: string) => {
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
                        mode: 'subscription',
                        successUrl: `${API_URL}/success?session_id={CHECKOUT_SESSION_ID}&service_id=${serviceId}`,
                        cancelUrl: `${API_URL}/services`,
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
                {services.map(service => (
                    <div key={service.id} className="card w-96 glass my-4">
                        <figure>
                            <img src={service.images[0]} alt={service.name} className="w-full h-48 object-cover" />
                        </figure>
                        <div className="card-body">
                            <h2 className="card-title">{service.name}</h2>
                            <p>{service.description}</p>
                            <div className="card-actions justify-between items-center">
                                <div className="text-lg font-bold">
                                    {service.display_price ? formatPrice(service.display_price) : formatPrice(service.default_price)}
                                </div>
                                <button
                                    className="btn btn-primary"
                                    onClick={() => handleSignUp(service.display_price.id, service.id)}
                                >
                                    Sign Up
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

export default ServicesPage;