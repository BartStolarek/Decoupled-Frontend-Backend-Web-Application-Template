// frontend/src/utils/stripeUtils.ts
import { User } from '@/types/user';
import { useFetchData } from '@/services/serverAPI';
import { useAuth } from '@/contexts/AuthContext';
import { loadStripe, Stripe } from '@stripe/stripe-js';

const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!);
const API_URL = process.env.NEXT_PUBLIC_WEBSITE_URL;

export const formatPrice = (price: any) => {
    if (price && price.unit_amount) {
        return `$${(price.unit_amount / 100).toFixed(2)}`;
    }
    return 'Price not available';
};

export const handleFetchItems = async (endpoint: string, setItems: (items: any[]) => void) => {
    const fetchData = useFetchData();
    try {
        const response = await fetchData(endpoint, 'GET');
        if (response.status !== 200) {
            return console.error('TODO: Add in error message.');
        }
        const result = await response.json();
        if (result.data) {
            console.log(result.data);
            setItems(result.data.items);
        } else {
            throw new Error('Unexpected data format');
        }
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
};

export const handleItemAction = async (priceId: string, itemId: string, mode: 'payment' | 'subscription', successUrlPath: string) => {
    const stripe = await stripePromise;
    const { user: userAuth, isAuthenticated } = useAuth();

    // Check user is not logged in and redirect to login page
    const isUserAuthenticated = await isAuthenticated('User');
    let userData: User | null = null;
    if (!isUserAuthenticated || !userAuth) {
        console.error('User not authenticated');
        console.error('TODO: Add in error message pop up.');
        window.location.assign('/login');
    } else {
        try {
            const fetchData = useFetchData();
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
                    mode: mode,
                    successUrl: `${API_URL}${successUrlPath}?session_id={CHECKOUT_SESSION_ID}&item_id=${itemId}`,
                    cancelUrl: `${API_URL}/${mode === 'payment' ? 'products' : 'services'}`,
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