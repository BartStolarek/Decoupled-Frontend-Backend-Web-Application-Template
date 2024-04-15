import React, { useState, useEffect } from 'react';
import DatabaseDynamicTable, { SortConfig } from './DatabaseDynamicTable';
import { User } from '@/types/user';
import { useFetchData } from '@/services/api';

const DatabaseUsersTable = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [sortConfig, setSortConfig] = useState<SortConfig>({ key: null, direction: 'ascending' });
    const fetchData = useFetchData();


    // Fetch data from API user all endpoint
  const handleFetchedUsers = async () => {
    try {
      const response = await fetchData('/api/user/all', 'GET');
      const result = await response.json();
      if (result.data && Array.isArray(result.data.users)) {
        setUsers(result.data.users);
      } else {
        throw new Error('Unexpected data format');
      }
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  };

    useEffect(() => {
        handleFetchedUsers();
    }, []);

    const handleSort = (key: keyof User) => {
        setSortConfig((current: SortConfig) => ({
            key,
            direction: current.key === key && current.direction === 'ascending' ? 'descending' : 'ascending',
        }));
    };

    const handleEdit = (userId: number) => {
        // Implement the logic to handle editing a user
        console.log('Edit user with ID:', userId);
    };

    const handleDelete = (userId: number) => {
        // Implement the logic to handle deleting a user
        console.log('Delete user with ID:', userId);
    };

    return (
        <DatabaseDynamicTable
            data={users}
            onSort={handleSort}
            sortConfig={sortConfig}
            includeActions={true}
            renderActions={(user: User) => (
                <>
                    <button onClick={() => handleEdit(user.id)}>Edit</button>
                    <button onClick={() => handleDelete(user.id)}>Delete</button>
                </>
            )}
        />
    );
};

export default DatabaseUsersTable;