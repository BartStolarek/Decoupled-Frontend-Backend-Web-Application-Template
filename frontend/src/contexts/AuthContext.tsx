// contexts/authContext.tsx
import React, { createContext, useContext, ReactNode } from 'react';
import useLocalStorage from '@/hooks/useLocalStorage'; // Adjust path as needed

interface User {
  token: string;
  role: 'Administrator' | 'User' | null;
}

interface AuthContextType {
  user: User;
  login: (token: string, role: 'Administrator' | 'User') => void;
  logout: () => void;
  isAuthenticated: (role: 'Administrator' | 'User') => Promise<boolean>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useLocalStorage<User>('user', { token: '', role: null });

  const login = (token: string, role: 'Administrator' | 'User') => {
    setUser({ token, role });
    console.log('User Logged in, token:', token, 'role:', role)
  };

  const logout = () => {
    setUser({ token: '', role: null });
    console.log('User Logged out')
  };

  const isAuthenticated = async (role: 'Administrator' | 'User') => {
    if (!user || !user.token) {
      console.log('User not found or token not found, authentication failed')
      return false;
    }

    try {
      if (role === 'Administrator') {
        // Call the API for Administrator role authentication
        const API_URL = process.env.NEXT_PUBLIC_API_URL;
        const response = await fetch(`${API_URL}/api/auth/admin`, {
          method: 'GET',
          headers: {
            Authorization: `Bearer ${user.token}`,
          },
        })
        console.log('Admin authentication response:', response)
        if (response.ok) {
          console.log('Admin authentication successful')
          return true;
        } else {
          console.log('Admin authentication failed')
          return false;
        }
        
      } else if (role === 'User') {
        // TODO: Implement user api authentication
        console.log('User authentication not implemented yet')
      }
    } catch (error) {
      console.error('Authentication error:', error);
      return false;
    }

    return false;
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, isAuthenticated }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  
  if (typeof window === 'undefined') {
    // Return a default object that matches the shape of AuthContextType
    // to avoid breaking SSR with a missing context error.
    return {
      user: { token: '', role: null },
      login: () => {},
      logout: () => {},
      isAuthenticated: () => Promise.resolve(false),
    };
  }
  
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  
  return context;
};