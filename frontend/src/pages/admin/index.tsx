import React, { useState, ReactNode } from "react";
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import { useEffect } from 'react';
import { useRouter } from 'next/router';
import DefaultLayout from '../../components/Layouts/DefaultLayout'


const IndexAdminPage: React.FC<{ children: ReactNode }> = ({ children }) => {
    const router = useRouter();
    const [sidebarOpen, setSidebarOpen] = useState(false);

    useEffect(() => {
        const role = localStorage.getItem('user_role');
        if (role !== 'Administrator') {
        router.push('/'); // Redirect to the home page or a 'not authorized' page
        }
    }, [router]);
  return (
    <>
      <Navbar />
      <DefaultLayout>
        {children}
      </DefaultLayout>
      <Footer />
    </>
  );
};

export default IndexAdminPage;
