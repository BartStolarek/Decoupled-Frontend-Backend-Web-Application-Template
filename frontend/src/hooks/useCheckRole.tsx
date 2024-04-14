// hooks/useCheckRole.tsx
import { useEffect, useState } from 'react';
import { useAuth } from '@/contexts/AuthContext';

const useCheckRole = () => {
  const { user } = useAuth();
  const [isLoading, setIsLoading] = useState(true);
  const [userRole, setUserRole] = useState<'Administrator' | 'User' | null>(null);

  useEffect(() => {
    const checkUserRole = async () => {
      setIsLoading(true);
      if (user && user.token && user.role === 'Administrator') {
        setUserRole('Administrator');
      } else if (user && user.token && user.role === 'User') {
        setUserRole('User');
      } else {
        setUserRole(null);
      }
      setIsLoading(false);
    };
    checkUserRole();
  }, [user]);

  return { isLoading, userRole };
};

export default useCheckRole;