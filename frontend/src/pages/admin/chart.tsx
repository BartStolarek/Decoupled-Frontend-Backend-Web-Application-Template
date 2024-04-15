import Chart from "@/components/Charts/page";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import React from "react";
import { useRequireAuth } from "@/hooks/useRequireAuth";


const BasicChartPage: React.FC = () => {
  const { isLoading } = useRequireAuth("Administrator");

  if (isLoading) {
    return <div>Loading...</div>;
  }
  return (
    <DefaultLayout>
      <Chart />
    </DefaultLayout>
  );
};

export default BasicChartPage;
