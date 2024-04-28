// src/services/api.ts
import { useAuth } from '@/contexts/AuthContext';

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export const useFetchData = () => {
  const { user } = useAuth();

  const fetchData = async (endpoint: string, method: string, data?: any) => {
    try {
      const headers: any = {
        'Content-Type': 'application/json',
      };

      if (user && user.token) {
        headers['Authorization'] = `Bearer ${user.token}`;
      }

      const options: RequestInit = {
        method,
        headers,
      };

      if (data) {
        options.body = JSON.stringify(data);
      }

      const response = await fetch(`${API_URL}${endpoint}`, options);
      return response;
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
      throw error;
    }
  };

  return fetchData;
};