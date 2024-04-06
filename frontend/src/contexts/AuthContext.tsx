import React, { createContext, useContext, useState, useEffect } from 'react';

type AuthContextType = {
    isAuthenticated: boolean;
    loading: boolean;
    error: string;
    checkAuthentication: () => Promise<void>;
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    const checkAuthentication = async () => {
        setLoading(true);
        const token = localStorage.getItem('user_token');

        if (!token) {
            setIsAuthenticated(false);
            setLoading(false);
            setError('User not authorized for access to this page'); // Set an appropriate error message
            return;
        }


        // Perform API check here
        try {
            const API_URL = process.env.NEXT_PUBLIC_API_URL;
            const response = await fetch(`${API_URL}/api/auth/admin`, {
                headers: { Authorization: `Bearer ${localStorage.getItem('user_token')}` }
            });

            // Inside checkAuthentication:
            if (response.status === 200) {
                setIsAuthenticated(true);
                setError(''); // Clear any previous error
            } else {
                setIsAuthenticated(false);
                setError('User not authorized for access to this page'); // Set an appropriate error message
            }
        } catch (error) {
            console.error('Failed to verify authentication:', error);
            setIsAuthenticated(false);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        const currentRoute = window.location.pathname;
        if (currentRoute.startsWith('/admin')) {
            checkAuthentication();
        } else {
            setLoading(false);
        }
    }, []);

    return (
        <AuthContext.Provider value={{ isAuthenticated, loading, checkAuthentication, error }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (context === undefined) {
        throw new Error('useAuth must be used within an AuthProvider');
    }
    return context;
};
