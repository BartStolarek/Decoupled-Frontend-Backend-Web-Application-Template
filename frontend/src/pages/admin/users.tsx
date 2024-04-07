import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import DatabaseUsersTable from "@/components/Tables/DatabaseUsersTable";
import useRequireAuth from '@/hooks/useRequireAuth'
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import AlertComponent from '@/components/Alert';
import Navbar from '@/components/Navbar';
import Footer from '@/components/Footer';


const UsersPage = () => {

  const { loading } = useRequireAuth("Administrator");

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <>
    <Navbar />
    <AlertComponent />
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
