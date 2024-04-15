import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import DatabaseRolesTable from "@/components/Tables/DatabaseRolesTable";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';


const RolesPage = () => {

  const { isLoading } = useRequireAuth("Administrator");

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <>
    <Navbar />
    <DefaultLayout>
      <Breadcrumb pageName="Roles" />

      <div className="flex flex-col gap-10">
        <DatabaseRolesTable />
      </div>
    </DefaultLayout>
    <Footer />
    </>
  );
};

export default RolesPage;
