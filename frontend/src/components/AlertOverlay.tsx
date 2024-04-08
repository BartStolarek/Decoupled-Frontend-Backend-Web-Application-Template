// A component that renders an overlay alert. It should be customizable to display different types of alerts (success, warning, error, info) and support optional timeout and redirect after timeout.

import React from 'react';
import { useAlert } from '@/hooks/useAlert'; // Adjust the import path as necessary

const AlertOverlay = () => {
    const { alert, hideAlert } = useAlert();

    if (!alert) return null;

    let backgroundColor = 'bg-green-500';
    switch (alert.type) {
        case 'error':
            backgroundColor = 'bg-red-500';
            break;
        case 'warning':
            backgroundColor = 'bg-yellow-500';
            break;
        case 'info':
            backgroundColor = 'bg-blue-500';
            break;
        case 'success':
        default:
            backgroundColor = 'bg-green-500';
            break;
    }

    return (
        <div className={`fixed inset-0 z-50 flex items-end justify-center px-4 py-6 pointer-events-none sm:p-6 sm:items-start sm:justify-end`}>
            <div className={`max-w-sm w-full bg-white shadow-lg rounded-lg pointer-events-auto ring-1 ring-black ring-opacity-5 overflow-hidden ${backgroundColor}`}>
                <div className="p-4">
                    <div className="flex items-center">
                        <div className="w-0 flex-1 flex justify-between">
                            <p className="w-full text-sm font-medium text-white">
                                {alert.title}
                            </p>
                            <p className="w-full text-sm font-medium text-white">
                                {alert.message}
                            </p>
                            <button onClick={hideAlert} className="ml-4 flex-shrink-0 bg-transparent text-white">
                                <span>Close</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AlertOverlay;
