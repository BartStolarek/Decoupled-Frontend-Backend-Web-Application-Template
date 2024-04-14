// hooks/useRequireAuth.tsx
import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '@/contexts/AuthContext'; // Adjust path as needed
import { useAlert } from './useAlert'; // Make sure to import useAlert

export const useRequireAuth = (requiredRole: 'Administrator' | 'User' ) => {
  const { user, isAuthenticated } = useAuth();
  const { showAlert } = useAlert(); // Use showAlert to display messages
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const handleAuthCheck = async () => {
      console.log('Checking authentication for role:', requiredRole)
      setIsLoading(true);
      const isAuthorized = await isAuthenticated(requiredRole);
      if (!isAuthorized) {
        // Show an error message before redirecting
        showAlert('Unauthorized', `You can not access this page`, 'error', 30000, '/login');
      } 
      setIsLoading(false);
    };

    handleAuthCheck();
  }, [user, isAuthenticated, requiredRole, router, showAlert]);

  // Optionally return the user object and isAuthenticated flag for use in the component
  return { user, isAdminAuthenticated: isAuthenticated('Administrator'), isLoading };
};
