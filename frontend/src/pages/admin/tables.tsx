import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import TableOne from "@/components/Tables/TableOne";
import TableThree from "@/components/Tables/TableThree";
import TableTwo from "@/components/Tables/TableTwo";
import TableFour from "@/components/Tables/TableFour";
import { useRequireAuth } from "@/hooks/useRequireAuth";

import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLayout";


const TablesPage = () => {

  const { isLoading } = useRequireAuth("Administrator");

  if (isLoading) {
    return <div>Loading...</div>;
  }
  return (
    <DefaultLayout>
      <Breadcrumb pageName="Tables" />

      <div className="flex flex-col gap-10">
        <TableOne />
        <TableTwo />
        <TableThree />
      </div>
    </DefaultLayout>
  );
};

export default TablesPage;
