// components/AlertComponent.tsx
import React from 'react';
import { useAlert } from '@/contexts/AlertContext';

const AlertComponent = () => {
  // Including title from the useAlert hook
  const { title, message, type, hideAlert } = useAlert();

  // Checking if there's no message to display, then don't render the component
  if (!message) return null;

  // Define the styles based on the type of alert
  const alertStyles = {
    success: 'bg-[#34D399] border-[#34D399] text-white',
    error: 'bg-[#F87171] border-[#F87171] text-white',
    warning: 'bg-warning border-warning text-[#9D5425]',
  };

  return (
    <div className="fixed top-0 left-0 right-0 bottom-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
      <div className={`w-full max-w-md border-l-6 ${alertStyles[type]} bg-opacity-[15%] px-7 py-8 shadow-md`}>
        <div className="flex items-center">
          {/* Render the appropriate icon based on the alert type */}
          <div className={`mr-5 flex h-9 w-9 items-center justify-center rounded-lg ${alertStyles[type]} bg-opacity-30`}>
            {/* Icon SVG */}
          </div>
          <div className="w-full">
            {/* Display the title if available */}
            {title && <h4 className={`mb-2 text-xl font-semibold ${alertStyles[type]}`}>{title}</h4>}
            <h5 className={`mb-3 text-lg ${alertStyles[type]}`}>
              {type === 'success' ? 'Success' : type === 'error' ? 'Error' : 'Warning'}
            </h5>
            <p className={`leading-relaxed ${alertStyles[type]}`}>{message}</p>
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

export default AlertComponent;
