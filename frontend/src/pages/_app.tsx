import React from 'react';
import type { AppProps } from 'next/app';
import Head from 'next/head';
import '../styles/output.css';
import { UserProvider } from '@/contexts/UserContext';
import { AuthProvider } from '@/contexts/AuthContext';
import { AlertProvider } from '@/contexts/AlertContext';
import AlertOverlay from '@/components/AlertOverlay';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>My App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      </Head>
      <AlertProvider>
        <AlertOverlay />
        <AuthProvider>
          <UserProvider>
            <Component {...pageProps} />
          </UserProvider>
        </AuthProvider>
      </AlertProvider>
    </>
  );
}

export default MyApp;