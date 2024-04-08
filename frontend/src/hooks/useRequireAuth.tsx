// hooks/useRequireAuth.tsx
import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '@/contexts/AuthContext'; // Adjust path as needed
import { useAlert } from './useAlert'; // Make sure to import useAlert

export const useRequireAuth = (requiredRole: 'Administrator' | 'User' | null = null) => {
  const { user, isAuthenticated } = useAuth();
  const { showAlert } = useAlert(); // Use showAlert to display messages
  const router = useRouter();

  useEffect(() => {
    const handleAuthCheck = async () => {
      if (!isAuthenticated()) {
        // Show an error message before redirecting
        showAlert('Unauthorized', 'Only administrators can access this page', 'error', 30000, '/login');
      } else if (requiredRole && user.role !== requiredRole) {
        // Show an error message for incorrect role before redirecting
        showAlert('Unauthorized', 'You do not have permission to access this page', 'error', 30000, '/login');
      }
    };

    handleAuthCheck();
  }, [user, isAuthenticated, requiredRole, router, showAlert]);

  // Optionally return the user object and isAuthenticated flag for use in the component
  return { user, isAuthenticated: isAuthenticated() };
};
