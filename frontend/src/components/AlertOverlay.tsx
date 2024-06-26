// A component that renders an overlay alert. It should be customizable to display different types of alerts (success, warning, error, info) and support optional timeout and redirect after timeout.

import React from 'react';
import { useAlert } from '@/hooks/useAlert'; // Adjust the import path as necessary

const AlertOverlay = () => {
    const { alert, hideAlert } = useAlert();

    if (!alert) return null;

    const alertStyles = {
        success: 'bg-success border-success text-white',
        error: 'bg-error border-error text-white',
        warning: 'bg-warning border-warning text-white',
        info: 'bg-info border-info text-white'
    };

    return (
        <div className="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
            <div className={`w-full max-w-md border-l-6 ${alertStyles[alert.type]} bg-opacity-[15%] px-7 py-8 shadow-md`}>
                <div className="flex items-center">
                    {/* Render the appropriate icon based on the alert type */}
                    <div className={`mr-5 flex h-9 w-9 items-center justify-center rounded-lg ${alertStyles[alert.type]} bg-opacity-30`}>
                        {/* Icon SVG */}
                    </div>
                    <div className="w-full">
                        {/* Display the title if available */}
                        {alert.title && <h4 className={`mb-2 text-xl font-semibold ${alertStyles[alert.type]}`}>{alert.title}</h4>}
                        <h5 className={`mb-3 text-lg ${alertStyles[alert.type]}`}>
                            {alert.type === 'success' ? 'Success' : alert.type === 'error' ? 'Error' : 'Warning'}
                        </h5>
                        <p className={`leading-relaxed ${alertStyles[alert.type]}`}>{alert.message}</p>
                    </div>
                </div>
                <button
                    onClick={hideAlert}
                    className="mt-4 px-4 py-2 bg-gray-100 text-gray-700 rounded-md hover:bg-gray-200"
                >
                    Close
                </button>
            </div>
        </div>
    );
};

export default AlertOverlay;
