import React, { useMemo } from 'react';

type SortDirection = 'ascending' | 'descending' | null;

export interface SortConfig {
    key: string | null;
    direction: SortDirection;
}

interface TableProps<T extends { [key: string]: any }> {
    tableName: string | null;
    data: T[];
    onSort: (key: keyof T) => void;
    sortConfig: SortConfig;
    includeActions?: boolean; // Optional, to include action column
    renderActions?: (item: T) => React.ReactNode; // Add this line
}

function DatabaseDynamicTable<T extends { [key: string]: any }>({
    tableName,
    data,
    onSort,
    sortConfig,
    includeActions,
    renderActions, // Add this line
}: TableProps<T>): JSX.Element {
    const sortedData = useMemo(() => {
        if (!sortConfig.key) return data;

        return [...data].sort((a, b) => {
            const valueA = a[sortConfig.key as keyof T];
            const valueB = b[sortConfig.key as keyof T];

            if (typeof valueA === 'string' && typeof valueB === 'string') {
                return sortConfig.direction === 'ascending'
                    ? valueA.localeCompare(valueB)
                    : valueB.localeCompare(valueA);
            }

            if (valueA < valueB) return sortConfig.direction === 'ascending' ? -1 : 1;
            if (valueA > valueB) return sortConfig.direction === 'ascending' ? 1 : -1;
            return 0;
        });
    }, [data, sortConfig]);

    return (
        <div className="rounded-sm border border-stroke bg-white px-5 pb-2.5 pt-6 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1">
            <h4 className="mb-6 text-xl font-semibold text-black dark:text-white">
                {tableName !== null ? tableName : ''}
            </h4>
            <div className="max-w-full overflow-x-auto">
                <table className="w-full table-auto">
                    <thead>
                        <tr className="bg-gray-2 text-left dark:bg-meta-4">
                            {data.length > 0 &&
                                Object.keys(data[0]).map((key) => (
                                    <th className="px-4 py-4 font-medium cursor-pointer text-black dark:text-white" key={key} onClick={() => onSort(key as keyof T)}>
                                        {key} {sortConfig.key === key && (sortConfig.direction === 'ascending' ? '↑' : '↓')}
                                    </th>
                                ))}
                            {includeActions && <th>Actions</th>}
                        </tr>
                    </thead>
                    <tbody>
                        {sortedData.map((item, index) => (
                            <tr key={index}>
                                {Object.values(item).map((value, i) => (
                                    <td className="border-b border-stroke px-4 py-5 dark:border-strokedark" key={i}><p className="text-black dark:text-white">{value as React.ReactNode}</p></td>
                                ))}
                                {includeActions && <td className="border-b border-stroke px-4 py-5 dark:border-strokedark">{renderActions && renderActions(item)}</td>}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default DatabaseDynamicTable;