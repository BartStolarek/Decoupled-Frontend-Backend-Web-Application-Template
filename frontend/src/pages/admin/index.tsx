import React, { useEffect, ReactNode, useState } from "react";
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import { useRouter } from 'next/router';
import DefaultLayout from '../../components/Layouts/DefaultLayout';
import { useAuth } from "@/contexts/AuthContext";
import { useAlert } from '@/contexts/AlertContext';
import AlertComponent from '@/components/Alert';
import useRequireAuth from '@/hooks/useRequireAuth'


const IndexAdminPage: React.FC<{ children: ReactNode }> = ({ children }) => {

  //const { loading } = useRequireAuth("Administrator");

  const { isAuthenticated, loading, error } = useAuth();
  const { showAlert } = useAlert();
  const router = useRouter();

  const [redirectInitiated, setRedirectInitiated] = useState(false);

  useEffect(() => {
    if (!loading && !redirectInitiated) {
      const role = localStorage.getItem('user_role');
      if (!isAuthenticated || role !== 'Administrator') {
        showAlert(
          'Unauthorized',
          'You are not authorized to access this page.',
          'error',
          '/',
          20000
        );
        setRedirectInitiated(true); // Prevent further redirects
        
      }
    }
  }, [isAuthenticated, loading, error, router, showAlert, redirectInitiated]);


  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <Navbar />
      <AlertComponent />
      <DefaultLayout>
        {children}
      </DefaultLayout>
      <Footer />
    </>
  );
};

export default IndexAdminPage;
