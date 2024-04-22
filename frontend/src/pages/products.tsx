import React, { useState, useEffect } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { useFetchData } from '@/services/api';

const ProductsPage: React.FC = () => {
  const [products, setProducts] = useState<any[]>([]);
  const fetchData = useFetchData();

  const handleFetchProducts = async () => {
    try {
      const response = await fetchData(`/api/v1/product/all`, 'GET');
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

  return (
    <>
      <Navbar />
      <div className="container mx-auto p-4">
        {products.map(product => (
          <div key={product.id} className="card w-96 glass my-4">
            <figure>
              <img
                src={product.images[0]}
                alt={product.name}
                className="w-full h-48 object-cover"
              />
            </figure>
            <div className="card-body">
              <h2 className="card-title">{product.name}</h2>
              <p>{product.description}</p>
              <div className="card-actions justify-between items-center">
                <div className="text-lg font-bold">
                  {product.display_price
                    ? formatPrice(product.display_price)
                    : formatPrice(product.default_price)}
                </div>
                <button className="btn btn-primary">Buy now</button>
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