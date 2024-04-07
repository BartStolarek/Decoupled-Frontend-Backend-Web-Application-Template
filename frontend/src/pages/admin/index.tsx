import React, { ReactNode } from "react";
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';
import DefaultLayout from '@/components/Layouts/DefaultLayout';
import AlertComponent from '@/components/Alert';
import useRequireAuth from '@/hooks/useRequireAuth';
import { Metadata } from "next";

export const metadata: Metadata = {
    title: "Next.js Buttons | TailAdmin - Next.js Dashboard Template",
    description:
        "This is Next.js Buttons page for TailAdmin - Next.js Tailwind CSS Admin Dashboard Template",
};

const IndexAdminPage: React.FC<{ children: ReactNode }> = ({ children }) => {
    const { isAuthenticated, loading } = useRequireAuth("Administrator");

    // If the authentication status is loading or the user is not authenticated,
    // show a loading indicator or another placeholder. This prevents the page
    // content from being rendered until the authentication process is complete.
    if (loading || !isAuthenticated) {
        return <div>Loading...</div>;
    }

    // Once authenticated and loading is complete, render the page content.
    return (
        <>
            <Navbar />
            <AlertComponent />  // Ensure AlertComponent is properly set up to listen and respond to alerts from AlertContext.
            <DefaultLayout>
                {children}
            </DefaultLayout>
            <Footer />
        </>
    );
};

export default IndexAdminPage;
