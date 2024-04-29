import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import Stripe from 'stripe';
import { useFetchData } from '@/services/serverAPI';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';

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
                setSessionData(result.data.session);
            }
        };

        fetchSessionData();
    }, [session_id]);

    console.log('sessionData:', sessionData)

    const convertUnixTimeToLocalString = (unixTime: number) => {
        const date = new Date(unixTime * 1000);
        return date.toLocaleString();
    };

    

    return (
        <>
            <Navbar />
            <section className="py-24 relative">
                <div className="w-full max-w-7xl px-4 md:px-5 lg-6 mx-auto">
                    <h2 className="font-bold text-4xl leading-10 text-accent text-center">
                        {sessionData && sessionData.mode === 'subscription' ? 'Subscription ' : 'Payment '}
                        Successful
                    </h2>
                    <p className="mt-4 font-normal text-lg leading-8 text-gray-500 mb-11 text-center">Thanks for making a purchase
                        you can
                        check our order summary form below</p>
                    {sessionData ? (
                    <div className="main-box border border-gray-200 rounded-xl pt-6 max-w-xl max-lg:mx-auto lg:max-w-full">
                        <div
                            className="flex flex-col lg:flex-row lg:items-center justify-between px-6 pb-6 border-b border-gray-200">
                            <div className="data">
                                <p className=" text-base leading-7 text-black">Order Id: <span className="text-secondary font-medium"># {sessionData!.client_reference_id}</span></p>
                                <p className=" text-base leading-7 text-black mt-4">Order Payment : <span className="text-gray-400 font-medium"> {convertUnixTimeToLocalString(sessionData!.created)}</span></p>
                            </div>
                            
                        </div>
                        
                        <div className="w-full border-gray-200 px-6 flex flex-col lg:flex-row items-center justify-between ">
                            
                            <p className=" text-lg text-black py-6">Total Price: <span className="text-secondary"> $200.00</span></p>
                        </div>

                    </div>
                    ) : (
                        <p>Loading session data...</p>
                    )}
                </div>
            </section>

            <Footer />
        </>
    );
};

export default SuccessPage;