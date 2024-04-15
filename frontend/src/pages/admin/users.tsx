import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import DatabaseUsersTable from "@/components/Tables/DatabaseUsersTable";
import { useRequireAuth } from "@/hooks/useRequireAuth";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';


const UsersPage = () => {

  const { isLoading } = useRequireAuth("Administrator");

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <>
    <Navbar />
    <DefaultLayout>
      <Breadcrumb pageName="Users" />

      <div className="flex flex-col gap-10">
        <DatabaseUsersTable />
      </div>
    </DefaultLayout>
    <Footer />
    </>
  );
};

export default UsersPage;
