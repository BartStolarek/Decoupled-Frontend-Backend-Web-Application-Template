import React, { createContext, useContext, useState, ReactNode } from 'react';
import { useRouter } from 'next/router'; // Assuming you're using Next.js for routing

type AlertContextType = {
  message: string;
  title: string;
  type: 'success' | 'error' | 'warning';
  showAlert: (
    title: string,
    message: string,
    type: 'success' | 'error' | 'warning',
    redirect?: string | null,
    timeout?: number
  ) => void;
  hideAlert: () => void;
};

const AlertContext = createContext<AlertContextType | undefined>(undefined);

const AlertProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [alert, setAlert] = useState({ title: '', message: '', type: '' });
  const router = useRouter(); // Use Next.js useRouter hook for redirection

  const showAlert = (
    title: string,
    message: string,
    type: 'success' | 'error' | 'warning',
    redirect: string | null = null, // Default to null
    timeout: number = 105000
  ) => {
    setAlert({ title, message, type });

    setTimeout(() => {
      setAlert({ title: '', message: '', type: '' });
      if (redirect !== null) { // Explicitly check for non-null value
        router.push(redirect); // Redirect if a valid path is provided
      }
    }, timeout); // Hide (and potentially redirect) after specified timeout
  };

  const hideAlert = () => {
    setAlert({ title: '', message: '', type: '' });
  };

  return (
    <AlertContext.Provider value={{ ...alert, showAlert, hideAlert }}>
      {children}
    </AlertContext.Provider>
  );
};

export const useAlert = () => {
  const context = useContext(AlertContext);
  if (!context) {
    throw new Error('useAlert must be used within an AlertProvider');
  }
  return context;
};

export default AlertProvider;
