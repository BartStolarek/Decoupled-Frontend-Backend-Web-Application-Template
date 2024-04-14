import React, { createContext, useContext, useState, ReactNode } from 'react';

type UserContextType = {
    userId: string | null;
    updateUser: (id: string | null) => void;
};

const UserContext = createContext<UserContextType | undefined>(undefined);

export const useUser = () => {
    const context = useContext(UserContext);
    if (context === undefined) {
        throw new Error('useUser must be used within a UserProvider');
    }
    return context;
};

type UserProviderProps = {
    children: ReactNode;
};

export const UserProvider: React.FC<UserProviderProps> = ({ children }) => {
    const [userId, setUserId] = useState<string | null>(null);

    const updateUser = (id: string | null) => {
        console.log('Updating userId to:', id); // Log the new userId value
        setUserId(id);
    };

    // Optionally, log the current userId state when it changes
    React.useEffect(() => {
    }, [userId]);

    return (
        <UserContext.Provider value={{ userId, updateUser }}>
            {children}
        </UserContext.Provider>
    );
};
