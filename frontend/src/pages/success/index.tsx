import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import Stripe from 'stripe';
import { useFetchData } from '@/services/serverAPI';

const SuccessPage: React.FC = () => {
  const router = useRouter();
  const { session_id, product_id } = router.query;
  const [sessionData, setSessionData] = useState<Stripe.Checkout.Session | null>(null);
  const fetchData = useFetchData();

  useEffect(() => {
    const fetchSessionData = async () => {
      if (session_id && typeof session_id === 'string') {
        
        const response = await fetchData(`/api/v1/stripe/session/${session_id}`, 'GET')

        if (response.status !== 200) {
          return console.error('TODO: Add in error message.');
        }

        const result = await response.json();
        setSessionData(result);
      }
    };

    fetchSessionData();
  }, [session_id]);

  return (
    <div>
      <h1>Payment Successful</h1>
      {sessionData && (
        <div>
          <p>Checkout Session ID: {sessionData.id}</p>
          <p>Customer Email: {sessionData.customer_details?.email}</p>
          {/* Display other relevant session data */}
        </div>
      )}
      {/* Display order summary using the product_id */}
    </div>
  );
};

export default SuccessPage;