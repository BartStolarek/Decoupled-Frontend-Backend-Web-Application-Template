import React, { useMemo } from 'react';

type SortDirection = 'ascending' | 'descending' | null;

export interface SortConfig {
    key: string | null;
    direction: SortDirection;
}

interface TableProps<T extends { [key: string]: any }> {
    data: T[];
    onSort: (key: keyof T) => void;
    sortConfig: SortConfig;
    includeActions?: boolean; // Optional, to include action column
    renderActions?: (item: T) => React.ReactNode; // Add this line
}

function DatabaseDynamicTable<T extends { [key: string]: any }>({
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
        <div className="overflow-x-auto">
            <table className="w-full">
                <thead>
                    <tr>
                        {data.length > 0 &&
                            Object.keys(data[0]).map((key) => (
                                <th key={key} onClick={() => onSort(key as keyof T)}>
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
                                <td key={i}>{value as React.ReactNode}</td>
                            ))}
                            {includeActions && <td>{renderActions && renderActions(item)}</td>}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default DatabaseDynamicTable;