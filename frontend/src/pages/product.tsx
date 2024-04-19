import React, { useState, useEffect } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';
import { useFetchData } from '@/services/api'


const ProductPage: React.FC = () => {

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
            setProducts(result.data.products)
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

  return (
    <>
      <Navbar />
      <div className="container mx-auto p-4">
        {products.map(product => (
          <div key={product.id} className="card w-96 glass my-4">
            <figure><img src="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg" alt={product.name} /></figure>
            <div className="card-body">
              <h2 className="card-title">{product.name}</h2>
              <p>{product.description}</p>
              <div className="card-actions justify-end">
                <button className="btn btn-primary">Learn now!</button>
              </div>
            </div>
          </div>
        ))}
      </div>
      
      <Footer />
    </>
  );
};

export default ProductPage;