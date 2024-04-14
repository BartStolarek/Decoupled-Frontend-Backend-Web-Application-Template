// contexts/authContext.tsx
import React, { createContext, useContext, ReactNode, useEffect } from 'react';
import useLocalStorage from '@/hooks/useLocalStorage'; // Adjust path as needed
import { parse } from 'path';


interface User {
    token: string;
    role: 'Administrator' | 'User' | null;
}

interface AuthContextType {
    user: User | null;
    login: (token: string, role: 'Administrator' | 'User') => void;
    logout: () => void;
    isAuthenticated: (role: 'Administrator' | 'User') => Promise<boolean>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
    const [user, setUser] = useLocalStorage<User | null>('user', null);

    const login = (token: string, role: 'Administrator' | 'User') => {
        setUser({ token, role });
        console.log('User Logged in, role:', role)
    };

    const logout = () => {
        // Here we just need to pass null to setUser to remove the user from localStorage
        setUser(null);
        console.log('User Logged out');
    };

    function parseJwt(token: string) {
        if (!token) { return; }
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace('-', '+').replace('_', '/');
        return JSON.parse(window.atob(base64));
    };

    const decodeUserRole = (token: string) => {
        const decodedToken = parseJwt(token);
        const userRole = decodedToken.user_role;
        return userRole;
    }

    const refreshToken = async () => {

        if (!user || !user.token) {
            return;
        }

        if (sessionStorage.getItem('tokenRefreshed')) {
            console.log('Token already refreshed')
            return;
        }

        sessionStorage.setItem('tokenRefreshed', 'true');

        if (!user || !user.token) {
            console.log('User not found or token not found, authentication failed')
            return false;
        }
        // Call the API for Administrator role authentication
        const API_URL = process.env.NEXT_PUBLIC_API_URL;
        const response = await fetch(`${API_URL}/api/auth/refresh`, {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${user.token}`,
            },
        })
        console.log('Refresh response:', response)
        if (response.ok) {
            const data = await response.json();
            const user_role = decodeUserRole(data.data.user_token);
            setUser({ token: data.data.user_token, role: user_role })
            console.log('Refresh successful')
            return true;
        } else {
            console.log('Refreshed failed')
            return false;
        }
    };


    const isAuthenticated = async (role: 'Administrator' | 'User' | null) => {
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
                // Call the API for Administrator role authentication
                const API_URL = process.env.NEXT_PUBLIC_API_URL;
                const response = await fetch(`${API_URL}/api/auth/user`, {
                    method: 'GET',
                    headers: {
                        Authorization: `Bearer ${user.token}`,
                    },
                })
                console.log('User authentication response:', response)
                if (response.ok) {
                    console.log('User authentication successful')
                    return true;
                } else {
                    console.log('User authentication failed')
                    return false;
                }
            }
        } catch (error) {
            console.error('Authentication error:', error);
            return false;
        }

        return false;
    };

    useEffect(() => {
        refreshToken();
    }, []);

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
            login: () => { },
            logout: () => { },
            isAuthenticated: () => Promise.resolve(false),
        };
    }

    if (context === undefined) {
        throw new Error('useAuth must be used within an AuthProvider');
    }

    return context;
};