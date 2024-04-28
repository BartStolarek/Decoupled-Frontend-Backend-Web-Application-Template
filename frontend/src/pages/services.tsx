import React, { useState, useEffect } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { useFetchData } from '@/services/serverAPI';

const ServicesPage: React.FC = () => {
  const [services, setServices] = useState<any[]>([]);
  const fetchData = useFetchData();

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
                <button className="btn btn-primary">Sign Up</button>
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