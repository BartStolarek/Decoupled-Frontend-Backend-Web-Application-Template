import React, { useState, useEffect } from 'react';
import { User } from '@/types/user';
import { useRouter } from 'next/router';
import { useUser } from '@/contexts/UserContext';
import { useAuth } from '@/contexts/AuthContext';

// Define a type for the keys of User that you will sort by
type UserKey = keyof User | undefined;

// Define the SortConfig type
type SortConfig = {
    key: UserKey | null;
    direction: 'ascending' | 'descending';
};


const DatabaseUsersTable = () => {

    const [users, setUsers] = useState<User[]>([]);
    const [sortConfig, setSortConfig] = useState<SortConfig>({ key: null, direction: 'ascending' });
    const router = useRouter();
    const { updateUser } = useUser(); // Use the context to get access to updateUser
    const { user: authUser } = useAuth();


    useEffect(() => {
        const fetchUsers = async () => {
            try {
                if (authUser) {
                    const API_URL = process.env.NEXT_PUBLIC_API_URL;
                    const response = await fetch(`${API_URL}/api/user/all`, { // Ensure endpoint is correct
                        method: 'GET',
                        headers: {
                            'Authorization': `Bearer ${authUser.token}`,
                        },
                    });

                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }

                    const result = await response.json();
                    if (result.data && Array.isArray(result.data.users)) {
                        setUsers(result.data.users); // Setting state correctly based on response structure
                    } else {
                        throw new Error('Unexpected data format');
                    }
                }
            } catch (error) {
                console.error('There was a problem with the fetch operation:', error);
            }
        };

        fetchUsers();
    }, []);

    const requestSort = (key: UserKey) => {
        setSortConfig(currentSortConfig => {
            if (currentSortConfig.key === key && currentSortConfig.direction === 'descending') {
                return { key: null, direction: 'ascending' };
            }
            let direction: 'ascending' | 'descending' = 'ascending'; // Explicit type here
            if (currentSortConfig.key === key && currentSortConfig.direction === 'ascending') {
                direction = 'descending';
            }
            return { key, direction };
        });
    };



    const sortedUsers = React.useMemo(() => {
        let sortableUsers = [...users];
        if (sortConfig.key && typeof sortConfig.key !== 'undefined' && sortConfig.key in users[0]) {
            const key = sortConfig.key; // It's safe to use key directly now
            sortableUsers.sort((a, b) => {
                // Initialize variables for comparison
                let valueA: string | number = a[key];
                let valueB: string | number = b[key];

                // Check and convert only if they are strings
                if (typeof valueA === 'string') {
                    valueA = valueA.toLowerCase();
                }
                if (typeof valueB === 'string') {
                    valueB = valueB.toLowerCase();
                }

                // Now compare the values, which are either numbers or lowercase strings
                if (valueA < valueB) {
                    return sortConfig.direction === 'ascending' ? -1 : 1;
                }
                if (valueA > valueB) {
                    return sortConfig.direction === 'ascending' ? 1 : -1;
                }
                return 0;
            });
        }
        return sortableUsers;
    }, [users, sortConfig]);






    const navigateToSettings = (userId: string) => {
        updateUser(userId); // Update the global state with the selected user ID
        router.push(`/settings`); // Navigate to settings without adding userId to the URL
    };


    return (
        <div className="rounded-sm border border-stroke bg-white px-5 pb-2.5 pt-6 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
            <h4 className="mb-6 text-xl font-semibold text-black dark:text-white">
                Database Users
            </h4>
            <div className="max-w-full overflow-x-auto">
                <table className="w-full table-auto">
                    <thead>
                        <tr className="bg-gray-200 text-left dark:bg-meta-4">
                            <th
                                className={`px-4 py-4 font-medium cursor-pointer ${sortConfig.key === 'id' ? 'text-blue-600' : 'text-black'} dark:text-white`}
                                onClick={() => requestSort('id')}
                            >
                                ID {sortConfig.key === 'id' ? (sortConfig.direction === 'ascending' ? '↑' : '↓') : ''}
                            </th>
                            <th
                                className={`px-4 py-4 font-medium cursor-pointer ${sortConfig.key === 'first_name' ? 'text-blue-600' : 'text-black'} dark:text-white`}
                                onClick={() => requestSort('first_name')}
                            >
                                First Name {sortConfig.key === 'first_name' ? (sortConfig.direction === 'ascending' ? '↑' : '↓') : ''}
                            </th>
                            <th
                                className={`px-4 py-4 font-medium cursor-pointer ${sortConfig.key === 'last_name' ? 'text-blue-600' : 'text-black'} dark:text-white`}
                                onClick={() => requestSort('last_name')}
                            >
                                Last Name {sortConfig.key === 'last_name' ? (sortConfig.direction === 'ascending' ? '↑' : '↓') : ''}
                            </th>
                            <th
                                className={`px-4 py-4 font-medium cursor-pointer ${sortConfig.key === 'email' ? 'text-blue-600' : 'text-black'} dark:text-white`}
                                onClick={() => requestSort('email')}
                            >
                                Email {sortConfig.key === 'email' ? (sortConfig.direction === 'ascending' ? '↑' : '↓') : ''}
                            </th>
                            <th
                                className={`px-4 py-4 font-medium cursor-pointer ${sortConfig.key === 'role_id' ? 'text-blue-600' : 'text-black'} dark:text-white`}
                                onClick={() => requestSort('role_id')}
                            >
                                Role ID {sortConfig.key === 'role_id' ? (sortConfig.direction === 'ascending' ? '↑' : '↓') : ''}
                            </th>
                            <th
                                className={`px-4 py-4 font-medium cursor-pointer ${sortConfig.key === 'created_utc' ? 'text-blue-600' : 'text-black'} dark:text-white`}
                                onClick={() => requestSort('created_utc')}
                            >
                                Created {sortConfig.key === 'created_utc' ? (sortConfig.direction === 'ascending' ? '↑' : '↓') : ''}
                            </th>
                            <th
                                className={`px-4 py-4 font-medium cursor-pointer ${sortConfig.key === 'updated_utc' ? 'text-blue-600' : 'text-black'} dark:text-white`}
                                onClick={() => requestSort('updated_utc')}
                            >
                                Updated {sortConfig.key === 'updated_utc' ? (sortConfig.direction === 'ascending' ? '↑' : '↓') : ''}
                            </th>
                            <th className="px-4 py-4 font-medium text-black dark:text-white">
                                Actions
                            </th>
                        </tr>
                    </thead>

                    <tbody>
                        {sortedUsers.map((user, index) => (
                            <tr key={index} className="border-b border-stroke dark:border-strokedark">
                                <td className="px-4 py-5">{user.id}</td>
                                <td className="px-4 py-5">{user.first_name}</td>
                                <td className="px-4 py-5">{user.last_name}</td>
                                <td className="px-4 py-5">{user.email}</td>
                                <td className="px-4 py-5">{user.role_id}</td>
                                <td className="px-4 py-5">{user.created_utc}</td>
                                <td className="px-4 py-5">{user.updated_utc}</td>
                                <td className="px-4 py-5">
                                    <div className="flex items-center space-x-3.5">

                                        <button onClick={() => navigateToSettings(String(user.id))} className="hover:text-danger">
                                            <svg
                                                className="fill-current"
                                                width="18"
                                                height="18"
                                                viewBox="0 0 24 24"
                                                xmlns="http://www.w3.org/2000/svg"
                                            >
                                                <path
                                                    d="M3 17.25V21H6.75L17.81 9.94L14.06 6.19L3 17.25ZM20.71 7.04C21.1 6.65 21.1 6.02 20.71 5.63L18.37 3.29C17.98 2.9 17.35 2.9 16.96 3.29L15.13 5.12L18.88 8.87L20.71 7.04Z"
                                                />
                                            </svg>

                                        </button>
                                        <button className="hover:text-primary">
                                            <svg
                                                className="fill-current"
                                                width="18"
                                                height="18"
                                                viewBox="0 0 18 18"
                                                fill="none"
                                                xmlns="http://www.w3.org/2000/svg"
                                            >
                                                <path
                                                    d="M13.7535 2.47502H11.5879V1.9969C11.5879 1.15315 10.9129 0.478149 10.0691 0.478149H7.90352C7.05977 0.478149 6.38477 1.15315 6.38477 1.9969V2.47502H4.21914C3.40352 2.47502 2.72852 3.15002 2.72852 3.96565V4.8094C2.72852 5.42815 3.09414 5.9344 3.62852 6.1594L4.07852 15.4688C4.13477 16.6219 5.09102 17.5219 6.24414 17.5219H11.7004C12.8535 17.5219 13.8098 16.6219 13.866 15.4688L14.3441 6.13127C14.8785 5.90627 15.2441 5.3719 15.2441 4.78127V3.93752C15.2441 3.15002 14.5691 2.47502 13.7535 2.47502ZM7.67852 1.9969C7.67852 1.85627 7.79102 1.74377 7.93164 1.74377H10.0973C10.2379 1.74377 10.3504 1.85627 10.3504 1.9969V2.47502H7.70664V1.9969H7.67852ZM4.02227 3.96565C4.02227 3.85315 4.10664 3.74065 4.24727 3.74065H13.7535C13.866 3.74065 13.9785 3.82502 13.9785 3.96565V4.8094C13.9785 4.9219 13.8941 5.0344 13.7535 5.0344H4.24727C4.13477 5.0344 4.02227 4.95002 4.02227 4.8094V3.96565ZM11.7285 16.2563H6.27227C5.79414 16.2563 5.40039 15.8906 5.37227 15.3844L4.95039 6.2719H13.0785L12.6566 15.3844C12.6004 15.8625 12.2066 16.2563 11.7285 16.2563Z"
                                                    fill=""
                                                />
                                                <path
                                                    d="M9.00039 9.11255C8.66289 9.11255 8.35352 9.3938 8.35352 9.75942V13.3313C8.35352 13.6688 8.63477 13.9782 9.00039 13.9782C9.33789 13.9782 9.64727 13.6969 9.64727 13.3313V9.75942C9.64727 9.3938 9.33789 9.11255 9.00039 9.11255Z"
                                                    fill=""
                                                />
                                                <path
                                                    d="M11.2502 9.67504C10.8846 9.64692 10.6033 9.90004 10.5752 10.2657L10.4064 12.7407C10.3783 13.0782 10.6314 13.3875 10.9971 13.4157C11.0252 13.4157 11.0252 13.4157 11.0533 13.4157C11.3908 13.4157 11.6721 13.1625 11.6721 12.825L11.8408 10.35C11.8408 9.98442 11.5877 9.70317 11.2502 9.67504Z"
                                                    fill=""
                                                />
                                                <path
                                                    d="M6.72245 9.67504C6.38495 9.70317 6.1037 10.0125 6.13182 10.35L6.3287 12.825C6.35683 13.1625 6.63808 13.4157 6.94745 13.4157C6.97558 13.4157 6.97558 13.4157 7.0037 13.4157C7.3412 13.3875 7.62245 13.0782 7.59433 12.7407L7.39745 10.2657C7.39745 9.90004 7.08808 9.64692 6.72245 9.67504Z"
                                                    fill=""
                                                />
                                            </svg>
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default DatabaseUsersTable;