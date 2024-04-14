import React, { createContext, useContext, useState, ReactNode, useCallback } from 'react';
import { useRouter } from 'next/router';

type AlertType = 'success' | 'warning' | 'error' | 'info';

interface AlertContextType {
  showAlert: (title: string, message: string, type: AlertType, timeout?: number, redirectTo?: string) => void;
  hideAlert: () => void;
  alert: { title: string, message: string; type: AlertType } | null;
}

const AlertContext = createContext<AlertContextType | undefined>(undefined);

export { AlertContext };

export const AlertProvider = ({ children }: { children: ReactNode }) => {

  const [alert, setAlert] = useState<{ title: string, message: string; type: AlertType } | null>(null);
  const router = useRouter();

  const showAlert = useCallback((title: string, message: string, type: AlertType, timeout = 0, redirectTo?: string) => {
    setAlert({ title, message, type });

    if (timeout > 0) {
      setTimeout(() => {
        setAlert(null);
        if (redirectTo) {
          router.push(redirectTo);
        }
      }, timeout);
    }
  }, [router]);

  const hideAlert = useCallback(() => {
    setAlert(null);
  }, []);

  return (
    <AlertContext.Provider value={{ showAlert, hideAlert, alert }}>
      {children}
    </AlertContext.Provider>
  );
};


