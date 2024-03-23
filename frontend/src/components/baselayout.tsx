// components/BaseLayout.tsx
import React, { ReactNode } from 'react';

type BaseLayoutProps = {
  children: ReactNode;
  title: string;
};

const BaseLayout: React.FC<BaseLayoutProps> = ({ children, title }) => {
  return (
    <html>
      <head>
        <title>{title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {/* Ensure you import your Tailwind CSS file here */}
      </head>
      {/* <body>{children}</body> */}
      <body>Hello World</body>
    </html>
    
  );
};

export default BaseLayout;
