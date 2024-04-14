import React, { ReactNode, useEffect } from "react";
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import DefaultLayout from '@/components/Layouts/DefaultLayout';
import { useRequireAuth } from '@/hooks/useRequireAuth'; // Make sure the path is correct

// Assuming Metadata and other imports are correctly set up
export const metadata = {
    title: "Next.js Buttons | TailAdmin - Next.js Dashboard Template",
    description:
        "This is Next.js Buttons page for TailAdmin - Next.js Tailwind CSS Admin Dashboard Template",
};

const IndexAdminPage: React.FC<{ children: ReactNode }> = ({ children }) => {
    // Use the useRequireAuth hook to check for "Administrator" role
    const { isLoading } = useRequireAuth('Administrator');

    if (isLoading) {
        return <div>Loading...</div>
    }

    return (
        <>
            <Navbar />
            <DefaultLayout>
                {children}
            </DefaultLayout>
            <Footer />
        </>
    );
};

export default IndexAdminPage;
