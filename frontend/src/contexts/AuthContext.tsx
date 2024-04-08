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
  isAuthenticated: () => boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useLocalStorage<User>('user', { token: '', role: null });

  const login = (token: string, role: 'Administrator' | 'User') => {
    setUser({ token, role });
  };

  const logout = () => {
    setUser({ token: '', role: null });
  };

  const isAuthenticated = () => {
    return !!user.token;
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
      isAuthenticated: () => false,
    };
  }

  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }

  return context;
};