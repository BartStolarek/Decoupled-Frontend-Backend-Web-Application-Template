// hooks/useRequireAuth.tsx
import { useEffect, useState } from 'react';
import { useAuth } from '@/contexts/AuthContext'; // Adjust path as needed

const useCheckAuth = () => {
    const { user, isAuthenticated } = useAuth();
    const [isLoading, setIsLoading] = useState(true);
    const [userRole, setUserRole] = useState<'Administrator' | 'User' | null>(null);
  
    useEffect(() => {
      const checkUserRole = async () => {
        setIsLoading(true);
        if (user) {
          const isAdmin = await isAuthenticated('Administrator');
          setUserRole(isAdmin ? 'Administrator' : 'User');
        } else {
          setUserRole(null);
        }
        setIsLoading(false);
      };
      checkUserRole();
    }, [user, isAuthenticated]);
  
    return { isLoading, userRole };
  };
  
  export default useCheckAuth;